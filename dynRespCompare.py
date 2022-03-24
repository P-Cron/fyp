import pandas as pd
from matplotlib import pyplot as plt
from pip import main

from logFilesAsDfs import * 

def plotOneValMultDfsOver0(valCheckList, dfList):   
    count = 0
    for df in dfList:
        count += 1
        for valCheck in valCheckList:
            df[(df[valCheck] > 0)][valCheck].plot(label='df'+str(count)+' - '+valCheck)

    plt.legend(loc='upper left')
    plt.show()

def plotOneValMultDfshasValue(valCheckList, dfList):   
    # can check multiple values over multiple dataframes
    count = 0
    for df in dfList:
        count += 1
        for valCheck in valCheckList:
            df[(df[valCheck] != '-')][valCheck].plot(label='df'+str(count)+' - '+valCheck)

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
otherCars = []

imp = 'Intake Manifold Pressure(psi)'

egrPercent = 'EGR Commanded(%)'
fuelRailP = 'Fuel Rail Pressure(psi)'
engLoad = 'Engine Load(%)' # no use
intManPress = 'Intake Manifold Pressure(psi)' # no good and all cars seem to have the same
mafRate= 'Mass Air Flow Rate(g/s)' # no good I think
if __name__ == "__main__":
    # plotOneValMultDfsOver0(rpm, dfList)
    # printDescribes(boost, dfList) # no good, boost is always changing
    printDescribes(mafRate, dfList)
    plotOneValMultDfshasValue([intManPress], dfList)
    # print(accord2[egrPercent].quantile(0.25)) # can get quantile like that


