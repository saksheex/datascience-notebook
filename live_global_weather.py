import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('/Users/sakshee/Downloads/GlobalWeatherRepository.csv')

pd.set_option('display.float_format', '{:.2f}'.format)  # now it will show the value to 2 decimal place
print(df['country'].unique())   # shows all unique country names
print(df['country'].nunique())  # shows total COUNT of unique countries
print(df.head())
print(df.tail())
print(df.shape)  # gives rows count of a column
print(df.dtypes)      # column names + their data types
print(df.columns.tolist())  # column names as a clean Python list
print(df.isnull().sum().sort_values())   # find missing → count them → sort them

print("-" * 40)
cols_to_drop = ['latitude', 'longitude', 'last_updated_epoch']
print(f" your minimun is \n {df.select_dtypes(include='number').drop(columns=cols_to_drop).min()}")
print(f" your maximun is \n {df.select_dtypes(include='number').drop(columns=cols_to_drop).max()}")
print(f" your mean is \n {df.select_dtypes(include='number').drop(columns=cols_to_drop).mean()}")

print ("*" * 80)
countries = ['India', 'USA', 'Canada']   # your 3 countries
yours = df[df['country'].isin(countries)]  
cols = ['country', 'location_name', 'temperature_celsius', 
        'humidity', 'wind_kph', 'condition_text']

print(yours[cols])

avg_temp = df.groupby('country')['temperature_celsius'].mean()

print("Hottest Countries", avg_temp.nlargest(10))
print("Coldest Countries" , avg_temp.nsmallest(10))
