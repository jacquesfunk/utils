import polars as pl

# Read the CSV file
df = pl.read_csv(
    r"C:\Users\mahmad\OneDrive - Ryan RTS\Downloads\password-rotation-source-v2.csv"
)

# Group by 'System' and then by 'Rotation Deadline', count records in each group
result = (
    df.group_by(["System", "Rotation Deadline"])
      .agg(pl.count().alias("count"))
      .sort(["System", "Rotation Deadline", "count"], descending=[False, False, True])
)

# Save the result to a CSV file
result.write_csv(r"C:\Users\mahmad\OneDrive - Ryan RTS\Downloads\password-rotation-system-deadline-pivot.csv")

print('Done')