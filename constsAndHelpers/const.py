# validColumns = ['Device Time', '0100', '011c obd standards vehicle conforms to', '0120', '0903', 'CO₂ in g/km (Average)(g/km)', 'Distance travelled with MIL/CEL lit(miles)', 'EGR Commanded(%)', 'Engine Coolant Temperature(°C)', 'Engine Load(%)', 'Engine RPM(rpm)', 'Fuel Rail Pressure(psi)', 'Intake Air Temperature(°C)', 'Intake Manifold Pressure(psi)', 'Mass Air Flow Rate(g/s)', 'service 09 pids supported', 'Turbo Boost & Vacuum Gauge(psi)', 'Voltage (OBD Adapter)(V)', 'Volumetric Efficiency (Calculated)(%)']

STATIC_PIDS = ['0100', '011c obd standards vehicle conforms to', '0120', '0140', '0160',
 '0900', '0901 vin message count', '0902', '0903', '0904', 
 '0905', '0906', '0907', '0908', '0909', '090A', '090B', 'service 09 pids supported']
DEFAULT_DYN_PIDS = ['Engine RPM(rpm)',  'EGR Commanded(%)', "Miles Per Gallon(Long Term Average)(mpg)",
        "Throttle Position(Manifold)(%)"]
# decided against using vol efficiency, it too often only gives '-' values when rpm is 0
DEFAULT_USEFUL_PIDS = STATIC_PIDS+DEFAULT_DYN_PIDS # useful pids is just the two other pid lists combined
DEFAULT_TOLERANCES = {'Engine RPM(rpm)':20,
  'EGR Commanded(%)': 3,
   "Miles Per Gallon(Long Term Average)(mpg)": 10,
        "Throttle Position(Manifold)(%)": 3}

RPM = 'Engine RPM(rpm)'
TURBO_BOOST = 'Turbo Boost & Vacuum Gauge(psi)'
IMP = 'Intake Manifold Pressure(psi)'
EGR = 'EGR Commanded(%)'
FUEL_RAIL = 'Fuel Rail Pressure(psi)'
ENG_LOAD = 'Engine Load(%)' # no use
MAF_RATE= 'Mass Air Flow Rate(g/s)' # no good I think
COOL_TEMP = 'Engine Coolant Temperature(°C)'
VOL_EFF= 'Volumetric Efficiency (Calculated)(%)'
MPG = 'Miles Per Gallon(Long Term Average)(mpg)'
THROT_POS = 'Throttle Position(Manifold)(%)'

FIXED_RANGES = {'Engine RPM(rpm)':[i for i in range(500, 1500, 25)], # intervals of 25 for RPM
  'EGR Commanded(%)': [i for i in range(0, 30, 1)],
   "Miles Per Gallon(Long Term Average)(mpg)": [i for i in range(10, 70, 10)],
        "Throttle Position(Manifold)(%)": [i for i in range(5, 50, 1)] # increments of 1
        }