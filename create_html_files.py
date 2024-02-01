import requests
import json
import os
import pandas as pd
import re

from string import Template
import markdown
from markdown.extensions.toc import TocExtension


def create_small_html(df_plugins):
    html_content = '<html>\n<body>\n'
    for _, row in df_plugins.iterrows():
        display_name = row.get('display_name', 'Unknown')
        name = row.get('name', 'unknown')
        plugin_name = row.get('name', 'unknown').replace("-", "_")

        print(display_name, name, plugin_name)

        summary = row.get("summary", "No summary")
        authors = [row.get("author", "Anonymous")]  # Assuming single author in 'author' column
        release_date = row.get("created_at", "N/A")
        last_updated = row.get("modified_at", "N/A")
        # Installs data not available in df_plugins, so you might want to omit this or use a placeholder
        #installs = "N/A"
        # Determine plugin type based on non-NA status of certain columns
        plugin_type = []
        if not pd.isna(row.get('contributions_readers_0_command')):
            plugin_type.append("reader")
        if not pd.isna(row.get('contributions_writers_0_command')):
            plugin_type.append("writer")
        if not pd.isna(row.get('contributions_widgets_0_command')):
            plugin_type.append("widget")
        if not pd.isna(row.get('contributions_sample_data_0_command')):
            plugin_type.append("sample_data")
        plugin_type = ', '.join(plugin_type) if plugin_type else "N/A"

        html_content += f'<a class="col-span-2 screen-1425:col-span-3 searchResult py-sds-xl border-black border-t-2 last:border-b-2 hover:bg-hub-gray-100" data-testid="pluginSearchResult" href="./plugins/{name}.html">\n'
        html_content += '    <article class="grid gap-x-sds-xl screen-495:gap-x-12 screen-600:grid-cols-2 screen-1425:grid-cols-napari-3" data-testid="searchResult">\n'
        html_content += '        <div class="col-span-2 screen-495:col-span-1 screen-1425:col-span-2 flex flex-col justify-between">\n'
        html_content += f'            <div>\n                <h3 class="font-bold text-lg" data-testid="searchResultDisplayName">{display_name}</h3>\n'
        html_content += f'                <span class="mt-sds-m screen-495:mt-3 text-[0.6875rem]" data-testid="searchResultName">{name}</span>\n'
        html_content += f'                <p class="mt-3" data-testid="searchResultSummary">{summary}</p>\n            </div>\n'
        html_content += '            <ul class="mt-3 text-xs">\n'
        for author in authors:
            html_content += f'                <li class="my-sds-s font-bold PluginSearchResult_linkItem__Vvs7H" data-testid="searchResultAuthor">{author}</li>\n'
        html_content += '            </ul>\n        </div>\n'
        html_content += '        <ul class="mt-sds-l screen-600:m-0 space-y-1 text-sm col-span-2 screen-495:col-span-1">\n'
        html_content += f'            <li class="grid grid-cols-[auto,1fr]" data-label="First released" data-testid="searchResultMetadata" data-value="{release_date}">\n'
        html_content += f'                <h4 class="inline whitespace-nowrap">First released<!-- -->: </h4>\n                <span class="ml-sds-xxs font-bold">{release_date}</span>\n            </li>\n'
        html_content += f'            <li class="grid grid-cols-[auto,1fr]" data-label="Last updated" data-testid="searchResultMetadata" data-value="{last_updated}">\n'
        html_content += f'                <h4 class="inline whitespace-nowrap">Last updated<!-- -->: </h4>\n                <span class="ml-sds-xxs font-bold">{last_updated}</span>\n            </li>\n'
#        html_content += f'            <li class="grid grid-cols-[auto,1fr]" data-label="Installs" data-testid="searchResultMetadata" data-value="{installs}">\n'
#        html_content += f'                <h4 class="inline whitespace-nowrap">Installs<!-- -->: </h4><span class="ml-sds-xxs font-bold">{installs}</span>\n            </li>\n'
        html_content += f'            <li class="grid grid-cols-[auto,1fr]" data-label="Plugin type" data-testid="searchResultMetadata" data-value="{plugin_type}">\n'
        html_content += f'                <h4 class="inline whitespace-nowrap">Plugin type<!-- -->: </h4><span class="ml-sds-xxs font-bold">{plugin_type}</span>\n            </li>\n        </ul>\n'
        html_content += '        <div class="mt-sds-xl text-xs flex flex-col gap-sds-s col-span-2 screen-1425:col-span-3">\n        </div>\n    </article>\n</a>\n'

    html_content += '</body>\n</html>'

    with open('temp.html', 'w') as file:
        file.write(html_content)


