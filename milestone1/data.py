# Objective: Practice data cleaning and transformation using a real-world dataset.    Tools: Python, Jupyter Notebook, Pandas, NumPy     
# Dataset Example: Retail sales CSV with missing values, inconsistent formats, and duplicates

# Real-World Applications

# Healthcare – AMREF
# Challenge: Mismatched formats in maternal health data across clinics.
# Solution: Standardized data formats and transformed fields for mobile health analytics.
# Impact: Supported better maternal health monitoring and reporting.

import pandas as pd
import numpy as np
import dash
from dash import dcc, html
import plotly.express as px

# Load the dataset
df = pd.read_csv('Sales_Data1.csv')

# #View basic info
# print(df.info())
# print(df.head())

# df.dropna(subset=['Sales'])
# print(df.columns)
# print(df.shape)


# np.random.seed(47)

# dates = pd.date_range(start="2024-01-01", end="2024-12-31", freq="D")
# regions = ["East", "West", "North", "South"]
# products = ["Laptop", "Phone", "Tablet", "Accessory"]

# data = pd.DataFrame({
#     "Date": np.random.choice(dates, 1000),
#     "Region": np.random.choice(regions, 1000),
#     "Product": np.random.choice(products, 1000),
#     "Sales": np.random.randint(100, 2000, 1000),
#     "Quantity": np.random.randint(1, 10, 1000)
# })

# data["Month"] = pd.to_datetime(data["Date"]).dt.to_period("M").astype(str)


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
import micropip
async def install_deps():
    await micropip.install('dash-canvas')

import asyncio
asyncio.run(install_deps())
from dash import Dash, html
from dash_canvas import DashCanvas

app = Dash(__name__)
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    html.H5('Press down the left mouse button and draw inside the canvas'),
    DashCanvas(id='canvas_101')
    ])


if __name__ == '__main__':
    app.run(debug=True)



