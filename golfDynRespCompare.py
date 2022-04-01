from dynRespCompare import *

# all columns for golf which give a value
colsOfInterest = ['CO₂ in g/km (Average)(g/km)', 
'Distance travelled with MIL/CEL lit(miles)', 'Engine Coolant Temperature(°C)', 'Engine Load(%)',
 'Engine RPM(rpm)', 'Fuel Trim Bank 1 Long Term(%)', 'Fuel Trim Bank 1 Short Term(%)', 
 'Intake Air Temperature(°C)', 'Intake Manifold Pressure(psi)', 'Kilometers Per Litre(Instant)(kpl)', 
 'Kilometers Per Litre(Long Term Average)(kpl)', 'Litres Per 100 Kilometer(Long Term Average)(l/100km)', 
 'Miles Per Gallon(Instant)(mpg)', 'Miles Per Gallon(Long Term Average)(mpg)', 
 'O2 Sensor1 Wide Range Current(mA)', 'O2 Bank 1 Sensor 1 Wide Range Equivalence Ratio(λ)', 
 'O2 Bank 1 Sensor 2 Voltage(V)', 'Speed (OBD)(mph)', 
 'Throttle Position(Manifold)(%)', 'Trip average KPL(kpl)', 'Trip average Litres/100 KM(l/100km)', 
 'Trip average MPG(mpg)', 'Turbo Boost & Vacuum Gauge(psi)']


# golf DF lists
golfDfList = [golf2, golf3] # golf1 did not have the engine running so not using
golfDfList0Rpms = getDfsRpmIs0(golfDfList)
statGolfs = getDfsRunStationary(golfDfList)


if __name__ == "__main__":

    # plotValsShowVals([rpm, boost, coolantTemp], [getDfsRunStationary([golf2])])
    # boost looks good here for golf, actuall too dependant on coolant really
    # plotValsShowVals([rpm, boost, coolantTemp], getDfsRunStationary([golf2, golf3]))
    # printDescribes([rpm, boost, coolantTemp], statGolfs)
    # for col in colsOfInterest:
    #     printDescribes(col, golfDfList0Rpms+statGolfs)
    # printDescribes([fTrim1Lt, coolantTemp], golfDfList0Rpms)
    # plotValsShowVals([fTrim1Lt, coolantTemp], [golf3])
    # fTrim maybe not useful, is stable when the engine has heated up and then is turned off it seems
    # becomes stabel once engine coolant reaches a certain temp

    # now checking o2 sensor. Seems a bit too dependant on temp
    # printDescribes([o2sensor, coolantTemp], golfDfList)
    # plotValsShowVals([o2sensor, coolantTemp], golfDfList)

    # checking throtPos
    # printDescribes([throtPos, coolantTemp], golfDfList0Rpms) # seems good and stable while car not started
    # printDescribes([throtPos, coolantTemp], statGolfs) # is less reliable when started. Better off with the car not running
    # plotValsShowVals([throtPos, coolantTemp], statGolfs)
    
    #usableCols = getValidColumns(golf2)
    #print(usableCols)
    pass
