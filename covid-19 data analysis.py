
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv('Latest Covid-19 India Status.csv')

print('This is about the covid-19 data analysis')
user=input('Enter the state name of your preference:').strip().lower()
result= df[df['State/UTs'].str.strip().str.lower()==user]

if result.empty:
    print("State not found! Please check the spelling.")
else:
    state     = result['State/UTs'].values[0]
    total     = result['Total Cases'].values[0]      
    active    = result['Active'].values[0]
    discharged = result['Discharged'].values[0]
    deaths    = result['Deaths'].values[0]

    print(f"State        : {state}")
    print(f"Total Cases  : {total}")
    print(f"Active       : {active}")
    print(f"Discharged   : {discharged}")
    print(f"Deaths       : {deaths}")
values = [total,active, discharged, deaths]
labels = ['Total cases','Active cases','Discharged','Deaths']  
colors = ['red','green','blue','Black']
plt.figure(figsize=(7,7))
plt.pie(values,labels=labels,colors=colors,autopct='%1.1f%%')  
legend_labels = [f'Total Cases:{total:,}',f'Active : {active:,}',f'Discharged : {discharged:,}',f'Deaths : {deaths:,}']
plt.legend(legend_labels,
           title='Case Breakdown',
           loc='lower right')
plt.title(f'COVID-19 Distribution for {state}',fontsize=12,fontweight='bold')      
plt.tight_layout()  
plt.show()