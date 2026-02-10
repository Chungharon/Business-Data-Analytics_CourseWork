import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('/Users/mac/Desktop/dataAnalysis/milestone1/retail_sales1.csv')

#View basic info
print(df.info())
print(df.head())

df.dropna(subset=['Quantity'])
print(df.columns)
print(df.shape)


# Remove the duplicates on the dataset
df.drop_duplicates(subset=['Customer Name', 'Product'])


# Handle missing values
df['Revenue'].fillna(df['Revenue'].mean(), inplace=True)

# Convert date column
df['Date'] = pd.to_datetime(df['Date'])

# Normalize categorical column
df['Category'] = df['Category'].str.lower()

#Create a new column (feature engineering)
df['Revenue_per_Item'] = df['Revenue'] / df['Quantity']

print(df.describe())
