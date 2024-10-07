import subprocess

# Input list of strings with line breaks
input_string = """
a0N1H00001EBU9bUAH
a0N1H00001EUu6jUAD
a0N3x00000pnTIZEA2
a0N3x00000pnTIZEA2
a0N3x00000patEnEAI
a0N3x00000pbQvzEAE
a0N3x00000pnTIZEA2
a0N3x00000pcFLpEAM
a0N3x00000qtYAcEAM
a0N3x00000qtwwYEAQ
a0N3x00000pbQvzEAE
a0N3x00000quqefEAA
a0N3x00000qvUvOEAU
a0N3x00000tNmZVEA0
a0N3x00000qtYAcEAM
a0N3x00000tOMnQEAW
a0N3x00000qtwwYEAQ
a0N3x00000tOm5eEAC
a0N3x00000tOhHfEAK
a0N3x00000tOm5eEAC
a0N3x00000leecuEAA
a0N3x00000sF9SjEAK
a0N3x00000qtYAcEAM
a0N3x00000pbQvzEAE
a0N3x00000tOm5eEAC
a0N3x00000leecuEAA
a0N3x00000sF9SjEAK
a0N3x00000patEnEAI
a0N3x00000pnTIZEA2
a0N3x00000pcFLpEAM
a0N3x00000qvUvOEAU
a0N3x00000tNmZVEA0
a0N3x00000qtwwYEAQ
a0N3x00000v09mSEAQ
a0N3x00000v09mSEAQ
a0N3x00000sF9SjEAK
a0N3x00000vLeh8EAC
a0N3x00000vUlwjEAC
a0N3x00000vUu7bEAC
a0N3x00000vW4VXEA0
a0N3x00000vLeh8EAC
a0N3x00000tFAH3EAO
a0N3x00000vV6n6EAC
a0N3x00000vLeh8EAC
a0N3x00000vLeh8EAC
a0N3x00000qv4vaEAA
a0N1H00001EBU9bUAH
a0N1H00001EUu6jUAD
a0NVu000001cmSrMAI
a0NVu0000022Im5MAE
"""

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

# # Split the input into a list of strings without quotes around each item
# strings_list = input_string.strip().split("\n")
# result = ", ".join(strings_list)

# Split the input into a list of strings with quotes around each item
strings_list = input_string.strip().split("\n")
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