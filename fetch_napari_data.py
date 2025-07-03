"""Fetch napari plugin data from the NPE2 API and process it into a DataFrame.

This script fetches plugin data, flattens nested structures, and saves the cleaned data to CSV files.
"""

from __future__ import annotations

import logging
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import lru_cache
from pathlib import Path
from urllib.parse import urljoin

import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

API_SUMMARY_URL = "https://npe2api.vercel.app/api/extended_summary"
API_CONDA_MAP_URL = "https://npe2api.vercel.app/api/conda"
API_CONDA_BASE_URL = "https://npe2api.vercel.app/api/conda/"
API_PYPI_BASE_URL = "https://npe2api.vercel.app/api/pypi/"
API_MANIFEST_BASE_URL = "https://npe2api.vercel.app/api/manifest/"

# Define columns needed for the plugin html page
PLUGIN_PAGE_COLUMNS = [
    "normalized_name",
    "name",
    "display_name",
    "version",
    "created_at",
    "modified_at",
    "author",
    "package_metadata_author_email",
    "license",
    "home",
    "package_metadata_home_page",
    "summary",
    "package_metadata_requires_python",
    "package_metadata_requires_dist",
    "package_metadata_description",
    "package_metadata_classifier",
    "package_metadata_project_url",
    "contributions_readers_0_command",
    "contributions_writers_0_command",
    "contributions_widgets_0_command",
    "contributions_sample_data_0_command",
    "contributions_readers_0_filename_patterns",
    "contributions_writers_0_filename_extensions",
    "contributions_writers_1_filename_extensions",
]

# Configure logging
logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

DEFAULT_TIMEOUT = 30  # Increased timeout for requests
MAX_WORKERS = 25  # Number of concurrent threads, balanced for the connection pool size, reduce if warnings are frequent
CHUNK_SIZE = 50  # Process plugins in chunks


class APIClient:
    """HTTP client with connection pooling and retry logic.

    For resource conservation, exponential backoff is used for retries.
    """

    def __init__(self, max_retries=3, backoff_factor=0.3):
        self.session = requests.Session()

        # Configure retry strategy
        retry_strategy = Retry(
            total=max_retries,
            backoff_factor=backoff_factor,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET"],
        )

        # Use the requests adapter to enable retries and tie it to the session
        adapter = HTTPAdapter(
            max_retries=retry_strategy,
            pool_connections=50,
            pool_maxsize=100,
        )
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

    def get(self, url: str, timeout: int = DEFAULT_TIMEOUT) -> dict | None:
        """Fetch JSON data from URL with retries and connection pooling."""
        try:
            response = self.session.get(url, timeout=timeout)
            response.raise_for_status()
            logger.info(f"Successfully fetched data: {url}")
            return response.json()
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP error occurred for {url}: {e}")
        except requests.exceptions.ConnectionError as e:
            logger.error(f"Connection error occurred for {url}: {e}")
        except requests.exceptions.Timeout as e:
            logger.error(f"Timeout error occurred for {url}: {e}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Request error occurred for {url}: {e}")
        except Exception as e:
            logger.error(f"Unexpected error occurred for {url}: {e}")
        return None

    def close(self):
        """Close the requests session."""
        self.session.close()


# Create a global API client instance to use for all API requests
api_client = APIClient()


# --- Helper Functions ---
def extract_author_names(email: str | list[str]) -> str:
    """
    Extract and clean author names from an email field.

    This function handles a string containing one or more authors, each potentially formatted as:
    - 'Name <email>'
    - 'email' only
    - Names with surrounding quotation marks

    It removes email addresses, cleans up the names, and returns a comma-separated string of author names.

    Args:
        email (Optional[str]): A string containing author information.

    Returns:
        str: A comma-separated string of cleaned author names, or an empty string if the input is invalid.
    """
    if not isinstance(email, str) or not email.strip():
        return ""

    # Split the string by comma to process multiple authors
    authors = email.split(",")
    clean_authors = []

    for author in authors:
        # Match a pattern with a name and an email (e.g., 'Name <email>')
        match = re.match(r"(.*?)\s*<.*?>", author.strip())

        if match:
            # Extract and clean the author name
            clean_authors.append(match.group(1).replace('"', "").strip())
        else:
            # If no match, clean and add the raw string
            clean_authors.append(author.replace('"', "").strip())

    return ", ".join(clean_authors)


