import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.dates as mdates

def generate_sales_chart():
    # Sample January sales data 
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    # Sample sales data for 2023
    sales_2023 = [45000, 52000, 48000, 61000, 58000, 67000,
                  72000, 69000, 75000, 82000, 78000, 85000]
    
    # Sample sales data for 2024
    sales_2024 = [48000, 55000, 51000, 65000, 62000, 71000,
                  76000, 73000, 79000, 86000, 82000, 89000]
    
    # Create figure and axis
    plt.figure(figsize=(12, 8))
    ax = plt.gca()
    
    # Plot lines for both years
    plt.plot(months, sales_2023, marker='o', linewidth=2, 
             label='2023', color='#2E86AB', markersize=6)
    plt.plot(months, sales_2024, marker='s', linewidth=2, 
             label='2024', color='#A23B72', markersize=6)
    
    # Customize the chart
    plt.title('Monthly Sales Trends', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Month', fontsize=12, fontweight='bold')
    plt.ylabel('Sales ($)', fontsize=12, fontweight='bold')
    
    # Format y-axis to show currency
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}')) # pyright: ignore[reportPrivateImportUsage]
    
    # Add grid
    plt.grid(True, alpha=0.3, linestyle='--')
    
    # Add legend
    plt.legend(fontsize=11, loc='upper left')
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)
    
    # Add data labels on points
    for i, (v2023, v2024) in enumerate(zip(sales_2023, sales_2024)):
        plt.annotate(f'${v2023:,}', (i, v2023), textcoords="offset points", 
                    xytext=(0,10), ha='center', fontsize=8, color='#2E86AB')
        plt.annotate(f'${v2024:,}', (i, v2024), textcoords="offset points", 
                    xytext=(0,-15), ha='center', fontsize=8, color='#A23B72')
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    
    # Save the chart
    plt.savefig('monthly_sales_trends.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    # Print summary statistics
    print("Sales Summary:")
    print(f"2023 Total Sales: ${sum(sales_2023):,.0f}")
    print(f"2024 Total Sales: ${sum(sales_2024):,.0f}")
    print(f"2024 Growth: {((sum(sales_2024) - sum(sales_2023)) / sum(sales_2023) * 100):.1f}%")

def generate_single_year_chart(year=2024, sales_data=None):
    """Generate chart for a single year"""
    if sales_data is None:
        # Generate random sample data if none provided
        np.random.seed(42)
        sales_data = np.random.randint(40000, 90000, 12)
    
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    plt.figure(figsize=(10, 6))
    plt.plot(months, sales_data, marker='o', linewidth=3, 
             color='#FF6B6B', markersize=8, markerfacecolor='white', 
             markeredgewidth=2, markeredgecolor='#FF6B6B')
    
    # Fill area under the line
    plt.fill_between(months, sales_data, alpha=0.3, color='#FF6B6B')
    
    plt.title(f'Monthly Sales Trends - {year}', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Month', fontsize=12, fontweight='bold')
    plt.ylabel('Sales ($)', fontsize=12, fontweight='bold')
    
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}')) # pyright: ignore[reportPrivateImportUsage]
    plt.grid(True, alpha=0.3, linestyle='--')
    plt.xticks(rotation=45)
    
    # Add trend line
    z = np.polyfit(range(12), sales_data, 1)
    p = np.poly1d(z)
    plt.plot(months, p(range(12)), "--", color='#333333', alpha=0.7, 
             label=f'Trend: {"↑" if z[0] > 0 else "↓"} ${abs(z[0]):,.0f}/month')
    
    plt.legend(fontsize=11)
    plt.tight_layout()
    plt.savefig(f'sales_trends_{year}.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    # Generate comparison chart (2023 vs 2024)
    generate_sales_chart()
    
    # Generate single year chart
    generate_single_year_chart()