import os
import re

# Define the pattern you want to match
# match filenames containing string: pattern = re.compile(r'data')
# match filenames starting with string: pattern = re.compile(r'^report')
# match filenames ending with string: pattern = re.compile(r'_2023$')
pattern = re.compile(
    r"^cadence_20240807"
)  # Replace 'your_pattern_here' with your actual pattern

# Get the current directory
current_directory = os.getcwd()

# Loop through the files in the current directory
for filename in os.listdir(current_directory):
    if pattern.search(filename) and not filename.endswith('.csv'):
        new_filename = filename + '.csv'
        os.rename(os.path.join(current_directory, filename), os.path.join(current_directory, new_filename))
        print(f'Renamed: {filename} to {new_filename}')
