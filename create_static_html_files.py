from __future__ import annotations

import ast
import json
import logging
import os
import re
import sys
from string import Template

import pandas as pd
from markdown_it import MarkdownIt
from markdown_it.common.utils import escapeHtml
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import (
    PythonLexer,
    get_lexer_by_name,
)

FALLBACK_LEXER = PythonLexer()
MISSING_LEXERS = [
    "",
    "angular2",
    "bitex",
    "bibtex",
    "commandline",
    "math",
    "mermaid",
    "{important}",
    "{note}",
    "{warning}",
]

# Configure logging
logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def _highlight_code(code, lang_name, lang_attrs):
    """Highlight a block of code using Pygments.
    This is the signature markdown-it uses to call the highlight function.
    Args:
        code (str): The code to highlight.
        lang_name (str): The language of the code.
        lang_attrs (dict): Additional attributes for the code block.
            (ignored here because I don't know how to use them)
    """
    try:
        if lang_name in MISSING_LEXERS:
            # Use fallback lexer
            return highlight(code, FALLBACK_LEXER, HtmlFormatter())
        else:
            lexer = get_lexer_by_name(lang_name)
    except Exception as e:
        # Captures the case that someone introduces a lexer name
        # not available in Pygments or in our list of missing lexers
        logger.error(f"Unknown error. Using fallback lexer: {e}")
        lexer = FALLBACK_LEXER

    formatter = HtmlFormatter()
    return highlight(code, lexer, formatter)


def _code_block_plugin(md):
    """Plugin to render code blocks (with indentation) the same as fenced code blocks.
    So we can use the same highlight function for both.
    """

    def _render_code_block(tokens, idx, options, env):
        """Render a code block with indentation.

        This function was mostly just copied from the default code block renderer.
        https://github.com/executablebooks/markdown-it-py
            /blob/36a9d146af52265420de634cc2e25d1d40cfcdb7/markdown_it/renderer.py#L224
        """
        token = tokens[idx]

        return (
            "<pre"
            + md.renderer.renderAttrs(token)
            + "><code>"
            + _highlight_code(escapeHtml(token.content), "", {})
            + "</code></pre>\n"
        )

    md.renderer.rules["code_block"] = _render_code_block


md = MarkdownIt("gfm-like", {"highlight": _highlight_code}).use(_code_block_plugin)


def create_small_html(df_plugins, build_dir):
    html_content = "<html>\n<body>\n"
    for index, row in df_plugins.iterrows():
        # Fill NaN values with 'N/A' for the current row
        row = row.fillna("N/A")

        display_name = (
            row["display_name"] if row["display_name"] != "N/A" else "Unknown"
        )
        name = row["name"] if row["name"] != "N/A" else "unknown"
        normalized_name = (
            row["normalized_name"] if row["normalized_name"] != "N/A" else "unknown"
        )

        summary = row["summary"]
        authors = [row["author"]]
        release_date = row["created_at"]
        last_updated = row["modified_at"]

        plugin_type = []
        if row["contributions_readers_0_command"] != "N/A":
            plugin_type.append("reader")
        if row["contributions_writers_0_command"] != "N/A":
            plugin_type.append("writer")
        if row["contributions_widgets_0_command"] != "N/A":
            plugin_type.append("widget")
        if row["contributions_sample_data_0_command"] != "N/A":
            plugin_type.append("sample_data")
        plugin_type = ", ".join(plugin_type) if plugin_type else "N/A"

        html_content += f'<a class="col-span-2 screen-1425:col-span-3 searchResult py-sds-xl border-black border-t-2 last:border-b-2 hover:bg-hub-gray-100" data-testid="pluginSearchResult" href="./plugins/{normalized_name}.html" data-plugin-id="{index}">\n'
        html_content += '    <article class="grid gap-x-sds-xl screen-495:gap-x-12 screen-600:grid-cols-2 screen-1425:grid-cols-napari-3" data-testid="searchResult">\n'
        html_content += '        <div class="col-span-2 screen-495:col-span-1 screen-1425:col-span-2 flex flex-col justify-between">\n'
        html_content += f'            <div>\n                <h3 class="font-bold text-lg" data-testid="searchResultDisplayName">{display_name}</h3>\n'
        html_content += f'                <span class="mt-sds-m screen-495:mt-3 text-[0.6875rem]" data-testid="searchResultName">{name}</span>\n'
        html_content += f'                <p class="mt-3" data-testid="searchResultSummary">{summary}</p>\n            </div>\n'
        html_content += '            <ul class="mt-3 text-xs">\n'
        for author in authors:
            html_content += f'                <li class="my-sds-s font-bold PluginSearchResult_linkItem__Vvs7H" data-testid="searchResultAuthor">{author}</li>\n'
        html_content += "            </ul>\n        </div>\n"
        html_content += '        <ul class="mt-sds-l screen-600:m-0 space-y-1 text-sm col-span-2 screen-495:col-span-1">\n'
        html_content += f'            <li class="grid grid-cols-[auto,1fr]" data-label="First released" data-testid="searchResultMetadata" data-value="{release_date}">\n'
        html_content += f'                <h4 class="inline whitespace-nowrap">First released<!-- -->: </h4>\n                <span class="ml-sds-xxs font-bold">{release_date}</span>\n            </li>\n'
        html_content += f'            <li class="grid grid-cols-[auto,1fr]" data-label="Last updated" data-testid="searchResultMetadata" data-value="{last_updated}">\n'
        html_content += f'                <h4 class="inline whitespace-nowrap">Last updated<!-- -->: </h4>\n                <span class="ml-sds-xxs font-bold">{last_updated}</span>\n            </li>\n'
        html_content += f'            <li class="grid grid-cols-[auto,1fr]" data-label="Plugin type" data-testid="searchResultMetadata" data-value="{plugin_type}">\n'
        html_content += f'                <h4 class="inline whitespace-nowrap">Plugin type<!-- -->: </h4><span class="ml-sds-xxs font-bold">{plugin_type}</span>\n            </li>\n        </ul>\n'
        html_content += '        <div class="mt-sds-xl text-xs flex flex-col gap-sds-s col-span-2 screen-1425:col-span-3">\n        </div>\n    </article>\n</a>\n'

    html_content += "</body>\n</html>"

    with open(f"{build_dir}/plugins_list.html", "w") as file:
        file.write(html_content)


