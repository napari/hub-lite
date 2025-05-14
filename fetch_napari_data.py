import sys
import requests
import json
import os
import pandas as pd
import re

def fetch_conda(plugin_name):
    """ Fetches Conda info and creates an HTML file for it """
    conda_url = f'https://npe2api.vercel.app/api/conda/{plugin_name}'
    response = requests.get(conda_url)
    if response.status_code != 200:
        print(f"Failed to fetch Conda info for {plugin_name}")
        return None

    return response.json()

def fetch_plugin(url):
    """ Fetches plugin summary from the given URL """
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch {url}")
        return None
    
def fetch_manifest(plugin_name):
    """ Fetches the manifest data for a given plugin """
    url = f'https://npe2api.vercel.app/api/manifest/{plugin_name}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch MANIFEST info for {plugin_name}")
        return None

def flatten_and_merge(original, additional, parent_key=''):
    """ Flattens an additional nested dictionary and merges it into the original dictionary """
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


def build_plugins_dataframe():
    summary_url = 'https://npe2api.vercel.app/api/summary'
    plugin_summary = fetch_plugin(summary_url)

    if not plugin_summary:
        return pd.DataFrame()

    all_plugin_data = []

    for plugin in plugin_summary:
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
        #print(pd.DataFrame(all_plugin_data))

    df = pd.DataFrame(all_plugin_data)
    return df

# Define the function to extract the author's name from the email field
def extract_author_name(email):

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

# Function to classify the 'home' column
def classify_website(home_url):
    if pd.notnull(home_url):
        if 'pypi.org' in home_url:
            return 'pypi'
        elif 'github.com' in home_url:
            return 'github'
    return 'other'


if __name__ == "__main__":
    build_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
    data_dir = f'{build_dir}/data'

    df_plugins = build_plugins_dataframe()

    # Drop columns where all elements are NaN
    #df_plugins.dropna(axis=1, how='all', inplace=True)

    # Drop columns where less than 20 non-NaN counts
    df_plugins.dropna(axis=1, thresh=20, inplace=True)

    # Create a dictionary of column names and their non-NaN counts
    column_counts = {column: df_plugins[column].count() for column in df_plugins.columns}

    # Sort the dictionary by counts and print
    for column, count in sorted(column_counts.items(), key=lambda item: item[1],  reverse=True):
        print(column, count)

    # Save the cleaned DataFrame to a CSV file
    df_plugins.to_csv(f'{data_dir}/cleaned_napari_plugins.csv')

    Plugin_page_columns = ['display_name', 'version', 'created_at','modified_at', 'name',
                        'author',  #'package_metadata_author', 
                        'package_metadata_author_email',
                        'license', #'package_metadata_license', 
                        'home', #'home_page', 'package_metadata_home_page', 
                        'summary', # 'package_metadata_summary'
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
                            'contributions_writers_1_filename_extensions']

    df_plugins = df_plugins[Plugin_page_columns]

    # Convert and format 'created_at' and 'modified_at' columns
    df_plugins['created_at'] = pd.to_datetime(df_plugins['created_at'], format='mixed').dt.date
    df_plugins['modified_at'] = pd.to_datetime(df_plugins['modified_at'], format='mixed').dt.date

    # Apply the function to the 'home' column to classify the websites
    df_plugins['home_type'] = df_plugins['home'].apply(classify_website)

    # Create the new columns based on classification
    df_plugins['home_pypi'] = df_plugins['home'].where(df_plugins['home_type'] == 'pypi', '')
    df_plugins['home_github'] = df_plugins['home'].where(df_plugins['home_type'] == 'github', '')
    df_plugins['home_other'] = df_plugins['home'].where(df_plugins['home_type'] == 'other', '')

    # Delete 'home_type' column as it is no longer needed
    df_plugins.drop('home_type', axis=1, inplace=True)


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

    df_plugins.to_csv(f'{data_dir}/final_plugins.csv')