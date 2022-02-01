import pandas as pd
df = pd.read_csv("torqueLogs\\trackLog-2022-Jan-16_17-42-53.csv")
df1 = df[['Device Time', '0903', 'Engine Coolant Temperature(°C)']].copy()
print(df.columns)
print(df1)
print(df1['Engine Coolant Temperature(°C)'].median()) # get median is easy
# print(df1.iloc[[-1]]) # last row
# alternatively tto get last row
print(df1.tail(1))
print(df1.tail(1)[['0903']])
print(df[['pids supported 01-20']].head(1))
print(df[['service 09 pids supported']].head(1))
