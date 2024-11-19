# Define the two dictionaries
dbx_fields = {
    "Descr": "string",
    "DefaultAmt": "double",
    "PurchasesOk": "boolean",
    "CollectionsOk": "boolean",
    "Balance": "double",
    "FinCode": "string",
    "AcctNo": "string",
    "CurrencyType": "string",
    "CashAcct": "boolean",
    "LoansOk": "boolean",
    "AutoCheckOnly": "boolean",
    "NextCheckNo": "string",
    "CostCenter": "string",
    "SubHdgAcctNo": "string",
    "FinReportNo": "int",
    "FinCategory": "int",
    "FinType": "int",
    "FinPrint": "boolean",
    "ReptModName": "string",
    "Accounts": "int",
    "BankAcctNo": "string",
    "BankAbaNo": "string",
    "HoldAcct": "int",
    "HoldAbbr": "string",
    "PostFuOnHold": "boolean",
    "RemindType": "int",
    "RemindUser": "string",
    "RemindDays": "int",
    "TaxableCode": "int",
    "WireChargeAcctNo": "string",
    "WireChargeAmt": "double",
    "PayByMethod": "int",
    "Earnings": "int",
    "PreviewCheck": "boolean",
    "RunClientCalc": "boolean",
    "WashHoldOk": "boolean",
    "Office": "string",
    "CountryCode": "string",
    "SwiftCode": "string",
    "NfeInclude": "boolean",
    "AnalysisCode": "string",
    "CheckPrefix": "string",
    "AltCashAcct": "string",
    "Deferred": "boolean",
    "LockBy": "string",
    "LockTime": "timestamp",
    "ACHCOID": "string"
}

redshift_fields = {
    "Descr": "text",
    "DefaultAmt": "double precision",
    "PurchasesOk": "boolean",
    "CollectionsOk": "boolean",
    "Balance": "double precision",
    "FinCode": "text",
    "AcctNo": "text",
    "CurrencyType": "text",
    "CashAcct": "boolean",
    "LoansOk": "boolean",
    "AutoCheckOnly": "boolean",
    "NextCheckNo": "text",
    "CostCenter": "text",
    "SubHdgAcctNo": "text",
    "FinReportNo": "smallint",
    "FinCategory": "smallint",
    "FinType": "smallint",
    "FinPrint": "boolean",
    "ReptModName": "text",
    "Accounts": "integer",
    "BankAcctNo": "text",
    "BankAbaNo": "text",
    "HoldAcct": "smallint",
    "HoldAbbr": "text",
    "PostFuOnHold": "boolean",
    "RemindType": "smallint",
    "RemindUser": "text",
    "RemindDays": "smallint",
    "TaxableCode": "smallint",
    "WireChargeAcctNo": "text",
    "WireChargeAmt": "double precision",
    "PayByMethod": "smallint",
    "Earnings": "integer",
    "PreviewCheck": "boolean",
    "RunClientCalc": "boolean",
    "WashHoldOk": "boolean",
    "Office": "text",
    "CountryCode": "text",
    "SwiftCode": "text",
    "NfeInclude": "boolean",
    "AnalysisCode": "text",
    "CheckPrefix": "text",
    "AltCashAcct": "text",
    "Deferred": "boolean",
    "LockBy": "text",
    "LockTime": "timestamp without time zone",
    "ACHCOID": "text"
}

# Transformation rules
type_mapping = {
    "text": "string",
    "smallint": "int",
    "integer": "int",
    "double precision": "double",
    "timestamp without time zone": "timestamp"
}

# Update redshift_fields to match dict1 format
updated_redshift_fields = {
    key: type_mapping.get(value, value)
    for key, value in redshift_fields.items()
}

# Find keys in redshift_fields that are not in dbx_fields
missing_in_dbx = {key for key in redshift_fields if key not in dbx_fields}

# Find keys in dbx_fields that are not in redshift_fields
missing_in_redshift = {key for key in dbx_fields if key not in updated_redshift_fields}

# Find keys with mismatched types
type_mismatches = {
    key: (dbx_fields.get(key), updated_redshift_fields[key])
    for key in redshift_fields
    if key in dbx_fields and dbx_fields[key] != updated_redshift_fields[key]
}

# Print results
print("Keys in redshift_fields that are not in dbx_fields:")
if missing_in_dbx:
    for key in missing_in_dbx:
        print(f"  - {key}")
else:
    print("No mismatches")

print("\nKeys in dbx_fields that are not in redshift_fields:")
if missing_in_redshift:
    for key in missing_in_redshift:
        print(f"  - {key}")
else:
    print("No mismatches")

print("\nKeys with mismatched types:")
if type_mismatches:
    for key, (dbx_type, redshift_type) in type_mismatches.items():
        print(f"  - {key}: dbx_fields={dbx_type}, redshift_fields={redshift_type}")
else:
    print("No mismatches")