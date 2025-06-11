import pandas as pd

# Read the dataset from a CSV file
df = pd.read_csv(r'C:\Users\mahmad\OneDrive - Ryan RTS\projects\pws-access-pwd.csv')

order_number = 1
for index, row in df.iterrows():
    if pd.notnull(row['recommendation']) and pd.isnull(row['order']):
        df.at[index, 'order'] = order_number
        order_number += 1

# Write the filtered and sorted rows to a new CSV file
output_file = r'C:\Users\mahmad\OneDrive - Ryan RTS\Downloads\pws-access-pwd-updated.csv'
df.to_csv(output_file, index=False)

print(f"Filtered and sorted CSV written to {output_file}")