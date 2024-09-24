# Polars

## EDA

```
# Get a mapping of column names to their data type
df.schema

# Get the dataframe's shape
df.shape

# Get list of column names
df.columns

# Get the first x rows of a dataset
df.head(3)

# Count number of rows
df.height

# Count number of columns
df.width

# Get info on dataset
df.describe()

# Counts dupe rows
df.is_duplicated()

# Counts number of unique rows
expr_unique_subset = pl.struct("a", "b").n_unique()

# Count null values per column
df.null_count()

# Count non-null values in each column
df.count()

# Count unique values in each group
df.group_by("d", maintain_order=True).n_unique()

# window function
orders = pl.scan_csv("orders.csv")
customers = pl.scan_csv("customers.csv")

orders_w_order_rank_column = (
    orders
    .join(customers, on="customer_id", how="left")
    .with_columns([
        pl.col("order_date_utc").rank()
        .over(pl.col("is_premium_customer"))
        .alias("order_rank")
    ])
)

(
    orders_w_order_rank_column
    .filter(pl.col("order_rank").le(2))
    .group_by(pl.col("is_premium_customer"))
    .agg(pl.col("order_value_usd").sum().name.prefix("sum_"))
    .collect()
)
```

## Update dataset

```
# Add blank columns to dataframe
df_final = df_select.with_columns(
    [
        pl.Series("schema_name", [None] * df.height),
        pl.Series("tables_used", [None] * df.height),
    ]
)

# Create new columns

    # create year column by extracting year from date column
    df_pl = df_pl.with_columns(pl.col("sales_date").dt.year().alias("year"))

    # create price column by dividing sales revenue by sales quantity
    df_pl = df_pl.with_columns((pl.col("sales_rev") / pl.col("sales_qty")).alias("price"))

    # create a column with a constant value
    df_pl = df_pl.with_columns(pl.lit(0).alias("dummy_column"))

# Add columns to dataframe by passing a list of expressions
df.with_columns(
    [
        (pl.col("a") ** 2).alias("a^2"),
        (pl.col("b") / 2).alias("b/2"),
        (pl.col("c").not_()).alias("not c"),
    ]
)

# Sort by one column
df.sort('A')

# Sort by multiple columns
df.sort("c", "a", descending=[False, True])

# Set column names
df.columns = ["apple", "banana", "orange"]

# Fill floating point NaN value with a fill value
df.with_columns(pl.col("b").fill_nan(0))

# Fill all na's
df.fill_none(value)

# Filter the expression based on one or more predicate expressions.
# The original order of the remaining elements is preserved.
# Elements where the filter does not evaluate to True are discarded, including nulls.
df.group_by("group_col").agg(
    lt=pl.col("b").filter(pl.col("b") < 2).sum(),
    gte=pl.col("b").filter(pl.col("b") >= 2).sum(),
).sort("group_col")

# Replace multiple values by passing sequences to the old and new parameters
df.with_columns(replaced=pl.col("a").replace([2, 3], [100, 200]))

# Transpose data
df.transpose(include_header=True)

# Remove columns from df
df.drop(["bar", "ham"])

# Drop a subset of columns, as defined by name or with a selector
df.drop_nulls(subset=cs.integer())

# Rename columns
df.rename({"foo": "apple"})

# Add column showing % change between rows
df.with_columns(pl.col("a").pct_change().alias("pct_change"))

# Choose columns to include in output
# single
df.select('A')

# double
df.select('A', 'B')

# Sum multiple columns
df.select(pl.sum("a", "c"))

# Sum all values horizontally across columns
df.with_columns(sum=pl.sum_horizontal("a", "b"))

# Count the occurrences of unique values in a column
df.select(pl.n_unique("b", "c"))

# Generate an index column by using len in conjunction with int_range()
df.select(
    pl.int_range(pl.len(), dtype=pl.UInt32).alias("index"),
    pl.all(),
)

# Get the maximum value horizontally across columns
df.with_columns(max=pl.max_horizontal("a", "b"))

# Round the values as specified and format as currency
df = df.with_columns([
    pl.col('Risk').round(2).map_elements(lambda x: f"${x:,.2f}", return_dtype=pl.Utf8)])

# Update data types for multiple columns
filtered_df = df.with_columns([
    pl.col("dot_number__c").cast(pl.Int64),
    pl.col("mc_number__c").cast(pl.Int64),
    pl.col("physphonenbr").cast(pl.Int64),
    pl.col("trucknbr").cast(pl.Int64)
])

# change the data type of sales date from string to date
df_pl = df_pl.with_columns(pl.col("sales_date").str.to_date())

# merge 2 datasets
df1.join(df2, on='key')

# merge >2 datasets
df1.join(df2, on='key').join(df3, on='key')

# concatenate dataframes
pl.concat([df1, df2])

# Sort columns
df.select(sorted(df.columns))

# Sort columns in reverse order
df.select(sorted(df.columns, reverse=True))

# Select columns based on headers
q = (
    pl.scan_csv('Titanic_train.csv')
    .select(
        ['Name','Age']
    )
)
q.collect()

# Exclude only one column
q = (
    pl.scan_csv('Titanic_train.csv')
    .select(
        pl.exclude('PassengerId')
    )
)
q.collect()

# Select columns based on string

q = (
    pl.scan_csv('Titanic_train.csv')
    .select(
        pl.col('^S.*$')  # get all columns that starts with S
    )
)
q.collect()

# Split columns
# Part 1
q = (
    pl.scan_csv('names.csv')
    .select(
    [
        'name',
        pl.col('name').str.split(' ').alias('splitname'),
        'age',
    ])
)
q.collect()

# Part 2
q = (
    pl.scan_csv('names.csv')
    .select(
    [
        'name',
        pl.col('name').str.split(' ').alias('split_name'),
        'age',
    ])
    .with_column(
        pl.struct(
            [
                pl.col('split_name').arr.get(i).alias(
                    'first_name' if i==0 else 'last_name') 
                for i in range(2)
            ]
        ).alias('split_name')
    )
)
q.collect()
```