def generate_plugin_types_html(row):
    plugin_types_html = ""

    # Determine plugin type based on non-NA status of certain columns
    plugin_type = []
    if not pd.isna(row.get("contributions_readers_0_command")):
        plugin_type.append("reader")
    if not pd.isna(row.get("contributions_writers_0_command")):
        plugin_type.append("writer")
    if not pd.isna(row.get("contributions_widgets_0_command")):
        plugin_type.append("widget")
    if not pd.isna(row.get("contributions_sample_data_0_command")):
        plugin_type.append("sample_data")

    if plugin_type:
        plugin_types_html = '<ul class="MetadataList_list__3DlqI list-none text-sm leading-normal inline space-y-sds-s MetadataList_inline__jHQLo">'
        for pt in plugin_type:
            plugin_types_html += f'<li class="MetadataList_textItem__KKmMN"><a class="MetadataList_textItem__KKmMN underline" href="../index.html?pluginType={pt}">{pt.capitalize()}</a></li>'
        plugin_types_html += "</ul>"

    return plugin_types_html


def generate_open_extensions_html(row):
    open_extensions_html = ""

    if not pd.isna(row.get("contributions_readers_0_filename_patterns")) and row.get(
        "contributions_readers_0_filename_patterns"
    ):
        # We use ast.literal_eval to safely evaluate the string representation
        # of the list; this is safer than using eval.
        filename_patterns = ast.literal_eval(
            row.get("contributions_readers_0_filename_patterns")
        )

        if filename_patterns:
            open_extensions_html = '<ul class="MetadataList_list__3DlqI list-none text-sm leading-normal inline space-y-sds-s MetadataList_inline__jHQLo">'
            for pattern in filename_patterns:
                open_extensions_html += f'<li class="MetadataList_textItem__KKmMN"><a class="MetadataList_textItem__KKmMN underline" href="../index.html?readerFileExtensions={pattern}">{pattern}</a></li>'
            open_extensions_html += "</ul>"

    return open_extensions_html


