"""Fetch napari plugin data from the NPE2 API and process it into a DataFrame.

This script fetches plugin data, flattens nested structures, and saves the cleaned data to CSV files.
"""
import re
import sys

import requests
import pandas as pd

from concurrent.futures import ThreadPoolExecutor

# --- Helper Functions ---
def extract_author_name(email) -> str:
    """
    Extracts and cleans author names from an email field.

    This function processes a string containing one or more authors, each possibly formatted as
    'Name <email>' or just an email address. It removes any surrounding quotation marks and extracts
    only the author names, returning a comma-separated string of clean names.
    """
    if not isinstance(email, str):
        return ''

    # Split the string by comma to process multiple authors
    authors = email.split(',')
    clean_authors = []

    for author in authors:
        # Use regex to find name patterns before the email
        match = re.match(r'(.*)<.*?>', author)

        if match:
            # Remove surrounding quotation marks using strip
            clean_author = match.group(1).replace('"', '').strip()
            clean_authors.append(clean_author)
        else:
            clean_authors.append(author.replace('"', '').strip())

    # Return the list of clean author names
    return ', '.join(clean_authors)

def classify_website(home_url: str) -> str:
    """
    Classify package source code home URL in a dataframe to a string identifying the package repository name.
     
    Currently, this categorizes a URL to be 'pypi', 'github', or 'other'.
    """
    if pd.notnull(home_url):
        if 'pypi.org' in home_url:
            return 'pypi'
        elif 'github.com' in home_url:
            return 'github'
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
    conda_url = f'https://npe2api.vercel.app/api/conda/{plugin_name}'
    response = requests.get(conda_url)
    if response.status_code != 200:
        print(f"Failed to fetch Conda info for {plugin_name}")
        return None

    return response.json()

def fetch_plugin(url: str):
    """ Fetches plugin summary from the given URL """
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch {url}")
        return None
    
def fetch_manifest(plugin_name: str):
    """ Fetches the manifest data for a given plugin """
    url = f'https://npe2api.vercel.app/api/manifest/{plugin_name}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch MANIFEST info for {plugin_name}")
        return None

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
    summary_url = 'https://npe2api.vercel.app/api/summary'
    plugin_summary = fetch_plugin(summary_url)

    if not plugin_summary:
        return pd.DataFrame()

    all_plugin_data = []

    def process_plugin(plugin):
        plugin_data = plugin.copy()
        plugin_name = plugin.get('name')

        # Fetch and flatten Conda info and Manifest
        conda_info = fetch_conda(plugin_name)
        manifest_info = fetch_manifest(plugin_name)

        if conda_info:
            flatten_and_merge(plugin_data, conda_info)

        if manifest_info:
            flatten_and_merge(plugin_data, manifest_info)

        all_plugin_data.append(plugin_data)

    with ThreadPoolExecutor() as executor:
        executor.map(process_plugin, plugin_summary)

    df = pd.DataFrame(all_plugin_data)
    return df


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

    # Define columns needed for the plugin html page
    plugin_page_columns = [
        'display_name',
        'version',
        'created_at',
        'modified_at',
        'name',
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
    # Modify in place the DataFrame to keep only the columns needed for the plugin html page
    df_plugins = df_plugins[plugin_page_columns]

    # Convert and format 'created_at' and 'modified_at' columns
    df_plugins['created_at'] = pd.to_datetime(df_plugins['created_at'], format='mixed').dt.date
    df_plugins['modified_at'] = pd.to_datetime(df_plugins['modified_at'], format='mixed').dt.date

    # Set a temporary helper column 'home_type' by classifying the 'home' URL to a common package repository name, like 'pypi', 'github', or 'other'
    df_plugins['home_type'] = df_plugins['home'].apply(classify_website)
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
            df_plugins.at[index, 'author'] = extract_author_name(row['package_metadata_author_email'])

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
