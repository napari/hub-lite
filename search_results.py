from flask import Flask, render_template, request, send_file
import pandas as pd
import os

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

    with open('flask_plugins_list.html', 'w') as file:
        file.write(html_content)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('flask_index.html')


from flask import send_from_directory

@app.route('/plugins/<path:filename>')
def serve_plugin(filename):
    return send_from_directory('static/plugins', filename)

@app.route('/search', methods=['POST'])
def search():
    search_word = request.form['query']
    
    # Load your DataFrame
    df = pd.read_csv('./data/final_plugins.csv')

    # Sort the DataFrame by 'modified_at' in descending order
    df = df.sort_values(by='modified_at', ascending=False)

    # Filter the DataFrame based on the search query
    filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search_word, case=False, na=False).any(), axis=1)]
    
    # Check if there are matches
    if not filtered_df.empty:

        create_small_html(filtered_df)

        # Read the target HTML file
        with open('./templates/flask_template.html', 'r') as file:
            target_html = file.read()

        # The number you want to insert
        number_to_insert = len(filtered_df)  # This can be dynamically set

        # Find the first insertion point in the target HTML for the number
        insertion_point_number = target_html.find('<!-- insert number here -->')

        # Check if the first insertion point is found
        if insertion_point_number != -1:
            # Insert the number
            target_html = target_html[:insertion_point_number] + str(number_to_insert) + target_html[insertion_point_number:]
        else:
            print("Number insertion point not found in the target HTML file.")

        # Read the contents of element.html
        with open('flask_plugins_list.html', 'r') as file:
            element_html = file.read()

        os.remove('flask_plugins_list.html')

        # Find the insertion point in the target HTML
        insertion_point = target_html.find('<!-- insert temp.html -->')

        # Check if the insertion point is found
        if insertion_point != -1:
            # Insert the element.html content
            modified_html = target_html[:insertion_point] + element_html + target_html[insertion_point:]

            # Save the modified HTML back to target.html or a new file
            file_path = 'search_results.html'
            with open(file_path, 'w') as file:
                file.write(modified_html)   
        else:
            print("Insertion point not found in the target HTML file.")
        
        # Serve the generated HTML file
        return send_file(file_path, as_attachment=False)

    else:
        # Return a simple message or render a template if no results
        return "No matching results found."


if __name__ == '__main__':
    app.run(debug=True)