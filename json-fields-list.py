import json
import json_repair
import pandas as pd
from pathlib import Path

# Load the csv file
file_path = Path(r'C:\Users\mahmad\OneDrive - Ryan RTS\Downloads\brok_hubtek_quote_exception_v9-20250217-Redshift_Prod.csv')

df = pd.read_csv(file_path)

# Extract headers
headers = df.columns.tolist()

# Write the headers to a text file, transposed as a list
output_file = Path(r'C:\Users\mahmad\OneDrive - Ryan RTS\Downloads\redshift_exception_headers.txt')
with output_file.open('w', encoding='utf-8') as file:
    for header in headers:
        file.write(header + '\n')

print(f"Headers written to {output_file}")