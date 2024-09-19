import polars as pl
from rich import print


def load_data(file_path):
    return pl.read_csv(file_path)


def count_total_rows(df):
    return len(df)


def sort_columns_by_non_null(df: pl.DataFrame) -> list:
    # Count non-null values for each column
    non_null_counts = df.select(
        [pl.col(col).drop_nulls().count().alias(col) for col in df.columns]
    )

    # Convert to dictionary and filter columns with non-null values greater than 0
    sorted_columns = dict(
        zip(non_null_counts.columns, non_null_counts.row(0))
    )  # Convert to dictionary
    sorted_columns = {k: v for k, v in sorted_columns.items() if v > 0}

    # Sort columns by non-null counts in descending order
    sorted_columns = sorted(sorted_columns.items(), key=lambda x: x[1], reverse=True)

    return sorted_columns


def print_results(total_rows, sorted_columns, title):
    print(f"Total rows: {total_rows}")
    print(f"{title}:")
    for col, count in sorted_columns:
        print(f"{col}: {count}")


# Load datasets
df = load_data(
    r"C:\Users\mahmad\OneDrive - Ryan RTS\Downloads\dim_fuelcard_202409191058.csv"
)

# Count total rows in each DataFrame
total_rows_df = count_total_rows(df)

# Sort columns by the number of non-null values
sorted_columns = sort_columns_by_non_null(df)

# Print results
print_results(total_rows_df, sorted_columns, "Counts")