## Categorical Filters and queries 

```
# basic filters
    # sales quantity is more than 0
    df_pl.filter(pl.col("sales_qty") > 0)

    # store code is B1
    df_pl.filter(pl.col("store_code") == "B1")

    # sales quantity is more than 0 and store code is A2
    df_pl.filter((pl.col("store_code") == "A2") & (pl.col("sales_qty") > 0))

    # product code is one of the following: 89909, 89912, 89915, 89918
    df_pl.filter(pl.col("product_code").is_in([89909, 89912, 89915, 89918]))

# Replace all matching regex/literal substrings with a new string value
df.with_columns(pl.col("text").str.replace_all("a", "-"))

# apply case-insensitive string replacement
df.with_columns(
    pl.col("weather").str.replace_all(
        r"(?i)foggy|rainy|cloudy|snowy", "Sunny"
    )
)

# split text to columns using delimiter
df.with_columns(
    pl.col("s").str.split(by="_").alias("split"))

# Remove leading and trailing characters
df.with_columns(foo_stripped=pl.col("foo").str.strip_chars())

# Count characters in all strings in a column
df.with_columns(
    pl.col("a").str.len_chars().alias("n_chars"))

# Check if string contains a substring that matches a pattern and doesn't use regex
df.select(pl.col("txt").str.contains("rab$", literal=True).alias("literal"))

# determines if any of the patterns find a match
df = pl.DataFrame(
    {
        "lyrics": [
            "Everybody wants to rule the world",
            "Tell me what you want, what you really really want",
            "Can you feel the love tonight",
        ]
    }
)
df.with_columns(
    pl.col("lyrics").str.contains_any(["you", "me"]).alias("contains_any")
)

# Return the index position of the first substring matching a pattern.
df.select(
    pl.col("txt"),
    pl.col("txt").str.find("a|e").alias("a|e (regex)"),
    pl.col("txt").str.find("e", literal=True).alias("e (lit)"),
)

```
## Numerical Filters and queries 

