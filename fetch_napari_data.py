"""Fetch napari plugin data from the NPE2 API and process it into a DataFrame.

This script fetches plugin data, flattens nested structures, and saves the cleaned data to CSV files.
"""
import logging
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from typing import Optional
from urllib.parse import urljoin

import requests
import pandas as pd


API_SUMMARY_URL = 'https://npe2api.vercel.app/api/extended_summary'
API_CONDA_BASE_URL = 'https://npe2api.vercel.app/api/conda/'
API_MANIFEST_BASE_URL = 'https://npe2api.vercel.app/api/manifest/'

# Define columns needed for the plugin html page
PLUGIN_PAGE_COLUMNS = [
    'normalized_name',
    'name',
    'display_name',
    'version',
    'created_at',
    'modified_at',
    'author',
    'package_metadata_author_email',
    'license',
    'home',
    'package_metadata_home_page',
    'summary',
    'package_metadata_requires_python',
    'package_metadata_requires_dist',
    'package_metadata_description',
    'package_metadata_classifier',
    'package_metadata_project_url',
    'contributions_readers_0_command',
    'contributions_writers_0_command',
    'contributions_widgets_0_command',
    'contributions_sample_data_0_command',
    'contributions_readers_0_filename_patterns',
    'contributions_writers_0_filename_extensions',
    'contributions_writers_1_filename_extensions'
]

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

DEFAULT_TIMEOUT = 10  # Timeout for requests in seconds

# --- Helper Functions ---
def extract_author_names(email: Optional[str]) -> str:
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
        return ''

    # Split the string by comma to process multiple authors
    authors = email.split(',')
    clean_authors = []

    for author in authors:
        # Match a pattern with a name and an email (e.g., 'Name <email>')
        match = re.match(r'(.*?)\s*<.*?>', author.strip())

        if match:
            # Extract and clean the author name
            clean_authors.append(match.group(1).replace('"', '').strip())
        else:
            # If no match, clean and add the raw string
            clean_authors.append(author.replace('"', '').strip())

    return ', '.join(clean_authors)

def classify_url(url: str) -> str:
    """
    Classify package source code URL in a dataframe to a string identifying the package repository name.
     
    Currently, this categorizes a URL to be 'pypi', 'github', or 'other'.
    """
    categories = {
        'pypi.org': 'pypi',
        'github.com': 'github',
    }

    if pd.notnull(url):
        for keyword, category in categories.items():
            if keyword in url:
                return category
    return 'other'

def flatten_and_merge(original, additional, parent_key='') -> None:
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
    """ Fetches Conda info and creates an HTML file for it """
    url = urljoin(API_CONDA_BASE_URL, plugin_name)
    logger.info(f"Fetching data for plugin: {plugin_name} from URL: {url}")
    try:
        response = requests.get(url, timeout=DEFAULT_TIMEOUT)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx, 5xx)
        logger.info(f"Successfully fetched data for plugin: {plugin_name}")
        return response.json()  # Assuming JSON response
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error occurred for plugin `{plugin_name}`: {e}")
    except requests.exceptions.ConnectionError as e:
        logger.error(f"Connection error occurred while fetching `{plugin_name}`: {e}")
    except requests.exceptions.Timeout as e:
        logger.error(f"Timeout error while fetching `{plugin_name}`: {e}")
    except requests.exceptions.RequestException as e:
        logger.error(f"An error occurred while fetching `{plugin_name}`: {e}")
    return None

def fetch_plugin(url: str):
    """ Fetches plugin summary from the given URL """
    logger.info(f"Fetching data from URL: {url}")
    try:
        response = requests.get(url, timeout=DEFAULT_TIMEOUT)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx, 5xx)
        logger.info(f"Successfully fetched data.")
        return response.json()  # Assuming JSON response
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error occurred for plugin `{plugin_name}`: {e}")
    except requests.exceptions.ConnectionError as e:
        logger.error(f"Connection error occurred while fetching `{plugin_name}`: {e}")
    except requests.exceptions.Timeout as e:
        logger.error(f"Timeout error while fetching `{plugin_name}`: {e}")
    except requests.exceptions.RequestException as e:
        logger.error(f"An error occurred while fetching `{plugin_name}`: {e}")
    return None
    
def fetch_manifest(plugin_name: str):
    """ Fetches the manifest data for a given plugin """
    url = urljoin(API_MANIFEST_BASE_URL, plugin_name)
    logger.info(f"Fetching data for manifest for: {plugin_name} from URL: {url}")
    try:
        response = requests.get(url, timeout=DEFAULT_TIMEOUT)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx, 5xx)
        logger.info(f"Successfully fetched data for plugin: {plugin_name}")
        return response.json()  # Assuming JSON response
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error occurred for plugin `{plugin_name}`: {e}")
    except requests.exceptions.ConnectionError as e:
        logger.error(f"Connection error occurred while fetching `{plugin_name}`: {e}")
    except requests.exceptions.Timeout as e:
        logger.error(f"Timeout error while fetching `{plugin_name}`: {e}")
    except requests.exceptions.RequestException as e:
        logger.error(f"An error occurred while fetching `{plugin_name}`: {e}")
    return None

