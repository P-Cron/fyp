import pandas as pd
df = pd.read_csv("torqueLogs\\trackLog-2022-Jan-23_19-26-14.csv")
df1 = df[['Device Time', '0903', '0100', '0120', 'Engine Coolant Temperature(°C)']].copy()
print(df.columns)
print(df1.columns)
print(df1['Engine Coolant Temperature(°C)'].median()) # get median is easy
# to get last row
print(df[['service 09 pids supported']].head(1))
print(df1)
