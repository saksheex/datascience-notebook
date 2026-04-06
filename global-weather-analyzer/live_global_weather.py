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

#average temperature,humidity and wind speed
# print(f" Average temperature of countries in celcius,\n{df.groupby('country')['temperature_celsius'].mean()}")
# print(f" Average humidity of countries ,\n{df.groupby('country')['humidity'].mean()}")
# print(f" Average wind speed of countries ,\n{df.groupby('country')['wind_kph'].mean()}")

print(df.groupby('country')[['temperature_celsius','humidity','wind_kph']].mean())

# PLACES WHERE TEMP AND FEELS LIKE DIFFER THE MOST

df['temp_diff'] = np.abs(df['temperature_celsius'] - df['feels_like_celsius'])
print("PLACES WHERE TEMP AND FEELS LIKE DIFFER THE MOST")
print(df[['country', 'location_name', 'temperature_celsius', 
          'feels_like_celsius', 'temp_diff']].nlargest(10, 'temp_diff'))

# Day length

print(df[['sunrise','sunset']].head())
df['sunrise'] = pd.to_datetime(df['sunrise'])
df['sunset']  = pd.to_datetime(df['sunset'])

df['day_length'] = df['sunset'] - df['sunrise']

print("DAY LENGTH PER CITY")
print(df[['country', 'location_name', 
          'sunrise', 'sunset', 'day_length']].head(10))

# common weather condition
print(f" Most common weather condition ,\n {df['condition_text'].value_counts()}")

# air_quality_PM2.5
# print(df['air_quality_PM2.5'].head())

print(df.nlargest(10,'air_quality_PM2.5')[['country', 'location_name', 'air_quality_PM2.5']])

# common wind direction
# print(df['wind_direction'].head())

print(f" Most common wind directions ,\n {df['wind_direction'].value_counts()}")

df['temp_category'] = np.where(df['temperature_celsius'] > 30, 'Hot',
                        np.where(df['temperature_celsius'] >= 15, 'Mild',
                            'Cold'))

print(df[['country', 'location_name', 
          'temperature_celsius', 'temp_category']].value_counts())

# Graph of 10 hottest country

avg_temp = df.groupby('country')['temperature_celsius'].mean()
top10 = avg_temp.nlargest(10)

plt.bar(top10.index, top10.values)
plt.title("Top 10 Hottest Countries")
plt.xlabel("Country")
plt.ylabel("Average Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Coldest countries
avg_temp = df.groupby('country')['temperature_celsius'].mean()
top10 = avg_temp.nsmallest(10)

plt.bar(top10.index, top10.values)
plt.title("Top 10 Coldest Countries")
plt.xlabel("Country")
plt.ylabel("Average Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# temperature vs feels_like
data = df[df['country'] == 'Turkey']
cities = data['location_name']
temp = data['temperature_celsius']
feels_like = data['feels_like_celsius']
plt.plot(cities, temp,  label='temp')                # first line
plt.plot(cities, feels_like, label='feels_like')      # second line
plt.legend()
plt.title('Temperature v/s Feels_like')
plt.xlabel('Temperaure in C')
plt.ylabel('Feels_like')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# global wind speed distribution
air = df['air_quality_Ozone']
plt.hist(air, bins= 20)
plt.tight_layout()
plt.show()

#  temperature_celsius vs humidity 
# assign color to each weather condition
def get_color(condition):
    if 'sun' in condition.lower():
        return 'orange'
    elif 'cloudy' in condition.lower():
        return 'blue'
    else :
        return "gray"

colors = df['condition_text'].apply(get_color)

plt.scatter(df['temperature_celsius'], df['humidity'],
            c = colors,             
            alpha = 0.5,
            s = 10)
plt.title('Temperature vs Humidity by Category')
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')
plt.show()

# Common weather condition
weather5 = df['condition_text'].value_counts().head(5)

plt.pie(weather5.values,
        labels = weather5.index,
        autopct = '%1.1f%%',
        )
plt.title('Top 5 Weather Conditions Globally')
plt.tight_layout()
plt.show()

countries = ['India', 'USA', 'Canada', 'Australia', 'Russia']

data = [df[df['country'] == c]['temperature_celsius'].values for c in countries]

plt.boxplot(data,
            labels=countries,
            patch_artist=True)
plt.title('Temperature Distribution by Country')
plt.xlabel('Country')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Trend line to scatter plot 
plt.scatter(df['temperature_celsius'], df['humidity'],
            c = colors,             
            alpha = 0.5,
            s = 10)
m, b = np.polyfit(df['temperature_celsius'], df['humidity'], 1)
plt.plot(df['temperature_celsius'],
         m * df['temperature_celsius'] + b,
         color='red',
         label='Trend Line')

plt.title('Temperature vs Humidity with Trend Line')
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')
plt.legend()
plt.tight_layout()
plt.show()

# Correlation heatmap 
cor = df.select_dtypes(include='number').corr()    # correlation!
print(cor)
plt.figure(figsize=(15, 12))
plt.imshow(cor)
plt.colorbar()
plt.xticks(range(len(cor.columns)), cor.columns, rotation=90)
plt.yticks(range(len(cor.columns)), cor.columns)
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()

city1 = input("Enter first city name: ")
city2 = input("Enter second city name: ")
data1 = df[df["location_name"] == city1]
data2 = df[df["location_name"] == city2]
if data1.empty:
    print(f"City '{city1}' not found in dataset!")
elif data2.empty:
    print(f"City '{city2}' not found in dataset!")
else:
 columns = ['temperature_celsius', 'humidity', 
           'wind_kph', 'pressure_mb', 'visibility_km']
city1_values = data1[columns].values[0]
city2_values = data2[columns].values[0]

x = np.arange(len(columns))
plt.figure(figsize=(12, 6))
plt.bar(x - 0.2, city1_values, width=0.4, label=city1, color='blue', alpha=0.7)
plt.bar(x + 0.2, city2_values, width=0.4, label=city2, color='red',  alpha=0.7)

plt.title(f'{city1} vs {city2} — Weather Comparison')
plt.xlabel('Weather Metrics')
plt.ylabel('Values')
plt.xticks(x, columns, rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
