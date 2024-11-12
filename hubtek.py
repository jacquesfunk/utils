"""
1. Get parameters files for the following dates:
2024-02-12- Berry Plastics data present
2024-02-13- Berry Plastics data not present
2024-03-27- Anheuser data present
2024-03-28- Anheuser data not present
2024-10-13- data for both is present
"""

import pandas as pd

# List of CSV file paths
csv_files = [
    r"C:\Users\mahmad\OneDrive - Ryan RTS\Downloads\Parameters_20240327.csv",
    # Add other file paths as needed
]

# Names to filter by
filter_names = ["Anheuser Busch", "Berry Plastics"]

# Initialize an empty DataFrame to hold all filtered data
all_data = pd.DataFrame()

# Loop through each CSV file
for file in csv_files:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file)

    # Filter the DataFrame for the specified names
    filtered_df = df[df["name"].isin(filter_names)]

    # Append the filtered DataFrame to all_data
    all_data = pd.concat([all_data, filtered_df], ignore_index=True)

# Write the final concatenated DataFrame to a new CSV
all_data.to_csv("hubtekresults.csv", index=False)

print(all_data)