@lru_cache(maxsize=1000)
def classify_url(url: str) -> str:
    """
    Classify package source code URL in a dataframe to a string identifying the package repository name.

    Currently, this categorizes a URL to be 'pypi', 'github', or 'other'.

    Use lru_cache since the same URL patterns may be processed multiple times when handling the dataframe.
    Caching prevents redundant string matching operations for frequently occurring URLs, improving efficiency.
    """
    categories = {
        "pypi.org": "pypi",
        "github.com": "github",
    }

    if pd.notnull(url):
        for keyword, category in categories.items():
            if keyword in url:
                return category
    return "other"


def flatten_and_merge(original, additional, parent_key="") -> None:
    """
    Recursively flattens a nested dictionary or list of dictionaries and merges the result into the original dictionary.

    This function traverses the `additional` dictionary, flattening any nested dictionaries or lists of dictionaries,
    and adds their key-value pairs to the `original` dictionary. Keys from nested structures are concatenated with
    their parent keys using underscores to create unique, flat keys.

    Parameters
    ----------
    original : dict
        The dictionary to merge flattened key-value pairs into.
    additional : dict
        The dictionary (possibly nested) to flatten and merge.
    parent_key : str, optional
        The base key to use for nested keys (default is '').

    Returns
    -------
    None
        The function modifies the `original` dictionary in place.
    """
    for key, value in additional.items():
        new_key = f"{parent_key}_{key}" if parent_key else key
        if isinstance(value, dict):
            flatten_and_merge(original, value, new_key)
        elif isinstance(value, list) and all(isinstance(elem, dict) for elem in value):
            # Handle list of dictionaries separately
            for i, elem in enumerate(value):
                flatten_and_merge(original, elem, f"{new_key}_{i}")
        else:
            original.setdefault(new_key, value)


# --- API Fetch Functions ---
def fetch_conda(plugin_name: str):
    """Fetches Conda info and creates an HTML file for it"""
    url = urljoin(API_CONDA_BASE_URL, plugin_name)
    logger.info(f"Fetching conda data for plugin: {plugin_name}")
    return api_client.get(url)


def fetch_plugin(url: str):
    """Fetches plugin summary from the given URL"""
    logger.info(f"Fetching plugin data from: {url}")
    return api_client.get(url)


def fetch_manifest(plugin_name: str):
    """Fetches the manifest data for a given plugin"""
    url = urljoin(API_MANIFEST_BASE_URL, plugin_name)
    logger.info(f"Fetching manifest for: {plugin_name}")
    return api_client.get(url)


def fetch_pypi(plugin_name: str):
    """Fetches PyPI data for a given plugin"""
    url = urljoin(API_PYPI_BASE_URL, plugin_name)
    logger.info(f"Fetching PyPI data for: {plugin_name}")
    return api_client.get(url)


def get_plugin_summary(url: str) -> list:
    """
    Fetches the plugin summary from the given URL and returns it as a list.
    If no summary is retrieved, an empty list is returned.

    Args:
        url (str): The API URL to fetch the plugin summary.

    Returns:
        list: The plugin summary as a list, or an empty list if none is retrieved.
    """
    plugin_summary = fetch_plugin(url)
    return plugin_summary if plugin_summary else []


def get_version_release_date(pypi_info: dict, release: str) -> str:
    """
    Extracts the release date of the given version from the PyPI plugin information.

    Args:
        pypi_info (dict): The plugin information fetched from PyPI.
        release (str): Release version to look for.

    Returns:
        str: The release date of given version, or an empty string if not found.
    """
    release_info = pypi_info.get("releases", {}).get(release, [])
    if release_info and len(release_info) > 0:
        # we don't mind which release artifact we look at, as we only want the date
        release_datetime = release_info[0].get("upload_time", "")
        return release_datetime
    return ""


