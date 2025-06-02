#  Task 1: Data Cleaning and Preprocessing – Customer Personality Analysis


##  Objective

Clean and prepare the *Customer Personality Analysis* dataset using *Python (Pandas)* in *Google Colab*.  
The task includes handling null values, removing duplicates, standardizing formats, and exporting the cleaned dataset.


##   Dataset Used

- *File:* marketing_campaign.csv  
- *Source:* [Kaggle – Customer Personality Analysis](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis)  
- *Separator:* Tab-separated (\t)

---

##  Steps Performed

1. Load Dataset
import pandas as pd
df = pd.read_csv("marketing_campaign.csv", sep="\t")

2. Missing Value Check

df.isnull().sum()

3. Remove Duplicates & Nulls

df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

4. Standardize Text Columns

df['education'] = df['education'].str.title().str.strip()
df['marital_status'] = df['marital_status'].str.title().str.strip()

5. Convert Dates

df['dt_customer'] = pd.to_datetime(df['dt_customer'], format="%d-%m-%Y")

6. Rename Columns

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

7. Data Type Check

df.dtypes

8. Final Output

Cleaned dataset saved as: cleaned_customer_personality.csv

from google.colab import files  
files.download("cleaned_customer_personality.csv")


#  Summary of Changes

* Missing Values	Checked and dropped rows with nulls
* 	Removed duplicates
* Text Standardization	Cleaned & formatted text (education, marital_status)
* Date Format	Converted dt_customer to datetime format
* Column Names	Renamed to lowercase_with_underscores
* Data Types	Verified and adjusted where needed

#  Tools Used

Python

Pandas

Google Colab

# Author
Boddupalli Charishma
GitHub Profile :https://github.com/Boddupallicharishma