def get_plugin_summary(url: str) -> pd.DataFrame:
    """
    Fetches the plugin summary from the given URL and returns it as a DataFrame.
    If no summary is retrieved, an empty DataFrame is returned.

    Args:
        url (str): The API URL to fetch the plugin summary.

    Returns:
        pd.DataFrame: The plugin summary as a pandas DataFrame, or an empty DataFrame if none is retrieved.
    """
    plugin_summary = fetch_plugin(url)

    return pd.DataFrame() if not plugin_summary else plugin_summary

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
    summary_df = get_plugin_summary(API_SUMMARY_URL)

    all_plugin_data = []

    def process_plugin(plugin):
        plugin_data = plugin.copy()
        plugin_normalized_name = plugin.get('normalized_name')

        # Fetch and flatten Conda info and Manifest
        conda_info = fetch_conda(plugin_normalized_name)
        manifest_info = fetch_manifest(plugin_normalized_name)

        if conda_info:
            flatten_and_merge(plugin_data, conda_info)

        if manifest_info:
            flatten_and_merge(plugin_data, manifest_info)

        all_plugin_data.append(plugin_data)

    with ThreadPoolExecutor() as executor:
        executor.map(process_plugin, summary_df)

    return pd.DataFrame(all_plugin_data)


if __name__ == "__main__":
    # Get path to target build directory and data directory from command line arguments
    # or set default
    build_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
    data_dir = f'{build_dir}/data'

    # Create and populate a raw DataFrame with plugin data
    df_plugins = build_plugins_dataframe()

    # Clean raw DataFrame by removing columns that are mostly empty, keep columns that have at least 20 non-missing values
    df_plugins.dropna(axis=1, thresh=20, inplace=True)

    # Create a dictionary of column names and their count of values
    column_counts = {column: df_plugins[column].count() for column in df_plugins.columns}
    # Create a sorted dictionary
    sorted_column_counts = sorted(column_counts.items(), key=lambda item: item[1],  reverse=True)

    # Save the cleaned DataFrame to a CSV file
    df_plugins.to_csv(f'{data_dir}/cleaned_napari_plugins.csv')

    # Modify in place the DataFrame to keep only the columns needed for the plugin html page
    df_plugins = df_plugins[PLUGIN_PAGE_COLUMNS]

    # Convert and format 'created_at' and 'modified_at' columns
    df_plugins['created_at'] = pd.to_datetime(df_plugins['created_at'], format='mixed').dt.date
    df_plugins['modified_at'] = pd.to_datetime(df_plugins['modified_at'], format='mixed').dt.date

    # Set a temporary helper column 'home_type' by classifying the 'home' URL to a common package repository name, like 'pypi', 'github', or 'other'
    df_plugins['home_type'] = df_plugins['home'].apply(classify_url)
    # Using the 'home_type' column, create new colums for 'pypi', 'github', and 'other'
    df_plugins['home_pypi'] = df_plugins['home'].where(df_plugins['home_type'] == 'pypi', '')
    df_plugins['home_github'] = df_plugins['home'].where(df_plugins['home_type'] == 'github', '')
    df_plugins['home_other'] = df_plugins['home'].where(df_plugins['home_type'] == 'other', '')

    # Delete the temporary 'home_type' column as it is no longer needed
    df_plugins.drop('home_type', axis=1, inplace=True)

    # Perform row-wise cleaning of the DataFrame for author, license, and home_pypi fields
    for index, row in df_plugins.iterrows():
        # Check if 'author' is NaN or contains quotation marks
        if pd.isna(row['author']) or '"' in str(row['author']):
            # Update 'author' using the extracted name from 'package_metadata_author_email'
            df_plugins.at[index, 'author'] = extract_author_names(row['package_metadata_author_email'])

        if pd.isna(row['license']):
            pass 
        else:
            # Check for specific license strings to shorten the license information
            if "BSD 3-Clause" in str(row['license']):
                df_plugins.at[index, 'license'] = "BSD 3-Clause"
            elif "MIT License" in str(row['license']):
                df_plugins.at[index, 'license'] = "MIT"

        # Fill home_pypi 
        if not row['home_pypi']:
            df_plugins.at[index, 'home_pypi'] = f"https://pypi.org/project/{row['name']}"

    # Save the final DataFrame of plugin page information to a CSV file
    df_plugins.to_csv(f'{data_dir}/final_plugins.csv')
