# validColumns = ['Device Time', '0100', '011c obd standards vehicle conforms to', '0120', '0903', 'CO₂ in g/km (Average)(g/km)', 'Distance travelled with MIL/CEL lit(miles)', 'EGR Commanded(%)', 'Engine Coolant Temperature(°C)', 'Engine Load(%)', 'Engine RPM(rpm)', 'Fuel Rail Pressure(psi)', 'Intake Air Temperature(°C)', 'Intake Manifold Pressure(psi)', 'Mass Air Flow Rate(g/s)', 'service 09 pids supported', 'Turbo Boost & Vacuum Gauge(psi)', 'Voltage (OBD Adapter)(V)', 'Volumetric Efficiency (Calculated)(%)']

STATIC_PIDS = ['0100', '011c obd standards vehicle conforms to', '0120', '0140', '0160',
'service 09 pids supported', '0900', '0901 vin message count', '0902', '0903', '0905', '0906', '0907', '0908', '0909', '090A', '090B',
    ]
DYNAMIC_PIDS = ['Engine RPM(rpm)', 'Volumetric Efficiency (Calculated)(%)',  'EGR Commanded(%)']
USEFUL_PIDS = STATIC_PIDS+DYNAMIC_PIDS # useful pids is just the two other pid lists combined
