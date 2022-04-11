import pandas as pd
from constsAndHelpers.logFilesAsDfs import *

df = pd.read_csv("torqueLogs\\trackLog-2022-Jan-16_17-42-53.csv")
jan16LogsPath = 'torqueLogs\\trackLog-2022-Jan-16_17-42-53.csv'
jan23LogsPath = 'torqueLogs\\trackLog-2022-Jan-23_19-26-14.csv'
jan27LogsPath = 'torqueLogs\\trackLog-2022-Jan-27_12-40-54.csv'

df1 = pd.read_csv(jan16LogsPath)
df2 = pd.read_csv(jan23LogsPath)
df3 = pd.read_csv(jan27LogsPath)


def getValidColumns(df):
    validColumns = []
    for columnName in df.columns:
        if df.tail(1)[columnName].values[0]!="-":
            # print(columnName)
            print("-----")
            print(df.tail(1)[columnName])
            validColumns.append(columnName)
    return validColumns

if __name__ == "__main__":
    # getValidColumns(df3)
    # validColumns = ['Device Time', '0100', '011c obd standards vehicle conforms to', '0120', '0903', 'CO₂ in g/km (Average)(g/km)', 'Distance travelled with MIL/CEL lit(miles)', 'EGR Commanded(%)', 'Engine Coolant Temperature(°C)', 'Engine Load(%)', 'Engine RPM(rpm)', 'Fuel Rail Pressure(psi)', 'Intake Air Temperature(°C)', 'Intake Manifold Pressure(psi)', 'Mass Air Flow Rate(g/s)', 'pids supported 01-20', 'service 09 pids supported', 'Turbo Boost & Vacuum Gauge(psi)', 'Voltage (OBD Adapter)(V)', 'Volumetric Efficiency (Calculated)(%)']
#     corollaValid = ['0100', '011c obd standards vehicle conforms to', '0120', '0140', '0160',
# '0901 vin message count', '0902', '0903', '0905', '0906', '0907', '0908', '0909', '090A', '090B',
#    'Fuel flow rate/hour(l/hr)', 'Fuel flow rate/minute(cc/min)', 'Fuel Remaining (Calculated from vehicle profile)(%)', 'Fuel used (trip)(l)', 'Intake Air Temperature(°C)', 'Intake Manifold Pressure(psi)', 'Kilometers Per Litre(Instant)(kpl)', 'Kilometers Per Litre(Long Term Average)(kpl)', 'Litres Per 100 Kilometer(Long Term Average)(l/100km)', 'Mass Air Flow Rate(g/s)', 'Miles Per Gallon(Instant)(mpg)', 'Miles Per Gallon(Long Term Average)(mpg)', 'pids supported 01-20', 'service 09 pids supported', 'Turbo Boost & Vacuum Gauge(psi)', 'Voltage (OBD Adapter)(V)', 'Volumetric Efficiency (Calculated)(%)']
    print(getValidColumns(corolla1))