import pandas as pd

makers= pd.read_csv(r'files\electric_vehicle_sales_by_makers.csv')

makers['date'] = pd.to_datetime(makers['date'], format= '%d-%b-%y', errors= 'coerce')
makers['year'] = makers['date'].dt.year

print(makers)