```
# Iterate over the groups of the group by operation
for name, data in df.group_by(["foo"]):
    print(name)
    print(data)

# Basic group by functions
    # calculate total and average sales for each store
    df_pl.group_by(["store_code"]).agg(
        pl.sum("sales_qty").alias("total_sales"),
        pl.mean("sales_qty").alias("avg_sales")
    )

    # calculate total and average sales for each store-year pair
    df_pl.group_by(["store_code", "year"]).agg(
        pl.sum("sales_qty").alias("total_sales"),
        pl.mean("sales_qty").alias("avg_sales")
    )

    # create product lifetime and unique day count for each product
    df_pl.group_by(["product_code"]).agg(
        [
            pl.n_unique("sales_date").alias("unique_day_count"),
            ((pl.max("sales_date") - pl.min("sales_date")).dt.total_days() + 1).alias("lifetime")
        ]
    )

# Compute aggregations for each group of a group by operation
df.group_by("a").agg(pl.col("b"), pl.col("c"))

# Compute multiple aggregates at once by passing a list of expressions
df.group_by("a").agg([pl.sum("b"), pl.mean("c")])

# Compute the sum of a column for each group
df.group_by("a").agg(pl.col("b").sum())

# Filter on multiple conditions
df.filter((pl.col("foo") < 3) & (pl.col("ham") == "a"))

# Create a spreadsheet-style pivot table as a DataFrame
df.pivot(index="foo", columns="bar", values="baz", aggregate_function="sum")

# Pivot using selectors to determine the index/values/columns
df.pivot(
    index=cs.string(),
    columns=cs.string(),
    values=cs.numeric(),
    aggregate_function="sum",
    sort_columns=True,
).sort(
    by=cs.string(),
)

# Select columns from df
df.select(["foo", "bar"])

# Start a when-then-otherwise expression
df.with_columns(pl.when(pl.col("foo") > 2).then(1).otherwise(-1).alias("val"))

# Window function for grouping by single column
df.with_columns(
    pl.col("c").max().over("a").name.suffix("_max"),
)

# Window function for grouping by multiple columns by passing a list of column names or expressions
df.with_columns(
    pl.col("c").min().over(["a", "b"]).name.suffix("_min"),
)
```

## Numpy
```
# Return pairwise Pearson product-moment correlation coefficients between columns. Requires numpy to be installed.
df.corr()
```

## Lambda functions
```
df.with_column(pl.col('A').apply(lambda x: x*2))
```

#  Pandas

## EDA

```
# Get info on dataset
df.info()

# List all df columns
df.columns

# Show first few rows of dataset
df.head()

# Show last few rows of dataset
df.tail()

# Number of rows in df
len(df)

# counts null values
df.isnull()

# counts NA values
df.isna()

# counts values that aren't NA
df.notna()

# assert that there are no missing values in the dataframe
assert pd.notnull(df).all().all()

# assert all values are greater than 0

assert (df >=0).all().all()
```


## Filters and queries 

```
# Show specific rows and columns
df.iloc[2:10, 5:10]

# Show specific row numbers and column names
df.loc[[3, 10, 14, 23], ["nationality", "weight_kg", "height_cm"]]

# Filter rows in df
df.query("shooting > passing")

# Show all dtypes of df columns
df.dtypes

# Find rows where string starts with
df[df.first_name.str.startswith("J")]

# select the variables or columns of a certain data type
df.select_dtypes(include="int64")

# query a dataset based on a boolean condition
df["random_col"].where(df["random_col"] > 50)

# used to find out the unique values of a categorical column
df.skill_moves.unique()

# remove duplicates from a list
unique_list = list(set(numbers))

# find most common element
from collections import Counter
most_common = Counter(numbers).most_common(1)

# make a subset of the dataset that will contain only a few nationalities of players using .isin() function
nationality = ["Argentina", "Portugal", "Sweden", "England"]
df[df.nationality.isin(nationality)]

# provides some basic statistical measures
df["wage_eur"].describe()

# number of data in the DataFrame in the specified direction.
# When the direction is 0, it provides the number of data in the columns.
# When the direction is 1, it provides the number of data in the rows
df.count(level="Pclass")
```


## Totals and grouping

