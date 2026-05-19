import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data={
    "Date": [
        "2026-01-01","2026-01-15",
        "2026-02-01","2026-02-10",
        "2026-03-05","2026-03-20"
    ],
    "Product":['Laptop','Tablet','Headphones','Camera','Monitor','Printer'],
    "Category":['Electronics','Electronics','Audio','Electronics','Electronics','Office'],
    "Price":[35000,15000,4000,20000,12000,5000],
    "Quantity": [1,10,5,2,20,1]
} 

df=pd.DataFrame(data)
#Total Sales Calculation
df['Total Sales']=df['Price']*df['Quantity']
#Total Sales by Category
sales_by_category=df.groupby('Category')['Total Sales'].sum()
print("\nSales by Category:\n")
print(sales_by_category)
#Total Sales by Product
sales_by_product=df.groupby('Product')['Total Sales'].sum()
print("\nSales by Product:\n")
print(sales_by_product)
#Calculating Average Sales per Day
df['Date']=pd.to_datetime(df['Date'])
print(df)
#Calculating total revenue per day
daily_sales=df.groupby('Date')['Total Sales'].sum()
print('Daily Sales:\n',daily_sales)
#Calculating average sales per day
average_sales_per_day=daily_sales.mean()
print("Average Sales per Day:", average_sales_per_day)

#Plotting Monthly Sales Trend
df['Date'] = pd.to_datetime(df['Date'])

monthly_sales = df.groupby(df['Date'].dt.to_period('M'))['Total Sales'].sum()

monthly_sales = monthly_sales.sort_index()

monthly_sales.plot(kind='line', marker='o',color='orange',linewidth=2)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.show()


