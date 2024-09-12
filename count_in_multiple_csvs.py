import os
import csv

def count_records_in_csv_files(directory, filename_prefix):
    total_record_count = 0
    total_files_processed = 0

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        if filename.startswith(filename_prefix) and filename.endswith('.csv'):
            file_path = os.path.join(directory, filename)
            try:
                with open(file_path, 'r', newline='', encoding='utf-8') as file:
                    reader = csv.reader(file)
                    # Skip the header
                    next(reader, None)
                    # Count the remaining lines
                    file_record_count = sum(1 for row in reader)
                    total_record_count += file_record_count
                    total_files_processed += 1
                    print(f"Processed file: {filename}, Records: {file_record_count}")
            except Exception as e:
                print(f"Error processing file {filename}: {e}")
    
    return total_record_count, total_files_processed

# Example usage
directory = '.'  # Current directory
filename_prefix = 'lead_fmcsa'
total_records, files_processed = count_records_in_csv_files(directory, filename_prefix)
print(f'Total number of records (excluding headers): {total_records}')
print(f'Total number of files processed: {files_processed}')
