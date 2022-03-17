import pandas as pd
from matplotlib import pyplot as plt
from pip import main

from logFilesAsDfs import * 

def plotOneValMultDfsOver0(valCheck, dfList):   
    for df in dfList:
        df[(df[valCheck] > 0)][valCheck].plot()

    plt.show()

def plotOneValMultDfshasValue(valCheck, dfList):   
    for df in dfList:
        df[(df[valCheck] != '-')][valCheck].plot()

    plt.show()

def printDescribes(valCheck, dfList):   
    count = 0
    for df in dfList:
        count += 1
        print(count)
        print(df[valCheck].describe())

rpm = 'Engine RPM(rpm)'

boost = 'Turbo Boost & Vacuum Gauge(psi)'

dfList = [accord1, accord2, accord3, accord4, accord5, accord6]
# plotOneValMultDfsOver0(rpm, dfList)

imp = 'Intake Manifold Pressure(psi)'
# printDescribes(boost, dfList) # no good

plotOneValMultDfsOver0(rpm, dfList)