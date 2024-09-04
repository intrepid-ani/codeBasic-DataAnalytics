import pandas as pd

sales_by_states= pd.read_csv(r"C:\Users\IntrepidAni\Desktop\Coding\Python And AI\PanDas\CodeBasics Data Analysis\electric_vehicle_sales_by_state.csv")

sales_by_states['date'] = pd.to_datetime(sales_by_states['date'], format = "%d-%b-%y", errors='coerce')
sales_by_states['month'] = sales_by_states['date'].dt.month

# Question-08: What are the peak and low season months for EV sales based on the data from 2022 to 2024

date_filter= sales_by_states[
    (sales_by_states['date']>='01-01-2022')&
    (sales_by_states['date']<='31-12-2024')
]

grp= date_filter.groupby(by= 'month')['electric_vehicles_sold'].sum().reset_index()

low= grp.sort_values(by='electric_vehicles_sold').head(1)

peak = grp.sort_values(by='electric_vehicles_sold', ascending= False).head(1)
print(peak)
print(low)
