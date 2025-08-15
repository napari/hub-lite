"""Fetch napari plugin data from the NPE2 API and process it into a DataFrame.

This script fetches plugin data, flattens nested structures, and saves the cleaned data to CSV
files.
"""

import dataclasses
import json
import logging
import re
import string
import sys
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from create_static_html_files import PluginPageData, get_plugin_types

API_SUMMARY_URL = "https://npe2api.vercel.app/api/extended_summary"
API_PYPI_BASE_URL = "https://npe2api.vercel.app/api/pypi/"
API_MANIFEST_BASE_URL = "https://npe2api.vercel.app/api/manifest/"

HOME_PYPI_REGEX = r"(.*)(pypi.org)(/)(project)(/)(.*)"
HOME_GITHUB_REGEX = r"https?://github\.com/[^/]+/[^/]+(?:\.git)?/?$"


# Configure logging
logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Increased timeout for requests
DEFAULT_TIMEOUT = 30
# Number of concurrent threads, balanced for the connection pool size, reduce warnings are frequent
MAX_WORKERS = 100


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

    def fetch_summary(self):
        """Fetches the summary data for all plugins"""
        logger.info(f"Fetching summary data from URL: {API_SUMMARY_URL}")
        return self.get(API_SUMMARY_URL)

    def fetch_manifest(self, plugin_name: str):
        """Fetches the manifest data for a given plugin"""
        url = urljoin(API_MANIFEST_BASE_URL, plugin_name)
        logger.info(f"Fetching data for manifest for: {plugin_name} from URL: {url}")
        return self.get(url)

    def fetch_pypi_info(self, plugin_normalized_name: str):
        """Fetches PyPI information for a given plugin (expects normalized pluginname)."""
        url = urljoin(API_PYPI_BASE_URL, plugin_normalized_name)
        logger.info(f"Fetching PyPI info for: {plugin_normalized_name} from URL: {url}")
        return self.get(url)

    def close(self):
        """Close the requests session."""
        self.session.close()


# Create a global API client instance to use for all API requests
api_client = APIClient()


# --- Helper Functions ---
def get_license(package_metadata: dict) -> str:
    """For license metadata, we subsitute a short phrase, truncate the text,
    or add a sensible default if the text is unavailable.
    """
    package_license = package_metadata["license"] or "Unavailable"
    if "BSD 3-Clause" in package_license:
        return "BSD 3-Clause"
    elif "MIT License" in package_license:
        return "MIT"
    elif "Apache" in package_license:
        return "Apache"
    elif len(package_license) > 30:
        return f"{package_license[:30]}..."
    return package_license


def get_authors_and_emails(package_metadata: dict) -> str:
    authors = [
        author.strip() for author in (package_metadata["author"] or "").split(",")
    ]
    emails = [
        email.strip() for email in (package_metadata["author_email"] or "").split(",")
    ]
    if not authors:
        authors = extract_author_names(emails)
    return authors or [], emails or []


def extract_author_names(emails: list[str]) -> list[str]:
    """
    Extract and clean author names from an email field.

    This function handles a string containing one or more authors, each potentially formatted as:
    - 'Name <email>'
    - 'email' only
    - Names with surrounding quotation marks

    It removes email addresses, cleans up the names, and returns a comma-separated string of author
    names.

    Args:
        email (Optional[str]): A string containing author information.

    Returns:
        str: A comma-separated string of cleaned author names, or an empty string if the input is
        invalid.
    """
    authors = []
    for email in emails:
        # Match a pattern with a name and an email (e.g., 'Name <email>')
        match = re.match(r"(.*?)\s*<.*?>", email.strip())

        if match:
            # Extract and clean the author name
            authors.append(match.group(1).replace('"', "").strip())
        else:
            # If no match, clean and add the raw string
            authors.append(email.replace('"', "").strip())

    return authors


def get_project_home_url(plugin_data: dict) -> tuple[str | None, str | None]:
    """
    Expands the project URL in the plugin data dictionary.

    This function checks if the 'project_url' key exists in
    the plugin data and extracts homepage and github repository URLs,
    if present.

    Parameters
    ----------
    plugin_data : dict
        The dictionary containing plugin data.

    Returns
    -------
        home_github : str | None
        home_other : str | None
    """
    urls = plugin_data.get("project_url", [])

    # If urls do not exist, we try using the 'home_page' key (like in the old metadata spec).
    if not urls and "home_page" in plugin_data:
        urls = [f"homepage, {plugin_data['home_page']}"]

    home_github = home_other = None
    for url_info in urls:
        label, url = url_info.split(", ")
        plugin_data[normalize_label(label)] = url
        if re.match(HOME_GITHUB_REGEX, url):
            # If url matches github repository link structure,
            # we display the github icon.
            # Otherwise, display the homepage label
            # as some other url
            home_github = url
        elif label == "homepage":
            home_other = url

    return home_github, home_other


def normalize_label(label: str) -> str:
    """Normalize project URL label.

    Code reproduced from:
    https://packaging.python.org/en/latest/specifications/well-known-project-urls/#label-normalization
    """
    chars_to_remove = string.punctuation + string.whitespace
    removal_map = str.maketrans("", "", chars_to_remove)
    return label.translate(removal_map).lower()


