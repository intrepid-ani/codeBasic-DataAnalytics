import pandas as pd

dim_date= pd.read_csv(r'files\dim_date.csv')
sales_by_makers= pd.read_csv(r'files\electric_vehicle_sales_by_makers.csv')

# Question-04: What are the quarterly trends based on sales volume for the top 5 EV makers (4-wheelers) from 2022 to 2024

# Convert the 'date' column to datetime format
dim_date['date'] = pd.to_datetime(dim_date['date'], format='%d-%b-%y')
sales_by_makers['date'] = pd.to_datetime(sales_by_makers['date'], format='%d-%b-%y')

# Filter the sales_by_makers data for 4-wheelers and years 2022 to 2024
filtered_sales = sales_by_makers[
    (sales_by_makers['vehicle_category'] == '4-Wheelers') & 
    (sales_by_makers['date'].dt.year >= 2022) & 
    (sales_by_makers['date'].dt.year <= 2024)
]

# Merge the filtered sales data with the dim_date data to include quarter information
merged_data = pd.merge(filtered_sales, dim_date, on='date', how='left')

# Aggregate sales data by fiscal year, quarter, and maker
quarterly_sales = merged_data.groupby(['fiscal_year', 'quarter', 'maker']).agg(
    {'electric_vehicles_sold': 'sum'}).reset_index()

# Calculate the total sales per maker over the period 2022-2024
total_sales_per_maker = quarterly_sales.groupby('maker')['electric_vehicles_sold'].sum().reset_index()

# Identify the top 5 makers based on total sales
top_5_makers = total_sales_per_maker.nlargest(5, 'electric_vehicles_sold')['maker']

# Filter the quarterly sales data for only the top 5 makers
top_5_sales_data = quarterly_sales[quarterly_sales['maker'].isin(top_5_makers)].sort_values(
    by=['fiscal_year', 'quarter'])

print(top_5_sales_data)