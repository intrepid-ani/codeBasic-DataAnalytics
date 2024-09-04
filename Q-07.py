import pandas as pd

sales_by_states = pd.read_csv(r'files\electric_vehicle_sales_by_state.csv')

sales_by_states['date'] = pd.to_datetime(sales_by_states['date'], format= '%d-%b-%y', errors='coerce')
#Question-07: List down the top 10 states that had the highest compounded annual growth rate (CAGR) from 2022 to 2024 in total vehicles sold.

# filter the date 
fil_22 = sales_by_states[
    (sales_by_states['date']<= '31-12-2022')&
    (sales_by_states['date']>= '01-01-2022')]
fil_24 = sales_by_states[
    (sales_by_states['date']<= '31-12-2024')&
    (sales_by_states['date']>= '01-01-2024')]

# group states
grp_22= fil_22.groupby(by='state')['total_vehicles_sold'].sum()
grp_24= fil_24.groupby(by='state')['total_vehicles_sold'].sum()

# merge 
merge= pd.merge(grp_22, grp_24, on='state', suffixes=['_22','_24'])
merge["CAGR"] = (merge['total_vehicles_sold_24']/merge['total_vehicles_sold_22'])**(1/2) -1

# result
print(merge.sort_values(by = 'CAGR', ascending= False).tail(10))