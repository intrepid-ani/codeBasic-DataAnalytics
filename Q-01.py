import pandas as pd

sales_by_makers= pd.read_csv(r'files\electric_vehicle_sales_by_makers.csv')

# Question-01: List the top 3 and bottom 3 makers for the fiscal years 2023 and 2024 in terms of the number of 2-wheelers sold.

# formating the date from '01-Jan-2024' to '01-01-2024
sales_by_makers["date"] =pd.to_datetime(sales_by_makers["date"], format= "%d-%b-%y", errors="coerce")

# filtering date for year 2023 and vehicles_category 2-Wheelers 
fy2023 = sales_by_makers[
    (sales_by_makers['date']<="31-12-2023")&
    (sales_by_makers["date"]>="01-01-2023")&
    (sales_by_makers['vehicle_category']=="2-Wheelers")
]

# filtering date for year 2024 and vehicles_category 2-Wheelers
fy2024 = sales_by_makers[
    (sales_by_makers['date']<="31-12-2024")&
    (sales_by_makers["date"]>="01-01-2024")&
    (sales_by_makers['vehicle_category']=="2-Wheelers")
]

# grouping rows by makers name for the year 2023
grp_23 = fy2023.groupby(by="maker")['electric_vehicles_sold'].sum()
res_23 = grp_23.sort_values(ascending=False)

# grouping rows by makers name for the year 2023
grp_24 = fy2024.groupby(by= 'maker')['electric_vehicles_sold'].sum()
res_24 = grp_24.sort_values(ascending= False)

# Printing the result
print("Top 3 makers in the year 2023: \n",res_23.head(3),'\n Bottom 3 makers in the year 2023: ', res_23.tail(3))
print("\n\nTop 3 makers in the year 2024: \n",res_24.head(3),'\n Bottom 3 makers in the year 2024: ', res_24.tail(3))

