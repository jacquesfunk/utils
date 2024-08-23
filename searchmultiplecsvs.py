import os
import csv

def search_csv_files(directory, search_string):
    # Get a list of all files in the directory
    files = [file for file in os.listdir(directory) if file.endswith('.csv')]

    # Iterate through each CSV file
    for file_name in files:
        file_path = os.path.join(directory, file_name)
        print(f"Searching in file: {file_name}")

        # Open the CSV file
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)

            # Iterate through each row in the CSV file
            for row in reader:
                # Check if the search string is in any column
                if any(search_string.lower() in column.lower() for column in row):
                    print(f"Found in file: {file_name}, row: {row}")
    else: print("Not found")

# Define the directory containing the CSV files
directory = '.'  # Current directory

# Define the search string
search_string = input("Enter the string you want to search for: ")

# Call the function to search CSV files
search_csv_files(directory, search_string)
