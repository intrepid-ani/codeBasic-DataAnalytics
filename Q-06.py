import pandas as pd

# Load the dataset
sales_by_makers = pd.read_csv(r'files\electric_vehicle_sales_by_makers.csv')

# List down the compounded annual growth rate (CAGR) in 4-wheeler units for the top 5 makers from 2022 to 2024

# Convert the date column to datetime format
sales_by_makers['date'] = pd.to_datetime(sales_by_makers['date'], format="%d-%b-%y", errors="coerce")

# Filter data by date & vehicle category for 2022 and 2024
date_filter_22 = sales_by_makers[
    (sales_by_makers['date'] <= "2022-12-31") &
    (sales_by_makers['date'] >= "2022-01-01") &
    (sales_by_makers['vehicle_category'] == "4-Wheelers")
]

date_filter_24 = sales_by_makers[
    (sales_by_makers['date'] <= "2024-12-31") &
    (sales_by_makers['date'] >= "2024-01-01") &
    (sales_by_makers['vehicle_category'] == "4-Wheelers")
]

# Group data by 'maker' and sum the 'electric_vehicles_sold'
group_22 = date_filter_22.groupby(by='maker')['electric_vehicles_sold'].sum().reset_index()
group_24 = date_filter_24.groupby(by='maker')['electric_vehicles_sold'].sum().reset_index()

# Merge the 2022 and 2024 data on 'maker'
merge_grp_22_24 = pd.merge(group_22, group_24, on='maker', suffixes=["_22", "_24"]).reset_index()

# Calculate the CAGR
merge_grp_22_24['CAGR'] = (merge_grp_22_24['electric_vehicles_sold_24'] / merge_grp_22_24['electric_vehicles_sold_22']) ** (1/2) - 1

# Sort by CAGR and get the top 5 makers
top_5_cagr = merge_grp_22_24.sort_values(by='CAGR', ascending=False).head(5)

# Result
print(top_5_cagr[['maker', 'electric_vehicles_sold_22', 'electric_vehicles_sold_24', 'CAGR']])
print(merge_grp_22_24.sort_values(by='CAGR', ascending=False).head(6).iloc[1:6])#Since the PCA Automobiles CAGR is infinit