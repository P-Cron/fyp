import pandas as pd
df = pd.read_csv("torqueLogs\\trackLog-2022-Jan-16_17-42-53.csv")
jan16LogsPath = 'torqueLogs\\trackLog-2022-Jan-16_17-42-53.csv'
jan23LogsPath = 'torqueLogs\\trackLog-2022-Jan-23_19-26-14.csv'
jan27LogsPath = 'torqueLogs\\trackLog-2022-Jan-27_12-40-54.csv'

df1 = pd.read_csv(jan16LogsPath)
df2 = pd.read_csv(jan23LogsPath)
df3 = pd.read_csv(jan27LogsPath)

validColumns = []
for columnName in df3.columns:
    if df3.tail(1)[columnName].values[0]!="-":
        # print(columnName)
        print("-----")
        print(df3.tail(1)[columnName])
        validColumns.append(columnName)
print(validColumns)