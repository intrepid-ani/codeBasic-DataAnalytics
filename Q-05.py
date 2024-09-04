import pandas as pd

sales_by_states= pd.read_csv(r'files\electric_vehicle_sales_by_state.csv')

# Question-05: How do the EV sales and penetration rates in Delhi compare to Karnataka for 2024


# Filter for the year 2024 and state
fil_date = sales_by_states[
    (sales_by_states['date'] >= '01-01-2024') &
    (sales_by_states['date'] <= '31-12-2024')
]
fil_date= fil_date[
    (fil_date['state']=='Delhi') |
    (fil_date['state']=="Karnataka")]

# Grouping the states in one domain
ev_sold = fil_date.groupby(by='state')['electric_vehicles_sold'].sum().reset_index()
to_sold = fil_date.groupby(by= 'state')['total_vehicles_sold'].sum().reset_index()

# merge ev_sold and to_sold
merge_ = pd.merge(ev_sold, to_sold, on= 'state')
merge_['peneteration'] = merge_["electric_vehicles_sold"]/merge_['total_vehicles_sold'] * 100

# Result
print(merge_)