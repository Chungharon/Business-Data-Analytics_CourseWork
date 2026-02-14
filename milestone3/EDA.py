# # # Import required libraries
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # # Exercise 2: Plot histograms of sales and customer ratings
# # plt.figure(figsize=(14, 5))

# # # plt.subplot(1, 2, 1)
# # # sns.histplot(df['MonthlySales(Kshs)'], bins=5, kde=True, color='skyblue')
# # # plt.title('Histogram of Monthly Sales (Kshs)')
# # # plt.xlabel('Monthly Sales (Kshs)')
# # # plt.ylabel('Frequency')

# # # Here's a complete Python (Jupyter Notebook) code using pandas, matplotlib, and seaborn to perform the following:

# # #     Exercise 2: Plot histograms of Sales and Customer Ratings

# # #     Exercise 3: Create scatter plots between Ad Budget and Monthly Sales

# # #     Exercise 4: Generate a box plot to assess sales distribution across branches





# sns.histplot(data=df, x='Customer_Rating', bins=5, kde=True, color='salmon')
# plt.title('Histogram of Customer Ratings')
# plt.xlabel('Customer Rating')
# plt.ylabel('Frequency')

# # plt.tight_layout()
# # plt.show()

# # # # Exercise 3: Create scatter plot between Ad Budget and Monthly Sales
# # # plt.figure(figsize=(8, 6))
# # # sns.scatterplot(data=df, x='Ad Budget (Kshs)', y='Monthly Sales (Kshs)', hue='Branch', palette='tab10', s=100)
# # # plt.title('Ad Budget vs Monthly Sales')
# # # plt.xlabel('Ad Budget (Kshs)')
# # # plt.ylabel('Monthly Sales (Kshs)')
# # # plt.grid(True)
# # # plt.show()

# # # Notes:

# # #     You can replace the sample data with your actual dataset by importing it using pd.read_csv("your_file.csv").

# # #     All plots use seaborn for cleaner aesthetics, with matplotlib managing layout and display.

# # # Exercise 4: Box plot to assess sales distribution across branches
# # plt.figure(figsize=(10, 6))
# # sns.boxplot(x='Branch', y='Monthly Sales (Kshs)', data=df, palette='pastel')
# # plt.title('Sales Distribution Across Branches')
# # plt.xlabel('Branch')
# # plt.ylabel('Monthly Sales (Kshs)')
# # plt.grid(True, axis='y')
# # plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('retail_sales1.csv')
print(df.info())
print(df.head())
plt.subplot(1, 2, 2)

mean_sales = df['Sales'].mean()
median_sales = df['Sales'].median()
mode_sales = df['Sales'].mode()
print(mean_sales)
print(median_sales)
print(mode_sales)

print(df.describe())

# # # Exercise 2: Plot histograms of Sales and Customer Ratings
sns.barplot(x='Product', y='Quantity', data=df)
plt.show()
