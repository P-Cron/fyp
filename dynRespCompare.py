import pandas as pd
from matplotlib import pyplot as plt

from logFilesAsDfs import * 

def plotValsMultDfsOver0(valCheckList, dfList):   
    count = 0
    for df in dfList:
        count += 1
        for valCheck in valCheckList:
            df[(df[valCheck] > 0)][valCheck].plot(label='df'+str(count)+' - '+valCheck)

    plt.legend(loc='upper left')
    plt.show()

def convertDfsColsToNums(dfList, valCheck):
    convertedDfs = []
    for df in dfList:
        df = (df[(df[valCheck] != '-')].copy())
        df[valCheck]= pd.to_numeric(df[valCheck])
        convertedDfs.append(df)
    return convertedDfs

def plotValsMultDfsHasValue(valCheckList, dfList):   
    # can check multiple values over multiple dataframes
    count = 0
    for df in dfList:
        count += 1
        for valCheck in valCheckList:
            df[(df[valCheck] != '-')][valCheck].plot(label='df'+str(count)+' - '+valCheck)

    plt.legend(loc='upper right')
    plt.show()

def printDescribes(valCheck, dfList):   
    count = 0
    for df in dfList:
        count += 1
        print(count)
        print(df[valCheck].describe())

def getDfsRpmIs0(dfList):
    zeroRpmDfs = []
    for df in dfList:
        dfZeroRpm = df[(df["Engine RPM(rpm)"] == 0)].copy()
        zeroRpmDfs.append(dfZeroRpm)
    return zeroRpmDfs


# list of dataframes for different cars
dfList = [accord1, accord2, accord3, accord4, accord5, accord6, accord7, accord8, accord9]
dfList0Rpms = getDfsRpmIs0(dfList)
otherCars = []

# dynamic variable names
rpm = 'Engine RPM(rpm)'
boost = 'Turbo Boost & Vacuum Gauge(psi)'
imp = 'Intake Manifold Pressure(psi)'
egrPercent = 'EGR Commanded(%)'
fuelRailP = 'Fuel Rail Pressure(psi)'
engLoad = 'Engine Load(%)' # no use
intManPress = 'Intake Manifold Pressure(psi)' # no good and all cars seem to have the same
mafRate= 'Mass Air Flow Rate(g/s)' # no good I think
coolantTemp = 'Engine Coolant Temperature(°C)'
volEff= 'Volumetric Efficiency (Calculated)(%)'
obdSpeed = 'Speed (OBD)(mph)'


if __name__ == "__main__":
    # plotValsMultDfsOver0(rpm, dfList)
    # printDescribes(boost, dfList) # no good, boost is always changing
    # printDescribes(egrPercent, dfList)
    # plotValsMultDfsHasValue([intManPress], dfList)
    # printDescribes([fuelRailP, coolantTemp], dfList0Rpms)
    # plotValsMultDfsHasValue([fuelRailP], dfList0Rpms)
    # printDescribes(volEff, convertDfsColsToNums(dfList0Rpms, volEff))
    # plotValsMultDfsHasValue([volEff, rpm], convertDfsColsToNums(dfList0Rpms, volEff))
    # vol eff might be missing in some of the dfs
    # finding if turbo boost can be used, across logs it does not seem to be stable though it is stable in individual logs
    # accord9[rpm] = accord9[rpm]/1100
    # accord9[obdSpeed] = accord9[obdSpeed]/12
    # accord9[coolantTemp] = accord9[coolantTemp]/10
    # plotValsMultDfsHasValue([obdSpeed, rpm, boost, coolantTemp], [accord9])
    pass