def generate_save_extensions_html(row):
    save_extensions_html = ""

    # Gather file extensions from both columns
    file_extensions = []
    if not pd.isna(row.get("contributions_writers_0_filename_extensions")):
        file_extensions += ast.literal_eval(
            row.get("contributions_writers_0_filename_extensions")
        )

    if not pd.isna(row.get("contributions_writers_1_filename_extensions")):
        file_extensions += ast.literal_eval(
            row.get("contributions_writers_1_filename_extensions")
        )

    if file_extensions:
        save_extensions_html = '<ul class="MetadataList_list__3DlqI list-none text-sm leading-normal inline space-y-sds-s MetadataList_inline__jHQLo">'
        for ext in file_extensions:
            save_extensions_html += f'<li class="MetadataList_textItem__KKmMN"><a class="MetadataList_textItem__KKmMN underline" href="../index.html?writerFileExtensions={ext}">{ext}</a></li>'
        save_extensions_html += "</ul>"

    return save_extensions_html


def generate_requirements_html(row):
    requirements_html = ""

    if not pd.isna(row.get("package_metadata_requires_dist")) and row.get(
        "package_metadata_requires_dist"
    ):
        requirements = ast.literal_eval(row.get("package_metadata_requires_dist"))

        if requirements:
            requirements_html = (
                '<ul class="MetadataList_list__3DlqI list-none text-sm leading-normal">'
            )
            for req in requirements:
                requirements_html += (
                    f'<li class="MetadataList_textItem__KKmMN">{req}</li>'
                )
            requirements_html += "</ul>"

    return requirements_html


def parse_version_specifier(specifier, default_min_version="3.6"):
    # Parse version specifiers to get the min and max version
    min_version = default_min_version
    max_version = None
    specifiers = specifier.split(",")

    for spec in specifiers:
        if ">=" in spec:
            min_version = spec.split(">=")[1]
        elif "<=" in spec:
            max_version = spec.split("<=")[1]
        elif "<" in spec:
            # If strictly less than, consider the next lower minor version as the max
            max_version = str(float(spec.split("<")[1]) - 0.1)

    return min_version, max_version


def generate_python_versions_html(
    row, max_supported_version="3.11", default_min_version="3.6"
):
    python_versions_html = ""

    if not pd.isna(row.get("package_metadata_requires_python")) and row.get(
        "package_metadata_requires_python"
    ):
        requirement = row.get("package_metadata_requires_python")
        min_version, max_version = parse_version_specifier(requirement)

        # Use the given maximum version if no upper bound is specified
        max_version = max_version if max_version else max_supported_version
        min_minor = (
            int(min_version.split(".")[1])
            if min_version
            else int(default_min_version.split(".")[1])
        )
        max_minor = int(max_version.split(".")[1])

        # Generate a list of versions from min_version to max_version
        versions = [f"3.{v}" for v in range(min_minor, max_minor + 1)]

        # Construct HTML list items for each version
        python_versions_html = '<ul class="MetadataList_list__3DlqI list-none text-sm leading-normal inline space-y-sds-s MetadataList_inline__jHQLo">'
        for version in versions:
            python_versions_html += f'<li class="MetadataList_textItem__KKmMN"><a class="MetadataList_textItem__KKmMN underline" href="../index.html?python={version}">{version}</a></li>'
        python_versions_html += "</ul>"

    return python_versions_html


def get_os_html(package_metadata_classifier):
    # Default message if no operating system info is found
    default_os_html = (
        '<ul class="MetadataList_list__3DlqI list-none text-sm leading-normal">'
        '<li class="flex justify-between items-center"><span '
        'class="text-napari-gray font-normal lowercase">Information not '
        "submitted</span></li>"
        "</ul>"
    )

    # Split the package_metadata_classifier into a list for easier searching
    classifier_items = package_metadata_classifier.strip("]").split(",")

    # Compose html from classifier or use the default
    os_html = default_os_html
    for item in classifier_items:
        if "Operating System ::" in item:
            os = item.split("Operating System :: ")[1].strip("' \"")
            os_html = (
                '<ul class="MetadataList_list__3DlqI list-none text-sm leading-normal">'
                f'<li class="MetadataList_textItem__KKmMN">{os}</li>'
                "</ul>"
            )
            break
    return os_html


def extract_github_info(url):
    match = re.search(r"github\.com/([^/]+)/([^/]+)", url)
    if match:
        user, repo = match.group(1), match.group(2).rstrip(".git")
        return user, repo
    return None, None