```
# Rolling Methods
## rolling sum
data["rolling_sum_2"] = data.rolling(window = 2).Sales.sum()

## rolling sum over 2 days
data["rolling_sum_2days"] = data.rolling(window = '2d', on = "Date").Sales.sum()
 
## grouped rolling sum

data["rolling_sum_grouped"] = data.groupby("Payment_type").rolling(window = 2).\
                              Sales.sum().reset_index().set_index("level_1").\
                              sort_index()["Sales"]

## rolling mean aka moving average
data["Date"] = pd.to_datetime(data["Date"])
data["rolling_avg_3days"] = data.rolling(window = 6, min_periods=1).Sales.mean()


# provides you with the cumulative sum of all the values of the previous rows
df[["value_eur", "wage_eur"]].cumsum()

# lets you know how many unique values do you have in a column
df.nationality.nunique()

# group the data as per a certain variable
df.groupby("death")[
    "creatinine_phosphokinase",
    "ejection_fraction",
    "platelets",
    "serum_creatinine",
    "serum_sodium",
    "time",
].agg([np.mean, np.median])
.sum()

# value counts of each category
df["Pclass"].value_counts(sort=True, ascending=True, normalize=True)

# Melted the data
melted_df_single_var = pd.melt(df, id_vars=['Date', 'City'], var_name='Variable', value_name='Value')

# Melt the data with multiple value_vars
melted_df = pd.melt(df, id_vars=['Date', 'City'], value_vars=['Temperature', 'Humidity'], var_name='Variable', value_name='Value')

# Stack - pivot the innermost column index to become the innermost row index
stacked_df = df.set_index(['Date', 'City']).stack()

# Unstack - pivot the innermost row index to become the innermost column index
unstacked_df = stacked_df.unstack()

# Pivot Table
pivot_table_df = df.pivot_table(index='Date', columns='City', values=['Temperature', 'Humidity'], aggfunc='mean')

# Wide to Long
long_df = pd.wide_to_long(df, stubnames=['Temperature', 'Humidity'], i=['Date', 'City'], j='Variable', sep='_').reset_index()

pd.crosstab(
    df["league_rank"], df["international_reputation"]
)  # gives you a frequency table that is a cross-tabulation of two variables

# bins the data or segments the data based on the distribution of the data
pd.qcut(df["value_eur"], q=5)

# provide number of bins and split up dataset
pd.cut(df["value_eur"], bins=5).value_counts()

# percentage change between the current and a prior element in a Series or DataFrame
data = {
    "date": pd.date_range(start="2022-01-01", end="2022-01-05"),
    "price": [100, 105, 98, 110, 120],
}

df = pd.DataFrame(data).set_index("date")

df["price"].pct_change()

# Calculate rolling mean with a 7-day window
rolling_mean = data['value'].rolling(window=7).mean()

# Compute exponential moving average (EMA)
ema = data['value'].ewm(span=10).mean()

# find intersection of sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection = set1 & set2
```

## Update dataset

```
# When we reset the index, the old index is added as a column, and a new sequential index is used:
df.reset_index(names=['classes', 'names'])

# slice list
subset = numbers[2:5]

# list comprehension
squared_dict = {x: x**2 for x in range(5)}

# zip lists
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
person_info = dict(zip(names, ages))

# Append dataframes using result
result = df1.append([df2, df3])

# Append dataframes using pd.concat
frames = [df1, df2, df3]
result = pd.concat(frames)

# Drop columns from df
df = df.drop(columns=["Unnamed: 0", "weak_foot", "real_face"])

# replaces the values of a column
df.replace(1.0, 1.1)

# rename columns
df.rename(columns={"weight_kg": "Weight (kg)", "height_cm": "Height (cm)"})

# Update segment of data
df.loc[(df['COUNCIL'] == 'LEEDS') & (df['POSTCODE'] == 'LS8'), ['CCG']] = 'LEEDS NORTH CCG'

# replaces the null values with some other value of your choice
df["pace"].fillna(0, inplace=True)

# drop null values
df.dropna()

# Drop duplicates
people = people.drop_duplicates(subset="Name")

# Drop columns from dataframe
to_drop = ['Edition Statement', 'Corporate Author', 'Corporate Contributors', 'Former owner', 'Engraver', 'Contributors',
            'Issuance type',
            'Shelfmarks']
df.drop(to_drop, inplace=True, axis=1)

# Convert to DateTime format
pd.to_datetime(people["Graduation"])

# Change all strings to lower case in a column
people["Standing"] = people["Standing"].str.lower()

# Handling invalid values
df["height(cm)"] = pd.to_numeric(df["height(cm)"], errors='coerce')

# Split columns
df[['age','sex']] = df.age_sex.str.split("_", expand = True)

# Reorder column labels
df = df[['fname','lname','age','sex','section','height(cm)','weight(kg)','spend_A','spend_B','spend_C']]
```

# Numpy

```
# Find out number of dimensions in array
df.ndim

# generate equally spaced values within a given interval
np.arange(5, 11, 2)

# Create linearly spaced array
linear_spaced = np.linspace(0, 1, 5)  # 5 values from 0 to 1

# Accessing Array Elements
element = a[2]  # Retrieve the third element of array 'a'
row = reshaped[1, :]  # Retrieve the second row of 'reshaped'

# Boolean indexing
filtered = a[a > 2]  # Elements of 'a' greater than 2

# transpose a NumPy array
a = np.arange(12).reshape((6, 2))
a.transpose()

# sort the array in-place
np.sort(a) ## sort based on rows
np.sort(a, axis=None) ## sort the flattened array
np.sort(a, axis=0) ## sort based on columns

```

# Regular expressions

```
# Replace text
replaced_text = re.sub(r"string", "sentence", text)
print(replaced_text)
```

## Misc scripts

