
# Step 1: Import libraries
import pandas as pd
import numpy as np

# Step 2: Load the dataset (tab-separated file from Kaggle)
df = pd.read_csv("marketing_campaign.csv", sep="\t")
print("Original shape:", df.shape)

# Step 3: Basic exploration
print(df.info())
print(df.describe())

# Step 4: Check for missing values
print("Missing values:\n", df.isnull().sum())

# Drop rows with missing values (or use fillna if preferred)
df = df.dropna()

# Step 5: Check and drop duplicates
print("Duplicates:", df.duplicated().sum())
df = df.drop_duplicates()

# Step 6: Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
print("Cleaned columns:\n", df.columns)

# Step 7: Convert data types
df['dt_customer'] = pd.to_datetime(df['dt_customer'], format="%d-%m-%Y")
df['income'] = pd.to_numeric(df['income'], errors='coerce')
df['year_birth'] = df['year_birth'].astype(int)

# Step 8: Standardize text values
df['education'] = df['education'].str.title().str.strip()
df['marital_status'] = df['marital_status'].str.title().str.strip()

# Step 9: Save cleaned dataset
df.to_csv("cleaned_customer_personality.csv", index=False)

# Step 10: Download the CSV file (Google Colab only)
from google.colab import files
files.download("cleaned_customer_personality.csv")
