import pandas as pd
import csv

df1 = pd.read_excel(
    "Create Bundle Objects-August Cleanupv3.xlsx", sheet_name="Master File"
)
df2 = pd.read_csv("2023-09-28 Bundles.csv")


def xlookup(lookup_value, lookup_array, return_array, if_not_found: str = None):
    match_value = return_array.loc[lookup_array == lookup_value]

    if match_value.empty:
        return if_not_found

    else:
        return match_value.tolist()[0]


df1 = df1[df1["CRM #"].notna()]

df1["Bundle Type"] = df1["CRM #"].apply(
    xlookup, args=(df2["CRM #"], df2["Bundle Type"])
)

columns = ["CRM #", "Bundle Type"]

with open("users.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(columns)
    for index, row in df1.iterrows():
        if pd.isnull(row["Bundle Type"]):
            continue  # skip row if Bundle Type is null
        writer.writerow([row["CRM #"], row["Bundle Type"]])
