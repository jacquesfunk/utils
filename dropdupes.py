import polars as pl
import os
from rich import print

file = 'Script-19-20240531.csv'

# Get the filename without extension
filename = os.path.splitext(os.path.basename(file))[0]

# Read the CSV file into a Polars DataFrame
dforig = pl.read_csv(file)

# Drop duplicates based on "int_field" and "ext_field"
df = dforig.unique(subset=["factorsoft_client_number__c"])

# Save the DataFrame with unique records to a new CSV file
df.write_csv(f'{filename}_uniques.csv')

print(len(df))

print('Done')