# Objective: Practice data cleaning and transformation using a real-world dataset.    Tools: Python, Jupyter Notebook, Pandas, NumPy     
# Dataset Example: Retail sales CSV with missing values, inconsistent formats, and duplicates

# Real-World Applications

# Healthcare – AMREF
# Challenge: Mismatched formats in maternal health data across clinics.
# Solution: Standardized data formats and transformed fields for mobile health analytics.
# Impact: Supported better maternal health monitoring and reporting.

import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('retail_sales1.csv')

# #View basic info
# print(df.info())
# print(df.head())

df.dropna(subset=['Quantity'])
print(df.columns)
print(df.shape)


# # Remove the duplicates on the dataset
# df.drop_duplicates(subset=['Customer Name', 'Product'])


# # Handle missing values
# df['Revenue'].fillna(df['Revenue'].mean(), inplace=True)

# # Convert date column
# df['Date'] = pd.to_datetime(df['Date'])

# # Normalize categorical column
# df['Category'] = df['Category'].str.lower()

# #Create a new column (feature engineering)
# df['Revenue_per_Item'] = df['Revenue'] / df['Quantity']


