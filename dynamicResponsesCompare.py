import pandas as pd
df = pd.read_csv("torqueLogs\\trackLog-2022-Jan-16_17-42-53.csv")
df1 = df[['Device Time', '0903', 'Engine Coolant Temperature(°C)']].copy()
jan16LogsPath = 'torqueLogs\\trackLog-2022-Jan-16_17-42-53.csv'
jan23LogsPath = 'torqueLogs\\trackLog-2022-Jan-23_19-26-14.csv'
jan27LogsPath = 'torqueLogs\\trackLog-2022-Jan-27_12-40-54.csv'
jan29LogsPath = 'torqueLogs\\trackLog-2022-Jan-29_00-56-43.csv'

df1 = pd.read_csv(jan16LogsPath)
df2 = pd.read_csv(jan23LogsPath)
df3 = pd.read_csv(jan27LogsPath)
# df4 = pd.read_csv(jan29LogsPath) # this csv seems to be corrupted

for df in [df1, df2, df3]:
    print("-----Next log-----")
    # print(df.columns)
    # for thing in df.tail(1):
    #     print(thing)

    #print(df.tail(1))
    # remove blanks
    # df = df.loc[df['Engine RPM(rpm)']!='0']
    print("--- RPM Stats ---")
    df = df[(df["Engine RPM(rpm)"] > 100)].copy() # how to get stuff over 100
    print(df.head(1)[['Engine RPM(rpm)']])

    # some other stat should check out now
    print(df['Engine RPM(rpm)'].describe())

for df in [df1, df2, df3]:
    print("-----Next log-----")
    print("--- Fuel Rail Pressure(psi) Stats ---")
    print(df.head(1)[['Fuel Rail Pressure(psi)']])

    # some other stat should check out now
    print(df['Fuel Rail Pressure(psi)'].describe())

# fuel rail pressure isn't any use really it seems

df1.corr()