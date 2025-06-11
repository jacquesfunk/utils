import polars as pl

df = pl.read_csv(
    r"C:\Users\mahmad\OneDrive - Ryan RTS\Downloads\password-rotation-source-v3.csv",
)

# Function to create a grouped DataFrame
def create_grouped_df(df, column_name):
    return (
        df.group_by(column_name)
        .agg(pl.col(column_name).count().alias("count"))
        .sort("count", descending=True)
    )


# Columns to analyze
columns1 = ["Proposed Rotation Deadline"]
columns2 = ["System"]
columns3 = ["Current Deadline"]

create_grouped_df(df, columns1[0]).write_csv(
    r"C:\Users\mahmad\OneDrive - Ryan RTS\Downloads\pivot-password-proposed-rotation-deadline.csv"
)
create_grouped_df(df, columns2[0]).write_csv(
    r"C:\Users\mahmad\OneDrive - Ryan RTS\Downloads\pivot-password-system.csv"
)
create_grouped_df(df, columns3[0]).write_csv(
    r"C:\Users\mahmad\OneDrive - Ryan RTS\Downloads\pivot-password-current-deadline.csv"
)

print("Pivot tables created and saved as CSV files.")