def process_plugin(plugin: dict, conda_name_map: dict) -> dict:
    """Process a single plugin and fetch its additional data."""
    plugin_data = plugin.copy()
    plugin_normalized_name = plugin.get("normalized_name")

    # Return and don't fetch data if there is no normalized name
    if not plugin_normalized_name:
        return plugin_data

    # Fetch all data concurrently for this plugin
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = {}

        # Submit conda fetch if needed
        if (
            plugin_normalized_name in conda_name_map
            and conda_name_map[plugin_normalized_name] is not None
        ):
            futures["conda"] = executor.submit(fetch_conda, plugin_normalized_name)

        # Always fetch manifest and pypi
        futures["manifest"] = executor.submit(fetch_manifest, plugin_normalized_name)
        futures["pypi"] = executor.submit(fetch_pypi, plugin_normalized_name)

        # Collect results
        results = {}
        for key, future in futures.items():
            try:
                results[key] = future.result()
            except Exception as e:
                logger.error(f"Error fetching {key} for {plugin_normalized_name}: {e}")
                results[key] = None

    # Process conda info
    if "conda" in results and results["conda"]:
        conda_info = {
            "conda_name": results["conda"].get("name"),
            "conda_html_url": results["conda"].get("html_url"),
            "home": results["conda"].get("home"),
        }
        plugin_data.update(conda_info)

    # Process pypi info
    if results.get("pypi"):
        pypi_info = results["pypi"]
        # Get release dates
        pypi_versions = plugin_data.get("pypi_versions", [])
        if pypi_versions:
            plugin_first_release = pypi_versions[-1]
            plugin_latest_release = pypi_versions[0]
            initial_release_date = get_version_release_date(
                pypi_info, plugin_first_release
            )
            last_updated_date = get_version_release_date(
                pypi_info, plugin_latest_release
            )
            plugin_data.update(
                {
                    "created_at": initial_release_date,
                    "modified_at": last_updated_date,
                }
            )

    # Process manifest info
    if results.get("manifest"):
        flatten_and_merge(plugin_data, results["manifest"])

    return plugin_data


# --- Main Data Processing Function ---
def build_plugins_dataframe() -> pd.DataFrame:
    """
    Fetches napari plugin data from the NPE2 API, enriches it with Conda and manifest information,
    flattens nested structures, and returns a cleaned pandas DataFrame.

    The function performs the following steps:
    - Retrieves a summary list of plugins from the NPE2 API.
    - For each plugin, fetches additional Conda and manifest data.
    - Flattens and merges nested dictionary structures into a single-level dictionary.
    - Aggregates all plugin data into a pandas DataFrame.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the enriched and flattened plugin data. Returns an empty DataFrame if no data is fetched.
    """
    print("Fetching plugin summary...")
    summary_list = get_plugin_summary(API_SUMMARY_URL)
    if not summary_list:
        logger.error("Failed to fetch plugin summary")
        return pd.DataFrame()

    print(f"Found {len(summary_list)} plugins")

    print("Fetching conda name map...")
    conda_name_map = fetch_plugin(API_CONDA_MAP_URL) or {}

    all_plugin_data = []

    print("Processing plugins...")
    # Process plugins in chunks for better progress reporting
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        # Submit all tasks
        future_to_plugin = {
            executor.submit(process_plugin, plugin, conda_name_map): plugin
            for plugin in summary_list
        }

        # Process completed tasks
        completed = 0
        for future in as_completed(future_to_plugin):
            try:
                plugin_data = future.result()
                all_plugin_data.append(plugin_data)
                completed += 1
                if completed % 10 == 0:
                    print(f"Processed {completed}/{len(summary_list)} plugins...")
            except Exception as e:
                plugin = future_to_plugin[future]
                logger.error(
                    f"Error processing plugin {plugin.get('normalized_name', 'unknown')}: {e}"
                )

    print(f"Successfully processed {len(all_plugin_data)} plugins")
    return pd.DataFrame(all_plugin_data)


