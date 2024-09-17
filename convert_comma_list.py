import subprocess

# Input list of strings with line breaks
input_string = """Exceptions_20240915.csv Exceptions_20240309.csv Exceptions_20240307.csv Exceptions_20240305.csv Exceptions_20240707.csv Exceptions_20240630.csv Exceptions_20240627.csv Exceptions_20240908.csv Exceptions_20240910.csv Exceptions_20240913.csv
"""

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

# # Split the input into a list of strings without quotes around each item
# strings_list = input_string.strip().split("\n")
# result = ", ".join(strings_list)

# Split the input into a list of strings with quotes around each item
# strings_list = input_string.strip().split("\n")
strings_list = input_string.strip().split(" ")
formatted_list = [f"'{name}'" for name in strings_list]
result = ", ".join(formatted_list)

# Print the result to the terminal
print(result)

# Copy to the clipboard
copy2clip(result)

# # Enclose the result in parentheses
# final_result = f"({result})"

# # Print paren enclosed result to the terminal
# print(final_result)

# # Copy paren enclosed result to the clipboard
# copy2clip(final_result)