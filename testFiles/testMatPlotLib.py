from matplotlib import pyplot as plt
import pandas as pd
  
jan16LogsPath = 'torqueLogs\\trackLog-2022-Jan-16_17-42-53.csv'
jan23LogsPath = 'torqueLogs\\trackLog-2022-Jan-23_19-26-14.csv'
jan27LogsPath = 'torqueLogs\\trackLog-2022-Jan-27_12-40-54.csv'
jan29LogsPath = 'torqueLogs\\trackLog-2022-Jan-29_00-56-43_FIXED.csv'

df1 = pd.read_csv(jan16LogsPath)
df2 = pd.read_csv(jan23LogsPath)
df3 = pd.read_csv(jan27LogsPath)

dfPlot = df3[['Device Time', '0100', '011c obd standards vehicle conforms to', '0120', '0903', 'CO₂ in g/km (Average)(g/km)', 'Distance travelled with MIL/CEL lit(miles)', 'EGR Commanded(%)', \
    'Engine Coolant Temperature(°C)', 'Engine Load(%)', # 'Engine RPM(rpm)',\
    #'Fuel Rail Pressure(psi)',\ # take out fuel rail pressure
         'Intake Air Temperature(°C)', 'Intake Manifold Pressure(psi)', 'Mass Air Flow Rate(g/s)',\
        'pids supported 01-20', 'service 09 pids supported', 'Turbo Boost & Vacuum Gauge(psi)', 'Voltage (OBD Adapter)(V)', \
            'Volumetric Efficiency (Calculated)(%)']]


dfPlot2 = df3[df3['Volumetric Efficiency (Calculated)(%)'] != '-']['Volumetric Efficiency (Calculated)(%)'] 
# get all the rows where it is not - and then take just that column 
dfPlot2 = pd.to_numeric(dfPlot2) # convert a series to numeric
print(dfPlot2.describe())
dfPlot2.plot()
plt.show()