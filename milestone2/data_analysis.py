import pandas as pd
import numpy as np

# BEGINNER PANDAS PROJECT: EXPENSE TRACKER

print("=" * 60)
print("PERSONAL EXPENSE TRACKER - Pandas Tutorial")
print("=" * 60)

# Create sample expense data
expenses = pd.DataFrame({
    'Date': ['2024-01-01', '2024-01-03', '2024-01-05', '2024-01-07', 
             '2024-01-10', '2024-01-12', '2024-01-15', '2024-01-18',
             '2024-01-20', '2024-01-22', '2024-01-25', '2024-01-28'],
    'Category': ['Food', 'Transport', 'Entertainment', 'Food',
                 'Shopping', 'Food', 'Transport', 'Entertainment',
                 'Food', 'Shopping', 'Transport', 'Food'],
    'Description': ['Grocery shopping', 'Uber ride', 'Movie tickets', 'Restaurant',
                    'New shoes', 'Coffee shop', 'Gas', 'Concert',
                    'Lunch', 'Clothes', 'Taxi', 'Dinner'],
    'Amount': [85.50, 15.00, 25.00, 42.30,
               120.00, 5.50, 45.00, 75.00,
               18.50, 95.00, 12.00, 55.20],
    'Payment_Method': ['Credit Card', 'Cash', 'Credit Card', 'Debit Card',
                       'Credit Card', 'Cash', 'Credit Card', 'Credit Card',
                       'Cash', 'Credit Card', 'Cash', 'Debit Card']
})

print("\n1. ORIGINAL DATA")
print("-" * 60)
print(expenses)

# 2. CONVERT DATE COLUMN TO DATETIME
# -----------------------------------
expenses['Date'] = pd.to_datetime(expenses['Date'])
print("\n2. DATA TYPES")
print("-" * 60)
print(expenses.dtypes)

# 3. BASIC INFORMATION
# --------------------
print("\n3. BASIC DATASET INFO")
print("-" * 60)
print(f"Total number of expenses: {len(expenses)}")
print(f"Date range: {expenses['Date'].min()} to {expenses['Date'].max()}")
print(f"\nColumn names: {list(expenses.columns)}")

# 4. SUMMARY STATISTICS
# ----------------------
print("\n4. SUMMARY STATISTICS")
print("-" * 60)
print(expenses['Amount'].describe())
print(f"\nTotal spent: ${expenses['Amount'].sum():.2f}")
print(f"Average expense: ${expenses['Amount'].mean():.2f}")
print(f"Highest expense: ${expenses['Amount'].max():.2f}")
print(f"Lowest expense: ${expenses['Amount'].min():.2f}")

# 5. GROUP BY CATEGORY
# ---------------------
print("\n5. SPENDING BY CATEGORY")
print("-" * 60)
category_spending = expenses.groupby('Category')['Amount'].agg(['sum', 'mean', 'count'])
category_spending.columns = ['Total', 'Average', 'Count']
category_spending = category_spending.sort_values('Total', ascending=False)
print(category_spending)

# 6. FILTER DATA
# ---------------
print("\n6. FILTERING: Expenses over $50")
print("-" * 60)
expensive_items = expenses[expenses['Amount'] > 50]
print(expensive_items[['Date', 'Description', 'Amount']])

print("\n7. FILTERING: Food expenses only")
print("-" * 60)
food_expenses = expenses[expenses['Category'] == 'Food']
print(food_expenses[['Date', 'Description', 'Amount']])

# 8. ADD NEW COLUMN
# ------------------
print("\n8. ADDING NEW COLUMN: Day of Week")
print("-" * 60)
expenses['Day_of_Week'] = expenses['Date'].dt.day_name() # type: ignore
print(expenses[['Date', 'Day_of_Week', 'Category', 'Amount']])

# 9. PAYMENT METHOD ANALYSIS
# ---------------------------
print("\n9. SPENDING BY PAYMENT METHOD")
print("-" * 60)
payment_summary = expenses.groupby('Payment_Method')['Amount'].sum().sort_values(ascending=False)
print(payment_summary)

# 10. SORTING
# -----------
print("\n10. TOP 5 HIGHEST EXPENSES")
print("-" * 60)
top_expenses = expenses.nlargest(5, 'Amount')[['Date', 'Description', 'Category', 'Amount']]
print(top_expenses)

# 11. CREATE A SUMMARY REPORT
# ----------------------------
print("\n" + "=" * 60)
print("MONTHLY SUMMARY REPORT")
print("=" * 60)

total_spent = expenses['Amount'].sum()
num_transactions = len(expenses)
avg_transaction = expenses['Amount'].mean()

print(f"Total Spent: ${total_spent:.2f}")
print(f"Number of Transactions: {num_transactions}")
print(f"Average Transaction: ${avg_transaction:.2f}")
print(f"\nMost Expensive Category: {category_spending.index[0]} (${category_spending['Total'].iloc[0]:.2f})")
print(f"Most Frequent Category: {expenses['Category'].value_counts().index[0]} ({expenses['Category'].value_counts().iloc[0]} times)")

# 12. FILE TO CSV (OPTIONAL)
# ---------------------------

expenses.to_csv('my_expenses.csv', index=False)
print("\n✓ Data saved to 'my_expenses.csv'")

print("\n" + "=" * 60)
print("PROJECT COMPLETE!")
print("=" * 60)


# print("\n\nTRY THESE EXERCISES:")
# print("-" * 60)
# print("1. Add more expense entries to the DataFrame")
# print("2. Filter expenses by a specific date range")
# print("3. Calculate what percentage of total spending each category represents")
# print("4. Find the day of the week you spend the most money")
# print("5. Create a new column for 'Budget_Category' (Under/Over budget)")
# print("6. Calculate cumulative spending over time")