def generate_home_html(plugin_name, home_pypi, home_github, home_other):
    # Start with the PyPI link, which is always present
    html_content = f'''
   <div class="flex items-center" style="gap: 20px; ; align-items: center;"">
        <a class="underline flex" href="{home_pypi}" rel="noreferrer" target="_blank">
        <img src="../static/images/PyPI_logo.svg.png" alt="PyPI" style="height: 42px;" /><span style="padding-top: 10px; padding-left: 10px;">{plugin_name}</span>
    </a>
    '''

    # Conditionally add the GitHub link
    if home_github and str(home_github).lower() not in ["n/a", "none", "nan", ""]:
        github_user_repo = ""
        user, repo = extract_github_info(home_github)
        if user is not None and repo is not None:
            github_user_repo = "/".join([user, repo])
        html_content += f'''
        <a class="underline flex" href="{home_github}" rel="noreferrer" target="_blank">
            <img src="../static/images/GitHub_Invertocat_Logo.svg.png" alt="GitHub" style="height: 42px;" /><span style="padding-top: 10px; padding-left: 10px;">{github_user_repo}</span>
        </a>
        '''

    # Conditionally add the Other link
    if home_other and str(home_other).lower() not in ["n/a", "none", "nan", ""]:
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
    html_content += "</div>"

    return html_content


def generate_plugin_html(row, template, plugin_dir):
    # Convert Markdown in 'package_metadata_description' to HTML
    if not pd.isna(row["package_metadata_description"]):
        # Remove the first Markdown header
        # Split the content into lines, drop the first line if it's a header, and rejoin
        lines = row["package_metadata_description"].split("\n")
        if lines and lines[0].startswith("#"):
            no_first_header = "\n".join(lines[1:])
        else:
            no_first_header = "\n".join(lines)

        html_description = md.render(no_first_header)
    else:
        html_description = "Not available"

    plugin_types_html = generate_plugin_types_html(row)
    openfile_types_html = generate_open_extensions_html(row)
    savefile_types_html = generate_save_extensions_html(row)
    requirements_html = generate_requirements_html(row)
    python_versions_html = generate_python_versions_html(row)
    home_html = generate_home_html(
        row["name"], row["home_pypi"], row["home_github"], row["home_other"]
    )

    # Replace NaN with 'Not available' and ensure all data are strings, except Markdown field
    row_data = {
        col: (str(row[col]) if not pd.isna(row[col]) else "Not available")
        for col in row.index
    }

    row_data["open_extension"] = openfile_types_html
    row_data["save_extension"] = savefile_types_html
    row_data["plugin_types"] = plugin_types_html
    row_data["requirements"] = requirements_html
    row_data["python_versions"] = python_versions_html
    row_data["os"] = get_os_html(row["package_metadata_classifier"])
    row_data["package_metadata_description"] = html_description
    row_data["home_link"] = home_html

    # Create a new Template with the row data
    filled_template = Template(template).safe_substitute(row_data)

    # Save the HTML file for each plugin
    os.makedirs(plugin_dir, exist_ok=True)
    with open(f"{plugin_dir}/{row['html_filename']}", "w") as file:
        file.write(filled_template)


if __name__ == "__main__":
    build_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    data_dir = f"{build_dir}/data"
    static_dir = f"{build_dir}/static"
    plugin_dir = f"{build_dir}/plugins"
    template_dir = f"{build_dir}/templates"

    # Load your DataFrame
    df_plugins = pd.read_csv(f"{data_dir}/final_plugins.csv")

    # Sort the DataFrame by 'modified_at' in descending order
    df_plugins = df_plugins.sort_values(by="modified_at", ascending=False)

    # Reset index to ensure it starts from 0 and is continuous after sorting
    df_plugins.reset_index(drop=True, inplace=True)
    df_plugins["plugin_id"] = df_plugins.index
    df_plugins["html_filename"] = df_plugins["normalized_name"].apply(
        lambda x: f"{x}.html"
    )

    # Generate plugins_manifest.json
    plugins_manifest = df_plugins[["plugin_id", "html_filename"]].to_dict(
        orient="records"
    )
    manifest_path = f"{build_dir}/plugins_manifest.json"
    with open(manifest_path, "w") as f:
        json.dump(plugins_manifest, f, indent=4)

    create_small_html(df_plugins, build_dir)

    # Read the list of available plugins
    with open(f"{build_dir}/plugins_list.html") as file:
        element_html = file.read()

    # Read the individual plugin HTML template
    with open(f"{template_dir}/each_plugin_template.html") as file:
        template = file.read()

    # Apply the function to each row in the DataFrame
    df_plugins.apply(
        lambda row: generate_plugin_html(row, template, plugin_dir), axis=1
    )
