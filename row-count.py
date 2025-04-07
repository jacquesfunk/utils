import polars as pl

file_path = r'C:\Users\mahmad\OneDrive - Ryan RTS\Downloads\fuel_trans_summ_20250403_095225_000'

df = pl.read_csv(file_path)
total_rows = len(df)

print(total_rows)