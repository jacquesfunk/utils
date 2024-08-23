import os
import json


def delete_first_line(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()[1:]
    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(lines)


def merge_json_files(directory, output_file, non_json_file):
    if not os.path.exists(directory):
        print(f"Directory does not exist: {directory}")
        exit(1)

    merged_data = []
    non_json_content = []

    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            file_path = os.path.join(directory, filename)
            delete_first_line(file_path)
            with open(file_path, "r", encoding="utf-8") as file:
                try:
                    data = json.load(file)
                    merged_data.append(data)
                except json.JSONDecodeError:
                    print(f"Non-JSON content found in file: {file_path}")
                    non_json_content.append(file_path)

    with open(non_json_file, "w", encoding="utf-8") as non_json_outfile:
        for file_path in non_json_content:
            with open(file_path, "r", encoding="utf-8") as file:
                non_json_outfile.write(file.read())
            non_json_outfile.write("\n\n")

    with open(output_file, "w", encoding="utf-8") as outfile:
        json.dump(merged_data, outfile, indent=4)


directory = r"C:\Users\mahmad\OneDrive - Ryan RTS\1- Projects\Python"
output_file = "merged_output.json"
non_json_file = "non_json_content.txt"
merge_json_files(directory, output_file, non_json_file)
