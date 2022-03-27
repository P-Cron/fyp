import pandas as pd
avensis08Path = 'torqueLogs\\trackLog-2022-Feb-12_12-18-08_Avensis08.csv'

df1 = pd.read_csv(avensis08Path)
print(df1['0100'].describe())