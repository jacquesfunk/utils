from pathlib import Path


def rename_files(directory, id, start_record):
    # Convert directory to a Path object
    directory_path = Path(directory)

    # Check if the directory exists
    if not directory_path.exists():
        print(f"Error: The directory '{directory}' does not exist.")
        return

    # Get a list of all files in the directory
    files = list(directory_path.iterdir())

    # Initialize the record number
    record_number = start_record

    # Loop through each file in the directory
    for file in files:
        # Skip if it's not a file
        if not file.is_file():
            continue

        # Construct the new filename
        new_filename = f"{id}-{record_number}{file.suffix}"

        # Create the new file path
        new_file_path = directory_path / new_filename

        try:
            # Rename the file
            file.rename(new_file_path)
            print(f"Renamed '{file.name}' to '{new_filename}'")

            # Increment the record number
            record_number += 1
        except Exception as e:
            print(f"Error renaming file '{file.name}': {e}")

    print("Files have been renamed successfully.")


# Static directory path
directory = r"C:\Users\mahmad\OneDrive - Ryan RTS\1-Projects\Python\rename"

# Input the id and starting record number
id = input("Enter the ID: ")
start_record = int(input("Enter the starting record number: "))

# Call the function to rename files
rename_files(directory, id, start_record)
