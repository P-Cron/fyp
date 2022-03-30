import pandas as pd
import const

jan16LogsPath = 'torqueLogs\\trackLog-2022-Jan-16_17-42-53.csv'
jan23LogsPath = 'torqueLogs\\trackLog-2022-Jan-23_19-26-14.csv'
jan27LogsPath = 'torqueLogs\\trackLog-2022-Jan-27_12-40-54.csv'
jan29LogsPath = 'torqueLogs\\trackLog-2022-Jan-29_00-56-43_FIXED.csv'
mar12LogsPath = 'torqueLogs\\trackLog-2022-Mar-12_17-27-39_Accord08_FIXED.csv'
mar13LogsPath = 'torqueLogs\\trackLog-2022-Mar-13_23-11-53_Accord08.csv'
mar16LogsPathGolf1 = 'torqueLogs\\trackLog-2022-Mar-16_15-15-49_Golf07Fixed1.csv'
mar16LogsPathGolf2 = 'torqueLogs\\trackLog-2022-Mar-16_15-15-49_Golf07Fixed2.csv'
mar16LogsPathGolf3 = 'torqueLogs\\trackLog-2022-Mar-16_15-15-49Golf07Fixed3.csv'

def changeDfColumnName(df):
    df = df.rename(columns={'100': '0100', '120': '0120', '140': '0140', '160':'0160',
     '900':'0900', 'service 09 pids supported': '0900',
     '903':'0903', '902': '0902', '903': '0903', '904': '0904', '905': '0905', '906':'0906',
     '907': '0907', '908': '0908', '909':'0909'})
    # need to rename columns as leading 0s are sometimes lost
    return df

accord1 = changeDfColumnName(pd.read_csv(jan16LogsPath))
accord2 = changeDfColumnName(pd.read_csv(jan23LogsPath))
accord3 = changeDfColumnName(pd.read_csv(jan27LogsPath))
accord4 = changeDfColumnName(pd.read_csv(jan29LogsPath, on_bad_lines='skip')) # this csv seems to be corrupted, now have fixed though
accord5 = changeDfColumnName(pd.read_csv(mar12LogsPath, on_bad_lines='skip'))
accord6 = changeDfColumnName(pd.read_csv(mar13LogsPath))
accord7 = changeDfColumnName(pd.read_csv('torqueLogs\\trackLog-2022-Mar-16_10-00-53_Acccord08_Fixed1stHalfNotRunning.csv'))
accord8 = changeDfColumnName(pd.read_csv('torqueLogs\\trackLog-2022-Mar-16_10-00-53_Accord08_fixed2ndHalf.csv'))


golf1 = changeDfColumnName(pd.read_csv(mar16LogsPathGolf1))
golf2 = changeDfColumnName(pd.read_csv(mar16LogsPathGolf2))
golf3 = changeDfColumnName(pd.read_csv(mar16LogsPathGolf3))

corolla1 = changeDfColumnName(pd.read_csv('torqueLogs\\trackLog-2022-Feb-12_10-53-51_Corolla06.csv'))

allDfs = [accord1, accord2, accord3, accord4, accord5, accord6, accord7, accord8,
golf1, golf2, golf3, 
corolla1]
