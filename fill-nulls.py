import polars as pl

# Read the dataset from a CSV file, ensuring all columns are read and empty values are handled
df = pl.read_csv(r"C:\Users\mahmad\OneDrive - Ryan RTS\Downloads\password-update.csv")

# Fill null or blank values with 0 in the "Must be on network" column
updated_df = df.with_columns([
    pl.col("Must be on network").fill_null(0),
])

# Write the entire DataFrame back to a new CSV file
updated_df.write_csv(r"C:\Users\mahmad\OneDrive - Ryan RTS\Downloads\20250312-passwords_null_resolved.csv")

print("Null or blank values in 'Must be on network' column filled with 0 and saved to new CSV file.")