import pandas as pd

sales_by_states= pd.read_csv(r'files\electric_vehicle_sales_by_state.csv')

# Question-02: Identify the top 5 states with the highest penetration rate in 2-wheeler and 4-wheeler EV sales in FY 2024

# formating the date from '01-Jan-2024' to '01-01-2024
sales_by_states['date'] = pd.to_datetime(sales_by_states['date'], format="%d-%b-%y", errors = "coerce")

# filtering data on the bases of date 
date_filter= sales_by_states[
    (sales_by_states['date'] <= "31-12-2024")&
    (sales_by_states['date'] >= "01-01-2024")
]

# For 2-Wheelers
two_wheelers = date_filter[(date_filter["vehicle_category"] == "2-Wheelers")].copy()
print(two_wheelers)
State_ev = two_wheelers.groupby(by='state')['electric_vehicles_sold'].sum()
State_to = two_wheelers.groupby(by='state')['total_vehicles_sold'].sum()
merge_ev_to_23 = pd.merge(State_ev, State_to, on='state')
merge_ev_to_23['peneteration'] = merge_ev_to_23['electric_vehicles_sold']/merge_ev_to_23['total_vehicles_sold']*100

# For 4-Wheelers
four_wheelers = date_filter[(date_filter["vehicle_category"] == "4-Wheelers")]
State_ev = four_wheelers.groupby(by='state')['electric_vehicles_sold'].sum()
State_to = four_wheelers.groupby(by='state')['total_vehicles_sold'].sum()
merge_ev_to_24 = pd.merge(State_ev, State_to, on='state')
merge_ev_to_24['peneteration'] = merge_ev_to_24['electric_vehicles_sold']/merge_ev_to_24['total_vehicles_sold']*100

# Print result
print("The States with highest peneteration rate in 2024 for 2_Wheelers are:")
print(merge_ev_to_23.sort_values(by= 'peneteration', ascending= False).head(5))

print("The States with highest peneteration rate in 2024 for 4_Wheelers are:")
print(merge_ev_to_24.sort_values(by='peneteration', ascending= False).head(5))