```
# set date to today
from datetime import datetime as dt
date_today = dt.now()

# capitalize text
capitalized_text = text.capitalize()

# generate a GUID
import uuid
guid = uuid.uuid4()

# check for leap year
def is_leap_year(year): return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Convert F to C
celsius = (fahrenheit - 32) * 5/9

# Create progress bar
import time from tqdm
import tqdm
for i in tqdm(range(100)): time.sleep(0.1)

# Get current working directory
import os

cwd = os.getcwd()

# Chain custom functions
result = (
    df.pipe(subtract_federal_tax)
      .pipe(subtract_state_tax, rate=0.12)
      .pipe(
          (subtract_national_insurance, 'df'),
          rate=0.05,
          rate_increase=0.02
      )
)
print(result)

# # Normalize numeric columns
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df[['numeric_column']] = scaler.fit_transform(df[['numeric_column']]

# pretty printing
import pprint
data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
pprint.pprint(data)

# Assign: create a new DataFrame with additional columns, assigning values based on existing columns or operations
df.assign(value_cat=np.where(df["Value"] > 20, "high", "low"))
df.assign(value_cat=np.where(df["Value"] > 20, "high", "low")).groupby(
    "value_cat"
).mean()

# combine_first: choosing values from the first Series and filling in any missing values with the corresponding values from the second Series
s1 = pd.Series([1, 2, np.nan, 4, np.nan, 6])
s2 = pd.Series([10, np.nan, 30, 40, np.nan, 60])

s1.combine_first(s2)

s3 = pd.Series([1, 2, 3, 4, 5, 6])
s1.combine_first(s2).combine_first(s3)

# Sort List based on another List
list1 =  ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
list2 = [ 0, 1, 1, 1, 2, 2, 0, 1, 1, 3, 4]
C = [x for _, x in sorted(zip(list2, list1), key=lambda pair: pair[0])]
print(C) # ['a', 'g', 'b', 'c', 'd', 'h', 'i', 'e', 'f', 'j', 'k']

# Reading lines from a file until an empty line is encountered using walrus
# allows for assignment and return of a value within an expression
with open('myfile.txt') as file:
    while (line := file.readline().rstrip()):
        print(line)

# Lambda functions
# filter
bricks = ["red", "blue", "red", "blue", "red", "blue"]
red_bricks = filter(lambda x: x == 'red', bricks)
print(len(list(bricks)))  # Output: 3

# map
bricks = ["red", "blue", "red", "blue", "red", "blue"]
green_bricks = map(lambda x: "green", bricks)
print(len(list(green_bricks)))  # Output: 6

# Data validation with enums
from enum import Enum

class UserRole(Enum):
    ADMIN = "admin"
    EDITOR = "editor"
    VIEWER = "viewer"

def assign_role(role: UserRole):
    if not isinstance(role, UserRole):
        raise ValueError(f"Invalid role: {role}")
    print(f"Role assigned: {role.name}")
```

# Logging

```
import logging

# Create a logger
logger = logging.getLogger(__name__)

# Set the logging level
logger.setLevel(logging.DEBUG)

# Create a file handler and set the logging level
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)

# Create a console handler and set the logging level
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Example usage
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

# Here’s an example of how to configure logging using a configuration file (logging.conf):

[loggers]
keys=root

[handlers]
keys=consoleHandler,fileHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler,fileHandler

[handler_consoleHandler]
class=StreamHandler
level=INFO
formatter=simpleFormatter
args=(sys.stdout,)

[handler_fileHandler]
class=FileHandler
level=DEBUG
formatter=simpleFormatter
args=('app.log',)

[formatter_simpleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
To use this configuration file in your Python code, you can do the following:

import logging
import logging.config

# Load the logging configuration from the file
logging.config.fileConfig('logging.conf')

# Get the logger
logger = logging.getLogger(__name__)

# Example usage
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
```

# File manipulation

```
from pathlib import Path

# Create a Path object
path = Path('/path/to/directory')

# Access parts of the path
print(path.name)       # 'directory'
print(path.parent)     # '/path/to'
print(path.suffix)     # ''

# Join paths
path = Path('/path/to')
new_path = path / 'directory' / 'file.txt'

# Checking if path exits 
if path.exists():
    print("The file exists")
else:
    print("The file does not exist")

# Reading from a file
path = Path('/path/to/file.txt')
content = path.read_text()
print(content)

# Listing Directory Contents
for file in path.iterdir():
    print(file)
```

# Generators

```
# Computes values only when needed, saving memory and processing time, especially with large datasets
def process_logs(filename):
    with open(filename) as file:
        for line in file:
            if "ERROR" in line:
                yield line

# Using a generator to process logs lazily
for log in process_logs("server.log"):
    print(log)
```