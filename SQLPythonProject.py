import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------
# Load Data
# ------------------------

df= pd.read_csv("data/SQL_dataset_export.csv")

# ----------------------------------------
# Average Net Revenue per Product Line
# ----------------------------------------
avg_revenue = df.groupby('product_line')['net_revenue'].mean().sort_values(ascending=False).reset_index()

plt.figure(figsize=(8,6))
sns.barplot(
    data=avg_revenue,
    x='product_line',
    y='net_revenue',
    hue='product_line',        
    dodge=False,               
    palette="tab10",         
    legend=False               
)

plt.title('Average Net Revenue per Product Line')
plt.ylabel('Average Net Revenue')
plt.xlabel('Product Line')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/avg_revenue_product_line.png", dpi=300)
plt.show()

# ----------------------------------------
# Total Net Revenue per Product Line
# ----------------------------------------
total_revenue = df.groupby('product_line')['net_revenue'].sum().sort_values(ascending=False).reset_index()

sns.barplot(
    data=total_revenue,
    x='product_line',
    y='net_revenue',
    hue='product_line',       
    dodge=False,              
    palette="Set2",           
    legend=False           
)

plt.title("Total Net Revenue per Product Line")
plt.ylabel("Total Net Revenue")
plt.xlabel("Product Line")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/total_revenue_product_line.png", dpi=300)
plt.show()
# ----------------------------------------------------------------
# Average and Total Net Revenue per Product Line (Stacked Columns)
# ----------------------------------------------------------------

# Aggregate
total_revenue = df.groupby('product_line')['net_revenue'].sum().reset_index()
avg_revenue = df.groupby('product_line')['net_revenue'].mean().reset_index()

# Merge totals and averages
revenue_combined = total_revenue.merge(avg_revenue, on='product_line')
revenue_combined.rename(columns={'net_revenue_x':'total_revenue', 'net_revenue_y':'average_revenue'}, inplace=True)

# Plot stacked bar chart
plt.figure(figsize=(10,6))

# Bottom: average revenue
plt.bar(revenue_combined['product_line'], revenue_combined['average_revenue'], color='skyblue', label='Average Revenue')

# Top: total revenue minus average to avoid double counting
plt.bar(
    revenue_combined['product_line'],
    revenue_combined['total_revenue'] - revenue_combined['average_revenue'],
    bottom=revenue_combined['average_revenue'],
    color='lightgreen',
    label='Total Revenue'
)

plt.title('Total and Average Net Revenue per Product Line')
plt.xlabel('Product Line')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig("images/stacked_revenue.png", dpi=300)
plt.show()

# ----------------------------------------
# Monthly Total Revenue per Product Line
# ----------------------------------------
monthly_total = df.groupby(['month', 'product_line'])['net_revenue'].sum().reset_index()

plt.figure(figsize=(10,6))
sns.lineplot(
    data=monthly_total,
    x='month',
    y='net_revenue',
    hue='product_line',
    marker='o'
)
plt.title('Monthly Total Net Revenue by Product Line')
plt.ylabel('Total Net Revenue')
plt.xlabel('Month')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/monthly_product_linechart.png", dpi=300)
plt.show()

# Using subplots per product line

sns.relplot(
    data=monthly_total,
    x='month',
    y='net_revenue',
    col='product_line',
    kind='line',
    marker='o',
    col_wrap=3,
    height=4,
    aspect=1.2
)
plt.subplots_adjust(top=0.9)
plt.suptitle("Monthly Total Net Revenue Trends by Product Line", fontsize=16)
plt.savefig("images/monthly_product_line_subplots.png", dpi=300)
plt.show()


# ----------------------------------------
# Monthly Total Revenue per Warehouse
# ----------------------------------------
monthly_warehouse = df.groupby(['month', 'warehouse'])['net_revenue'].sum().reset_index()

# Line chart with all warehouses

plt.figure(figsize=(12,6))
sns.lineplot(
    data=monthly_warehouse,
    x='month',
    y='net_revenue',
    hue='warehouse',
    marker='o'
)
plt.title('Monthly Total Net Revenue by Warehouse')
plt.ylabel('Total Net Revenue')
plt.xlabel('Month')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/monthly_warehouse.png", dpi=300)
plt.show()

