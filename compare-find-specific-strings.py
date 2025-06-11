# Read the contents of the files
with open(r'C:\Users\mahmad\OneDrive - Ryan RTS\Downloads\rs-parameters.txt', 'r') as file:
    rs_parameters = file.read().splitlines()

with open(r'C:\Users\mahmad\OneDrive - Ryan RTS\Downloads\dbx-parameters.txt', 'r') as file:
    dbx_parameters = file.read().splitlines()

# Replace the '.' after 'parameters' with '_' in the dbx_parameters list
dbx_parameters = [param.replace('parameters.', 'parameters_') for param in dbx_parameters]

# List of prefixes to check
prefixes = [
    "parameters_distancetiersdistancetiers",
    "parameters_fixedlaneslanes",
    "parameters_conditionedlanes",
    "parameters_conditionedlanesorigins",
    "parameters_conditionedlanesbystate",
    "parameters_conditionedlanesdestinations",
    "parameters_leadtimetimes",
    "parameters_restrictedlaneslanes",
    "parameters_restrictedlanesdestinations",
    "parameters_restrictedlanesorigins",
    "parameters_restrictedlaneslanebystate",
    "parameters_restrictedlanesoriginsstates",
    "parameters_restrictedlanesdestinationsstates",
    "parameters_seasonality",
    "parameters_crossborderlanes",
    "parameters_transittimevariance"
]

# Function to check for prefixes
def check_prefixes(parameters, prefixes):
    return [param for param in parameters if any(param.startswith(prefix) for prefix in prefixes)]

# Check for prefixes in each list
rs_matches = check_prefixes(rs_parameters, prefixes)
dbx_matches = check_prefixes(dbx_parameters, prefixes)

# Write the results to a new file
output_file = r'C:\Users\mahmad\OneDrive - Ryan RTS\Downloads\prefix_check_results.txt'
with open(output_file, 'w') as file:
    file.write("Matches in rs-parameters:\n")
    file.write("\n".join(rs_matches))
    file.write("\n\nMatches in dbx-parameters:\n")
    file.write("\n".join(dbx_matches))

print(f"Prefix check results written to {output_file}")