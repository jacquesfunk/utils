from pathlib import Path

# Specify the directory
directory = Path(r"C:\Users\mahmad\OneDrive - Ryan RTS\Downloads")

# Iterate through the files in the directory and rename them
for file in directory.iterdir():
    if file.is_file():
        new_name = file.name.replace("_", "-").replace(" ", "-").lower()
        new_path = directory / new_name
        if file.name != new_name:  # Ensure the name actually changes
            file.rename(new_path)

print(f'Replaced "_" and whitespace with "-", and converted filenames to lowercase in {directory}')