def optimize_dataframe_cleaning(df_plugins: pd.DataFrame) -> pd.DataFrame:
    """Optimize DataFrame cleaning operations using vectorized operations."""

    # Vectorized author extraction
    def extract_author_vectorized(series):
        return series.apply(lambda x: extract_author_names(x) if pd.notna(x) else "")

    # Update author column using vectorized operations
    mask_author = df_plugins["author"].isna() | df_plugins["author"].str.contains(
        '"', na=False
    )
    df_plugins.loc[mask_author, "author"] = extract_author_vectorized(
        df_plugins.loc[mask_author, "package_metadata_author_email"]
    )

    # Vectorized license processing
    df_plugins["license"] = df_plugins["license"].fillna("Unavailable")

    # Apply license replacements using vectorized string operations
    license_replacements = {
        "BSD 3-Clause": lambda s: s.str.contains("BSD 3-Clause", na=False),
        "MIT": lambda s: s.str.contains("MIT License", na=False),
    }

    for replacement, condition in license_replacements.items():
        mask = condition(df_plugins["license"])
        df_plugins.loc[mask, "license"] = replacement

    # Truncate long licenses with quotes
    mask_quotes = df_plugins["license"].str.contains('"', na=False)
    df_plugins.loc[mask_quotes, "license"] = (
        df_plugins.loc[mask_quotes, "license"].str[:30] + "..."
    )

    # Set home_type using vectorized operations
    df_plugins["home_type"] = df_plugins["home"].apply(classify_url)

    # Create home columns using vectorized operations
    df_plugins["home_pypi"] = df_plugins["home"].where(
        df_plugins["home_type"] == "pypi", ""
    )
    df_plugins["home_github"] = df_plugins["home"].where(
        df_plugins["home_type"] == "github", ""
    )
    df_plugins["home_other"] = df_plugins["home"].where(
        df_plugins["home_type"] == "other", ""
    )

    # Fill empty home_pypi values
    mask_empty_pypi = df_plugins["home_pypi"] == ""
    df_plugins.loc[mask_empty_pypi, "home_pypi"] = (
        "https://pypi.org/project/" + df_plugins.loc[mask_empty_pypi, "name"]
    )

    # Drop temporary column
    df_plugins.drop("home_type", axis=1, inplace=True)

    return df_plugins


if __name__ == "__main__":
    start_time = time.time()

    # Get path to target build directory and data directory from command line arguments
    # or set default
    build_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    # Set data directory and create if needed
    (data_dir := Path(f"{build_dir}/data")).mkdir(exist_ok=True)

    try:
        # Create and populate a raw DataFrame with plugin data
        df_plugins = build_plugins_dataframe()

        # Save raw dataframe as a csv. Useful for debugging since dataframe df_plugins
        # is being modified in place in the following code.
        df_plugins.to_csv(f"{data_dir}/raw_napari_plugins.csv")

        # Clean raw DataFrame by removing columns that are mostly empty, keep columns that have at least 20 non-missing values
        df_plugins.dropna(axis=1, thresh=20, inplace=True)

        # Create a dictionary of column names and their count of values
        column_counts = {
            column: df_plugins[column].count() for column in df_plugins.columns
        }
        # Create a sorted dictionary
        sorted_column_counts = sorted(
            column_counts.items(), key=lambda item: item[1], reverse=True
        )

        # Save the cleaned DataFrame to a CSV file
        df_plugins.to_csv(f"{data_dir}/cleaned_napari_plugins.csv")

        # Modify in place the DataFrame to keep only the columns needed for the plugin html page
        # Filter to keep only columns that exist
        existing_columns = [
            col for col in PLUGIN_PAGE_COLUMNS if col in df_plugins.columns
        ]
        df_plugins = df_plugins[existing_columns]

        # Convert and format 'created_at' and 'modified_at' columns
        df_plugins["created_at"] = pd.to_datetime(
            df_plugins["created_at"], format="mixed"
        ).dt.date
        df_plugins["modified_at"] = pd.to_datetime(
            df_plugins["modified_at"], format="mixed"
        ).dt.date

        # Use optimized cleaning function
        df_plugins = optimize_dataframe_cleaning(df_plugins)

        # Save the final DataFrame of plugin page information to a CSV file
        df_plugins.to_csv(f"{data_dir}/final_plugins.csv")

        elapsed_time = time.time() - start_time
        print(f"Total execution time: {elapsed_time:.2f} seconds")
        print(f"Processed {len(df_plugins)} plugins successfully")

    finally:
        # Clean up
        api_client.close()
