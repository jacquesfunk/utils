import polars as pl

# Read the dataset from a CSV file
df = pl.read_csv(
    "part-00000-tid-2659363838259475703-6031fdb8-b31c-4691-9047-fe28ed7dd359-4-1-c000.csv"
)

# Filter the records
updated_df = df.filter(
    pl.col("DOT_Number__c").is_in(
        [
            901149,
            3551633,
            3272608,
            2084644,
            1329510,
            3934330,
            3318509,
            4107527,
            3637719,
            3414513,
            2046380,
            3486661,
            3823018,
            4089593,
            1024009,
            4029287,
            728326,
            3321304,
            1444749,
            3426030,
            3305891,
            4105507,
            3694733,
            3625008,
            977831,
            79127,
            3424092,
            4003610,
            675236,
            3027659,
            2634486,
            3220882,
            3808871,
            2967527,
            4069255,
            3274895,
            3825460,
            3978384,
            3445904,
            4101745,
            2572955,
            3404664,
            1239587,
            2537388,
            3163128,
            2558809,
        ]
    )
)

# Columns to include in output
columns = [
    "Name",
    "DOT_Number__c",
    "Cargo__c",
    "Class__c",
    "Entity_Type__c",
    "Operations_Classification__c",
]

# Select the desired columns
final_df = updated_df.select(columns)

df_sorted = final_df.sort(["Name"], descending=False)

# Write final file
df_sorted.write_csv('carrierprofiletestoutput.csv')
