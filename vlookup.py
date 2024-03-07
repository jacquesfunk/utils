import pandas as pd


def remove_whitespace_from_columns(df, columns_to_clean=None):
    """
    Remove leading and trailing whitespace from specified columns in a DataFrame.

    Parameters:
        df (pd.DataFrame): The input DataFrame.
        columns_to_clean (list or None): A list of column names to clean.
            If None, all string columns are cleaned.

    Returns:
        pd.DataFrame: The DataFrame with whitespace removed from specified columns.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")

    if columns_to_clean is None:
        # If columns_to_clean is not specified, clean all string columns
        columns_to_clean = [col for col in df.columns if df[col].dtype == "object"]

    cleaned_df = df.copy()

    for col in columns_to_clean:
        if col in cleaned_df.columns:
            cleaned_df[col] = cleaned_df[col].str.strip()

    return cleaned_df


df_main_orig = pd.read_excel(
    "Create Bundle Objects-August Cleanupv3.xlsx", sheet_name="Master File"
)
df_newfuel_orig = pd.read_csv("2023-09-28 Bundles.csv")

df_main = remove_whitespace_from_columns(df_main_orig, "CRM #")
df_newfuel = remove_whitespace_from_columns(df_newfuel_orig, "Account Name")


fuel_result = pd.merge(
    df_main[
        [
            "BI Report FC ID (If Needed)-18 Digit Guid",
            " CS Opportunity ID",
            " RTSF Opportunity Id",
            "Account Name/Bundle Object Name",
            "ACCOUNT ID",
            "Bundle Type",
            "Established Date",
            "Fuel Discount",
            "Fuel Discount Applied",
            "PFJ Response",
            "PFJ Review Sent",
            "Proposal Received Date",
            "Proposal Sent Date",
            "RTSCS Ops Review",
            "RTSF Contract ID",
            "Status",
        ]
    ],
    df_newfuel,
    on="ACCOUNT ID",
    how="inner",
)

# Select only the specified columns in the fuel_result DataFrame
selected_columns = [
    "ACCOUNT ID",
]

fuel_result = fuel_result[selected_columns]

fuel_result.to_csv("Bundled Fuel v2.csv", index=False)
