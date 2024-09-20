import polars as pl

df = pl.read_excel(
    source= r"C:\Users\mahmad\OneDrive - Ryan RTS\1- Projects\datasets needing lineage .xlsx",
    sheet_name="Sheet1",
)

df_select = df.select(["dataset id", "dataset name"])
# Add new columns with the new headers
df_final = df_select.with_columns(
    [
        pl.Series("schema_name", [None] * df.height),
        pl.Series("tables_used", [None] * df.height),
    ]
)

df_final.write_csv(r"C:\Users\mahmad\OneDrive - Ryan RTS\1- Projects\DS5121.csv")