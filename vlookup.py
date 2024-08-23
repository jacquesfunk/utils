import polars as pl
from datetime import datetime as dt

# Get the current date
current_date = dt.now()

df_main_orig = pl.read_excel(
    "Create Bundle Objects-August Cleanupv3.xlsx", sheet_name="Master File"
)
df_newfuel_orig = pl.read_csv("2023-09-28 Bundles.csv")

fuel_result = df_newfuel_orig.join(
    df_main
    by=[
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
    "Status"]
    on="ACCOUNT ID",
    how="inner")

# Select only the specified columns in the fuel_result DataFrame
selected_columns = [
    "ACCOUNT ID",
]

fuel_result = fuel_result[selected_columns]

ticket_number = 'insert Jira number here'
output_filename = f"DS{ticket_number}_{current_date}_output.csv"

fuel_result.to_csv(output_filename, index=False)
