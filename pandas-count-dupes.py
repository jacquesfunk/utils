from pathlib import Path
import pandas as pd
from rich import print


def main():
    # Set the directory containing the cleaned CSV files
    data_dir = Path(
        r"C:\Users\mahmad\OneDrive - Ryan RTS\code"
    )  # Replace with your directory path

    if not data_dir.is_dir():
        print(f"[red]Error: The directory {data_dir} does not exist.[/red]")
        return

    # Define file paths
    df1_filename = data_dir / "datafile1.csv"
    df2_filename = data_dir / "datafile2.csv"

    if not df1_filename.exists() or not df2_filename.exists():
        print(f"[red]Error: One or more files do not exist in {data_dir}.[/red]")
        return

    # Read DataFrames
    df1 = pd.read_csv(df1_filename)
    df2 = pd.read_csv(df2_filename)

    # Count duplicate values in transaction ID columns
    df1_id_dupes = len(df1["id"]) - len(df1["id"].drop_duplicates())
    print(f"Number of duplicate transaction IDs in DF1: {df1_id_dupes}")

    df2_id_dupes = len(df2["id"]) - len(df2["id"].drop_duplicates())
    print(f"Number of duplicate transaction IDs in DF2: {df2_id_dupes}")

    # Save cleaned DataFrames for further processing
    df1_cleaned = df1.drop_duplicates(subset=["id"])
    df2_cleaned = df2.drop_duplicates(subset=["id"])

    # Save to intermediate files
    df1_cleaned.to_csv("df1_cleaned.csv", index=False)
    df2_cleaned.to_csv("df2_cleaned.csv", index=False)
    print("Cleaned data saved to intermediate files.")


if __name__ == "__main__":
    main()
