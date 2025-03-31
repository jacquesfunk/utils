# Load necessary libraries
library(dplyr)
library(readr)

# Read the dataset from a CSV file
df1 <- read_csv("C:/Users/mahmad/OneDrive - Ryan RTS/Downloads/Parameters_20240327.csv")

# Take a random sample of 5000 rows
set.seed(123)  # Set seed for reproducibility
df_sample <- df1 %>% sample_n(5000)

# Write the sampled data to a new CSV file
output_file <- "C:/Users/mahmad/OneDrive - Ryan RTS/Downloads/hubtek20240327sample.csv"
write_csv(df_sample, output_file)

cat("Sampled data saved to", output_file, "\n")