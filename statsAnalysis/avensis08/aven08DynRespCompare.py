import sys
sys.path.append(".")
from statsAnalysis.accord08.dynRespCompare import *
from constsAndHelpers.checkWhichColumnsUsable import *

# print(getValidColumns(avensis2))

# all columns for avensis which give a value
colsOfInterest = [
    'Device Time', '0100', '011c obd standards vehicle conforms to', '0120', '0140', '0900', '0901 vin message count', '0903', '0905', '0906', 'Barometric pressure (from vehicle)(psi)', 'Distance travelled with MIL/CEL lit(miles)', 'EGR Commanded(%)', 'EGR Error(%)', 'Engine Coolant Temperature(°C)', 'Engine Load(%)', 'Engine RPM(rpm)', 
    'Fuel Rail Pressure(psi)', 'Intake Air Temperature(°C)', 
    'Intake Manifold Pressure(psi)', 'Kilometers Per Litre(Instant)(kpl)', 
    'Kilometers Per Litre(Long Term Average)(kpl)', 'Litres Per 100 Kilometer(Long Term Average)(l/100km)', 
    'Mass Air Flow Rate(g/s)', 'Miles Per Gallon(Instant)(mpg)', 'Miles Per Gallon(Long Term Average)(mpg)', 
    'Speed (OBD)(mph)', 'Throttle Position(Manifold)(%)', 'Trip average KPL(kpl)', 'Trip average Litres/100 KM(l/100km)', 'Trip average MPG(mpg)', 
    'Turbo Boost & Vacuum Gauge(psi)', 'Voltage (Control Module)(V)', 'Voltage (OBD Adapter)(V)', 'Volumetric Efficiency (Calculated)(%)']

avenDfList = [avensis1, avensis2]
avenDfList0Rpms = getDfsRpmIs0(avenDfList)
statAvens = getDfsRunStationary([avensis2])

if __name__ == "__main__":
    # plotValsShowVals([rpm, coolantTemp], getDfsScaledRpm(avenDfList))
    # plotValsShowVals([egrPercent, rpm], getDfsScaledRpm(avenDfList)) # no use as can be seen
    # plotValsShowVals([egrPercent, rpm, egrErr], avenDfList0Rpms) # no use as can be seen, same as EGR percent
    plotValsShowVals([throtPos, rpm], avenDfList0Rpms) # throt pos remains consistent when vehicle has not been started
    pass