def generate_plugin_types_html(row):
    plugin_types_html = ''

    # Determine plugin type based on non-NA status of certain columns
    plugin_type = []
    if not pd.isna(row.get('contributions_readers_0_command')):
        plugin_type.append("reader")
    if not pd.isna(row.get('contributions_writers_0_command')):
        plugin_type.append("writer")
    if not pd.isna(row.get('contributions_widgets_0_command')):
        plugin_type.append("widget")
    if not pd.isna(row.get('contributions_sample_data_0_command')):
        plugin_type.append("sample_data")

    if plugin_type:  # Check if the list is not empty
        plugin_types_html = '<ul class="MetadataList_list__3DlqI list-none text-sm leading-normal inline space-y-sds-s MetadataList_inline__jHQLo">'
        for pt in plugin_type:
            plugin_types_html += f'<li class="MetadataList_textItem__KKmMN"><a class="MetadataList_textItem__KKmMN underline" href="/plugins?pluginType={pt}">{pt.capitalize()}</a></li>'
        plugin_types_html += '</ul>'

    return plugin_types_html

def generate_open_extensions_html(row):
    open_extensions_html = ''

    # Check if 'contributions_readers_0_filename_patterns' is not NA and not empty
    if not pd.isna(row.get('contributions_readers_0_filename_patterns')) and row.get('contributions_readers_0_filename_patterns'):
        # Assuming the data is stored as a string representation of a list
        filename_patterns = eval(row.get('contributions_readers_0_filename_patterns'))

        if filename_patterns:  # Check if the list is not empty
            open_extensions_html = '<ul class="MetadataList_list__3DlqI list-none text-sm leading-normal inline space-y-sds-s MetadataList_inline__jHQLo">'
            for pattern in filename_patterns:
                open_extensions_html += f'<li class="MetadataList_textItem__KKmMN"><a class="MetadataList_textItem__KKmMN underline" href="/plugins?readerFileExtensions={pattern}">{pattern}</a></li>'
            open_extensions_html += '</ul>'

    return open_extensions_html

def generate_save_extensions_html(row):
    save_extensions_html = ''

    # Gather file extensions from both columns
    file_extensions = []
    if not pd.isna(row.get('contributions_writers_0_filename_extensions')):
        file_extensions += eval(row.get('contributions_writers_0_filename_extensions'))

    if not pd.isna(row.get('contributions_writers_1_filename_extensions')):
        file_extensions += eval(row.get('contributions_writers_1_filename_extensions'))

    if file_extensions:  # Check if the list is not empty
        save_extensions_html = '<ul class="MetadataList_list__3DlqI list-none text-sm leading-normal inline space-y-sds-s MetadataList_inline__jHQLo">'
        for ext in file_extensions:
            save_extensions_html += f'<li class="MetadataList_textItem__KKmMN"><a class="MetadataList_textItem__KKmMN underline" href="/plugins?writerFileExtensions={ext}">{ext}</a></li>'
        save_extensions_html += '</ul>'

    return save_extensions_html

def generate_requirements_html(row):
    requirements_html = ''

    # Check if 'package_metadata_requires_dist' is not NA and not empty
    if not pd.isna(row.get('package_metadata_requires_dist')) and row.get('package_metadata_requires_dist'):
        # Convert the string representation of the list to an actual list
        requirements = eval(row.get('package_metadata_requires_dist'))

        if requirements:  # Check if the list is not empty
            requirements_html = '<ul class="MetadataList_list__3DlqI list-none text-sm leading-normal">'
            for req in requirements:
                requirements_html += f'<li class="MetadataList_textItem__KKmMN">{req}</li>'
            requirements_html += '</ul>'

    return requirements_html
def parse_version_specifier(specifier, default_min_version='3.6'):
    # Parse version specifiers to get the min and max version
    min_version = default_min_version  # Set a default min version
    max_version = None
    specifiers = specifier.split(',')

    for spec in specifiers:
        if '>=' in spec:
            min_version = spec.split('>=')[1]
        elif '<=' in spec:
            max_version = spec.split('<=')[1]
        elif '<' in spec:
            # If strictly less than, consider the next lower minor version as the max
            max_version = str(float(spec.split('<')[1]) - 0.1)
    
    return min_version, max_version

