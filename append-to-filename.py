import os

def prepend_to_filenames(directory, prefix):
    # Loop through all files in the directory
    for filename in os.listdir(directory):
        # Construct the old file path
        old_file_path = os.path.join(directory, filename)
        
        # Check if it is a file (not a directory)
        if os.path.isfile(old_file_path):
            # Create the new filename
            new_filename = prefix + filename
            new_file_path = os.path.join(directory, new_filename)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f'Renamed: {filename} -> {new_filename}')

# Example usage
directory_path = 'path/to/your/directory'  # Replace with your directory path
prefix_string = 'polars-'  # Replace with your desired prefix
prepend_to_filenames(directory_path, prefix_string)