def get_version_release_date(pypi_info: dict, release: str) -> str | None:
    """
    Extracts the release date of the given version from the PyPI plugin information.

    Args:
        pypi_info (dict): The plugin information fetched from PyPI.
        release (str): Release version to look for.

    Returns:
        str: The release date of given version, or an empty string if not found.
    """
    release_info = pypi_info.get("releases", {}).get(release, {})
    if release_info:
        release_timestamp = release_info[0].get("upload_time")
        return release_timestamp.split("T")[0]


# --- Main Data Processing Function ---
def build_plugins_list() -> list[PluginPageData]:
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
    A list of PluginPageData objects containing the processed plugin data.
    """
    extended_summary = api_client.fetch_summary()

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        all_plugin_data = executor.map(
            get_plugin_page_data_from_api,
            extended_summary,
        )

    return sorted(
        all_plugin_data,
        key=lambda p: p.modified_at,
        reverse=True,
    )


def get_plugin_page_data_from_api(plugin_summary_data):
    plugin_normalized_name = plugin_summary_data.get("normalized_name")
    manifest_info = api_client.fetch_manifest(plugin_normalized_name)

    # some PyPI info is not included in the manifest
    pypi_info = api_client.fetch_pypi_info(plugin_normalized_name)
    # this is much of the same as what's in the pypi_info
    package_metadata = manifest_info.get("package_metadata", {})

    # conda_info is not currently used

    name = manifest_info.get("name", plugin_summary_data.get("name", ""))
    display_name = manifest_info.get(
        "display_name", plugin_summary_data.get("display_name", "")
    )
    # releases are sorted in descending order
    plugin_first_release = plugin_summary_data["pypi_versions"][-1]
    plugin_latest_release = plugin_summary_data["pypi_versions"][0]
    initial_release_date = get_version_release_date(pypi_info, plugin_first_release)
    last_updated_date = get_version_release_date(pypi_info, plugin_latest_release)
    authors, emails = get_authors_and_emails(package_metadata)
    package_license = get_license(package_metadata)
    home_pypi = pypi_info.get(
        "home_page",
        f"https://pypi.org/project/{plugin_normalized_name}/",
    )
    home_github, home_other = get_project_home_url(plugin_summary_data)

    contributions = manifest_info.get("contributions", {})
    reader_patterns = list(
        set(
            ext
            for reader in contributions["readers"] or []
            for ext in reader["filename_patterns"]
        )
    )

    writer_extensions = list(
        set(
            ext
            for writer in contributions["writers"] or []
            for ext in writer["filename_extensions"]
        )
    )

    widgets = [widget["display_name"] for widget in contributions["widgets"] or []]

    sample_data = [
        sample["display_name"] for sample in contributions["sample_data"] or []
    ]

    return PluginPageData(
        normalized_name=plugin_normalized_name,
        name=name,
        display_name=display_name,
        version=plugin_latest_release,
        created_at=initial_release_date,
        modified_at=last_updated_date,
        authors=authors,
        author_emails=emails,
        license=package_license,
        home_pypi=home_pypi,
        home_github=home_github,
        home_other=home_other,
        summary=plugin_summary_data.get("summary", ""),
        package_metadata_requires_python=package_metadata.get("requires_python", ""),
        package_metadata_requires_dist=package_metadata.get("requires_dist", []),
        package_metadata_description=package_metadata.get("description", ""),
        package_metadata_classifiers=package_metadata.get("classifiers", []),
        contributions_readers_filename_patterns=reader_patterns,
        contributions_writers_filename_extensions=writer_extensions,
        contributions_widgets=widgets,
        contributions_sample_data=sample_data,
    )


def create_search_index(plugins: list[PluginPageData], data_dir: str):
    search_index = [
        {
            "name": plugin.name,
            "display_name": plugin.display_name,
            "normalized_name": plugin.normalized_name,
            "summary": plugin.summary,
            "authors": plugin.authors,
            "author_emails": plugin.author_emails,
            "filename_patterns": plugin.contributions_readers_filename_patterns,
            "filename_extensions": plugin.contributions_writers_filename_extensions,
            "widgets": plugin.contributions_widgets,
            "sample_data": plugin.contributions_sample_data,
            "contributions": get_plugin_types(plugin),
        }
        for plugin in plugins
    ]

    # newline-delimited JSON format for search index
    # allows for efficient streaming and parsing
    with open(f"{data_dir}/search_index.ndjson", "w") as file:
        for entry in search_index:
            file.write(json.dumps(entry) + "\n")


if __name__ == "__main__":
    # Get path to target build directory and data directory from command line arguments
    # or set default
    build_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    data_dir = f"{build_dir}/data"

    # Create and populate a list of all plugins with the data needed for their HTML pages
    try:
        plugins = build_plugins_list()
    finally:
        api_client.close()

    # Save the final list of plugin page information and a "search index" JSON file
    with open(f"{data_dir}/plugin_page_data.json", "w", encoding="utf-8") as f:
        json.dump(
            [dataclasses.asdict(p) for p in plugins],
            f,
            indent=2,
            ensure_ascii=False,
        )

    create_search_index(plugins, data_dir)