def generate_python_versions_html(row, max_supported_version='3.11'):
    python_versions_html = ''

    # Check if 'package_metadata_requires_python' is not NA and not empty
    if not pd.isna(row.get('package_metadata_requires_python')) and row.get('package_metadata_requires_python'):
        requirement = row.get('package_metadata_requires_python')
        min_version, max_version = parse_version_specifier(requirement)

        # Use the given maximum version if no upper bound is specified
        max_version = max_version if max_version else max_supported_version
        min_minor = int(min_version.split('.')[1]) if min_version else int(default_min_version.split('.')[1])
        max_minor = int(max_version.split('.')[1])

        # Generate a list of versions from min_version to max_version
        versions = [f'3.{v}' for v in range(min_minor, max_minor + 1)]
        
        # Construct HTML list items for each version
        python_versions_html = '<ul class="MetadataList_list__3DlqI list-none text-sm leading-normal inline space-y-sds-s MetadataList_inline__jHQLo">'
        for version in versions:
            python_versions_html += f'<li class="MetadataList_textItem__KKmMN"><a class="MetadataList_textItem__KKmMN underline" href="/plugins?python={version}">{version}</a></li>'
        python_versions_html += '</ul>'

    return python_versions_html

def get_os_html(classifiers):
    # Default message if no operating system info is found
    default_os_html = '<ul class="MetadataList_list__3DlqI list-none text-sm leading-normal">' \
                      '<li class="flex justify-between items-center"><span ' \
                      'class="text-napari-gray font-normal lowercase">Information not ' \
                      'submitted</span></li>' \
                      '</ul>'
    
    # # Search for the operating system classifier
    # os_classifier = next((c for c in classifiers if c.startswith('Operating System ::')), None)
    # if os_classifier:
    #     operating_system = os_classifier.split('::')[-1].strip()
    #     os_html = '<ul class="MetadataList_list__3DlqI list-none text-sm leading-normal">' \
    #               f'<li class="MetadataList_textItem__KKmMN">{operating_system}</li>' \
    #               '</ul>'
    # else:
    #     os_html = default_os_html
    
    return default_os_html

def generate_home_html(home_pypi, home_github, home_other):

    # Start with the PyPI link, which is always present
    html_content = f'''
   <div class="flex items-center" style="gap: 10px; ; align-items: center;"">
        <a href="{home_pypi}" rel="noreferrer" target="_blank">
        <img src="../static/images/PyPI_logo.svg.png" alt="PyPI" style="height: 42px;" /> 
    </a>
    '''

    # Conditionally add the GitHub link
    if home_github and str(home_github).lower() not in ['n/a', 'none', 'nan', '']:
        html_content += f'''
        <a href="{home_github}" rel="noreferrer" target="_blank">
            <img src="../static/images/GitHub_Invertocat_Logo.svg.png" alt="GitHub" style="height: 42px;" />
        </a>
        '''

    # Conditionally add the Other link
    if home_other and str(home_other).lower() not in ['n/a', 'none', 'nan', '']:
        html_content += f'''
        <a href="{home_other}" rel="noreferrer" target="_blank">
        <svg width="21" height="21" viewBox="0 0 21 21" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="10.8331" cy="10.0835" r="9.33333" stroke="#000" stroke-width="1.33333"></circle>
            <path
                d="M15.4998 10.0835C15.4998 12.7576 14.9202 15.1456 14.0161 16.8408C13.0967 18.5648 11.9398 19.4168 10.8331 19.4168C9.7264 19.4168 8.56951 18.5648 7.65009 16.8408C6.74594 15.1456 6.16642 12.7576 6.16642 10.0835C6.16642 7.40935 6.74594 5.02142 7.65009 3.32615C8.56951 1.60224 9.7264 0.750163 10.8331 0.750163C11.9398 0.750163 13.0967 1.60224 14.0161 3.32615C14.9202 5.02142 15.4998 7.40935 15.4998 10.0835Z"
                stroke="#000" stroke-width="1.33333"></path>
            <path d="M10.8331 0.270996V19.896" stroke="#000" stroke-width="1.33333"></path>
            <path d="M1.02063 10.0835L20.6456 10.0835" stroke="#000" stroke-width="1.33333"></path>
        </svg>
        </a>
        '''

    # Close the div tag
    html_content += '</div>'

    return html_content

