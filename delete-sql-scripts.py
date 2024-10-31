import os
import glob

def delete_files_with_pattern(directory, pattern):
    os.chdir(directory)  # Change current working directory to specified directory
    files_to_delete = glob.glob(pattern)
    for file in files_to_delete:
        os.remove(file)

if __name__ == "__main__":
    directory = r"C:\Users\mahmad\AppData\Roaming\DBeaverData\workspace6\General\Scripts"  # Specify the directory where files are located
    pattern = "Script-*.sql"  # Specify your pattern here
    delete_files_with_pattern(directory, pattern)
    print("Deletes are done")
