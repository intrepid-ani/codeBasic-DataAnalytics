import pandas as pd

# Load the dataset
sales_by_states = pd.read_csv(r'files\electric_vehicle_sales_by_state.csv')

# List the states with negative penetration (decline) in EV sales from 2022 to 2024

# Format the date
sales_by_states['date'] = pd.to_datetime(sales_by_states['date'], format="%d-%b-%Y", errors="coerce")

# Penetration rate of Year 2022

# filter the data on the bases of date
fil_set_22 = sales_by_states[
    (sales_by_states['date'] <= '2022-12-31') & 
    (sales_by_states['date'] >= '2022-01-01')
]

# group data ['electric_vehicles_sold']
group_ev_22 = fil_set_22.groupby(by='state')['electric_vehicles_sold'].sum().reset_index()

# group data ['total_vehicles_sold']
group_to_22 = fil_set_22.groupby(by='state')['total_vehicles_sold'].sum().reset_index()

# merging total and electric sales columns
merge_22 = pd.merge(group_ev_22, group_to_22, on='state')

# Find the penetration for year 2022
merge_22['penetration_22'] = merge_22['electric_vehicles_sold'] / merge_22['total_vehicles_sold'] * 100


# Penetration rate of Year 2024

# filter the data on the bases of date
fil_set_24 = sales_by_states[
    (sales_by_states['date'] <= '2024-12-31') & 
    (sales_by_states['date'] >= '2024-01-01')]
print(fil_set_24)

# group data ['electric_vehicles_sold']
group_ev_24 = fil_set_24.groupby(by='state')['electric_vehicles_sold'].sum().reset_index()

# group data ['total_vehicles_sold']
group_to_24 = fil_set_24.groupby(by='state')['total_vehicles_sold'].sum().reset_index()

# merging total and electric sales columns
merge_24 = pd.merge(group_ev_24, group_to_24, on='state')

# Find the penetration for year 2024
merge_24['penetration_24'] = merge_24['electric_vehicles_sold'] / merge_24['total_vehicles_sold'] * 100

# Merge 2022 and 2024 data on 'state'
merge_22_24 = pd.merge(merge_22, merge_24, on='state', suffixes=('_22', '_24'))

# Calculate the difference in penetration rates
merge_22_24['difference_p22_p24'] = merge_22_24['penetration_24'] - merge_22_24['penetration_22']

# Filter states with a decline in penetration rate
decline_states = merge_22_24[merge_22_24['difference_p22_p24'] < 0]

print(decline_states[['state', 'penetration_22', 'penetration_24', 'difference_p22_p24']])