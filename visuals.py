import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv('Latest Covid-19 India Status.csv')
print(df.head())
print(df.isna().sum())


plt.figure(figsize=(12, 6))
sns.regplot(x='Total Cases',y='Active',data=df)
plt.title('Total cases v/s Active cases')
plt.xlabel('Total cases')
plt.ylabel('Active cases')
plt.tight_layout()
plt.show()