def generate_plugin_html(row, template):


    # Convert Markdown in 'package_metadata_description' to HTML
    if not pd.isna(row['package_metadata_description']):
        # Remove only the first Markdown header
        # We split the content into lines, drop the first line if it's a header, and rejoin
        lines = row['package_metadata_description'].split('\n')
        if lines and lines[0].startswith('#'):
            no_first_header = '\n'.join(lines[1:])
        else:
            no_first_header = '\n'.join(lines)
        
        html_description = markdown.markdown(no_first_header)

        # Add the CSS styles for the code block
        html_description = f'''
        <style>
        pre {{
   background-color: #f6f8fa;
    border: 1px solid #e1e4e8;
    border-radius: 6px;
    padding: 16px;
    overflow: auto;
    font-size: 85%;
    line-height: 1.45;
    font-family: SFMono-Regular, Consolas, "Liberation Mono", Menlo, Courier, monospace;
}}

        code {{
    padding: 0.2em 0.4em;
    margin: 0;
    font-size: 85%;
    background-color: rgba(27,31,35,0.05);
    border-radius: 6px;
    font-family: SFMono-Regular, Consolas, "Liberation Mono", Menlo, Courier, monospace;
}}
/* Remove margin and padding from the last child to avoid extra space */
pre > code:last-child {{
    margin-bottom: 0;
    padding-bottom: 0;
}}
        </style>
        {html_description}
        '''

    else:
        html_description = 'Not available'

    
    plugin_types_html = generate_plugin_types_html(row)
    openfile_types_html = generate_open_extensions_html(row)
    savefile_types_html = generate_save_extensions_html(row)
    requirements_html = generate_requirements_html(row)
    python_versions_html = generate_python_versions_html(row)
    home_html = generate_home_html(row['home_pypi'],row['home_github'], row['home_other'])



    # Replace NaN with 'Not available' and ensure all data are strings, except Markdown field
    row_data = {col: (str(row[col]) if not pd.isna(row[col]) else 'Not available') for col in row.index}

    row_data['open_extension'] = openfile_types_html  
    row_data['save_extension'] = savefile_types_html 
    row_data['plugin_types'] = plugin_types_html  
    row_data['requirements'] = requirements_html
    row_data['python_versions'] = python_versions_html
    row_data['os'] = get_os_html(row)
    row_data['package_metadata_description'] = html_description  
    row_data['home_link'] = home_html 

    # Create a new Template with the row data
    filled_template = Template(template).safe_substitute(row_data)

    # Save the HTML file for each plugin
    plugin_dir = './static/plugins/'
    os.makedirs(plugin_dir, exist_ok= True)
    file_name = f"{row['name']}.html"
    with open(plugin_dir + file_name, 'w') as file:
        file.write(filled_template)


# Load your DataFrame
df_plugins = pd.read_csv('./data/final_plugins.csv')

# Sort the DataFrame by 'modified_at' in descending order
df_plugins = df_plugins.sort_values(by='modified_at', ascending=False)

create_small_html(df_plugins)

# Read the target HTML file
with open('./templates/all_plugins_template.html', 'r') as file:
    target_html = file.read()

# The number you want to insert
number_to_insert = len(df_plugins)  # This can be dynamically set

# Find the first insertion point in the target HTML for the number
insertion_point_number = target_html.find('<!-- insert number here -->')

# Check if the first insertion point is found
if insertion_point_number != -1:
    # Insert the number
    target_html = target_html[:insertion_point_number] + str(number_to_insert) + target_html[insertion_point_number:]
else:
    print("Number insertion point not found in the target HTML file.")

# Read the contents of element.html
with open('temp.html', 'r') as file:
    element_html = file.read()

# Find the insertion point in the target HTML
insertion_point = target_html.find('<!-- insert temp.html -->')

# delete temp.html
os.remove('temp.html')

# Check if the insertion point is found
if insertion_point != -1:
    # Insert the element.html content
    modified_html = target_html[:insertion_point] + element_html + target_html[insertion_point:]
    # Save the modified HTML back to target.html or a new file
    with open('./index.html', 'w') as file:
        file.write(modified_html)
else:
    print("Insertion point not found in the target HTML file.")


# Read the individual plugin HTML template
with open('./templates/each_plugin_template.html', 'r') as file:
    template = file.read()

# Apply the function to each row in the DataFrame
df_plugins.apply(lambda row: generate_plugin_html(row, template), axis=1)


# Read the individual plugin HTML template
with open('./templates/search_each_plugin_template.html', 'r') as file:
    search_template = file.read()

# Apply the function to each row in the DataFrame
df_plugins.apply(lambda row: generate_plugin_html(row, search_template), axis=1)