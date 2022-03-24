from cProfile import label
import pandas as pd
from matplotlib import pyplot as plt
from pip import main

from logFilesAsDfs import * 

def plotOneValMultDfsOver0(valCheck, dfList):   
    count = 0
    for df in dfList:
        count += 1
        df[(df[valCheck] > 0)][valCheck].plot(label=str(count))

    plt.legend(loc='upper left')
    plt.show()

def plotOneValMultDfshasValue(valCheck, dfList):   
    count = 0
    for df in dfList:
        count += 1
        df[(df[valCheck] != '-')][valCheck].plot(label='df'+str(count))

    plt.legend(loc='upper left')
    plt.show()

def printDescribes(valCheck, dfList):   
    count = 0
    for df in dfList:
        count += 1
        print(count)
        print(df[valCheck].describe())

rpm = 'Engine RPM(rpm)'

boost = 'Turbo Boost & Vacuum Gauge(psi)'

dfList = [accord1, accord2, accord3, accord4, accord5, accord6, accord7]
# plotOneValMultDfsOver0(rpm, dfList)

imp = 'Intake Manifold Pressure(psi)'
# printDescribes(boost, dfList) # no good, boost is always changing

egrPercent = 'EGR Commanded(%)'

printDescribes(egrPercent, dfList)
plotOneValMultDfshasValue(egrPercent, dfList)