import pandas as pd

# Load the dataset
file_path = r'C:\Users\IntrepidAni\Desktop\Coding\Code basic resume project\files\electric_vehicle_sales_by_state.csv'
df = pd.read_csv(file_path)

# Convert the 'date' column to datetime format and extract the year
df['date'] = pd.to_datetime(df['date'], format='%d-%b-%y')
df['year'] = df['date'].dt.year

# Group by 'state' and 'year', summing up electric and total vehicles sold
state_yearly_sales = df.groupby(['state', 'year']).agg({
    'electric_vehicles_sold': 'sum',
    'total_vehicles_sold': 'sum'
}).reset_index()

# Calculate penetration rate
state_yearly_sales['penetration_rate'] = state_yearly_sales['electric_vehicles_sold'] / state_yearly_sales['total_vehicles_sold']

# Function to calculate CAGR
def calculate_cagr(start_value, end_value, periods):
    if start_value == 0 or periods == 0:
        return None
    return (end_value / start_value) ** (1 / periods) - 1

# Calculate CAGR for each state
cagr_list = []
for state in state_yearly_sales['state'].unique():
    state_data = state_yearly_sales[state_yearly_sales['state'] == state]
    start_year = state_data['year'].min()
    end_year = state_data['year'].max()
    start_sales = state_data[state_data['year'] == start_year]['electric_vehicles_sold'].sum()
    end_sales = state_data[state_data['year'] == end_year]['electric_vehicles_sold'].sum()
    cagr = calculate_cagr(start_sales, end_sales, end_year - start_year)
    cagr_list.append((state, cagr))

# Create a DataFrame for CAGR values
cagr_df = pd.DataFrame(cagr_list, columns=['state', 'cagr']).dropna()

# Merge CAGR data with the state_yearly_sales data
state_sales_with_cagr = pd.merge(state_yearly_sales, cagr_df, on='state')

# Project the sales for 2030 using the CAGR
state_sales_with_cagr['projected_2030_sales'] = state_sales_with_cagr.apply(
    lambda row: row['electric_vehicles_sold'] * (1 + row['cagr']) ** (2030 - row['year']) if row['cagr'] is not None else None, axis=1
)

# Get the latest penetration rate for each state
latest_penetration = state_sales_with_cagr.sort_values('year').groupby('state').tail(1)[['state', 'penetration_rate']]
latest_penetration.rename(columns={'penetration_rate': 'latest_penetration'}, inplace=True)

# Merge the latest penetration rate with the state sales data
state_sales_with_cagr = pd.merge(state_sales_with_cagr, latest_penetration, on='state')

# Sort by penetration rate and select the top 10 states
top_10_states = state_sales_with_cagr.groupby('state').agg({
    'cagr': 'first',
    'latest_penetration': 'first',
    'projected_2030_sales': 'first'
}).sort_values(by='latest_penetration', ascending=False).head(10)

# Reset index for the final output
top_10_projection = top_10_states.reset_index()

print(top_10_projection)
