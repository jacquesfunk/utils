import os
import shutil

# Define folder paths
source_dir = 'C:/Users/YourName/Downloads'
dest_dirs = {
    'Documents': 'C:/Users/YourName/Documents',
    'Images': 'C:/Users/YourName/Pictures',
}

# Map file extensions to their respective folder
file_type_mapping = {
    '.pdf': 'Documents',
    '.docx': 'Documents',
    '.jpg': 'Images',
    '.png': 'Images',
}

# Organize files
for filename in os.listdir(source_dir):
    file_extension = os.path.splitext(filename)[1]
    if file_extension in file_type_mapping:
        folder_name = file_type_mapping[file_extension]
        destination = dest_dirs[folder_name]
        shutil.move(os.path.join(source_dir, filename), destination)