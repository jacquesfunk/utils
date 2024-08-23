import os
import json

def search_json_files(directory, search_string):
    found_json = False  # Flag to track if any JSON files are found
    found_match = False  # Flag to track if any match is found
    
    # List all files and directories in the specified directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if the file is a JSON file
            if file.endswith('.json'):
                found_json = True
                file_path = os.path.join(root, file)
                # Process the JSON file
                with open(file_path, 'r') as f:
                    try:
                        # Read the entire content of the file
                        file_content = f.read()
                        # Find all valid JSON substrings in the content
                        json_strings = file_content.splitlines()
                        for json_string in json_strings:
                            try:
                                data = json.loads(json_string)
                                if isinstance(data, dict):
                                    # If data is a dictionary
                                    for key in data.keys():
                                        if isinstance(data[key], str) and search_string in data[key]:
                                            print(f"Found '{search_string}' in {key} column of file: {file_path}")
                                            found_match = True
                                elif isinstance(data, list):
                                    # If data is a list
                                    for item in data:
                                        if isinstance(item, dict):
                                            for key in item.keys():
                                                if isinstance(item[key], str) and search_string in item[key]:
                                                    print(f"Found '{search_string}' in {key} column of file: {file_path}")
                                                    found_match = True
                            except json.JSONDecodeError:
                                # Skip over non-JSON parts of the file
                                pass
                    except Exception as e:
                        print(f"Error processing file: {file_path} - {e}")

    if not found_json:
        print("No JSON files in directory")
    elif not found_match:
        print("Search term not found")

# Example usage
search_directory = "."  # Current directory
search_term = "3870948"
search_json_files(search_directory, search_term)
