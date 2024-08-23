import subprocess

# Input list of strings with line breaks
input_string = """0013x00002KEHmXAAX
0013x00002KEwzCAAT
0013x00002KEujyAAD
0013x00002KEw4WAAT
0013x00002KFPMJAA5
0013x00002KG1kqAAD
0013x00002KuKt2AAF
0013x00002KtcAkAAJ
0013x00002KtcNXAAZ
0013x00002Kuw3qAAB
0013x00002Ku952AAB
0013x00002KvS5xAAF
0013x00002Kvo31AAB
0013x00002KuTRfAAN
0013x00002KuTm4AAF
0011H00001nbqa2QAA
0013x00002Kw8gbAAB
0013x00002KwRp5AAF
0013x00002KuTzNAAV
0013x00002KurORAAZ
0013x00002KurOgAAJ
0013x00002OitsjAAB
0013x00002OiuiGAAR
0013x00002OiunQAAR
0013x00002OjclTAAR
0013x00002OjczpAAB
0013x00002QPaWkAAL
0013x00002Ojd6WAAR
0013x00002QPadMAAT
0013x00002Rr5ZUAAZ
"""

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

# Split the input into a list of strings without quotes around each item
strings_list = input_string.strip().split("\n")
result = ", ".join(strings_list)

# # Split the input into a list of strings with quotes around each item
# strings_list = input_string.strip().split("\n")
# formatted_list = [f"'{name}'" for name in strings_list]
# result = ", ".join(formatted_list)

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