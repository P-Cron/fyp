# Final Year Project - Creating Unique Identities for Vehicles

Run main.py in order to observe simple tests being carried out on v1, v2 and v3 of vehicleProfile. This will also create profiles in the relevant directories for each version.

## Example Usage

To create a vehicle profile, a CSV file of vehicle data is needed as input. This CSV file is converted to a Pandas Dataframe. Some PIDs may need to added manually in the vehicle data collection application being used. The PIDs and the names required are specified in the 'PIDs Required' section.

Create the vehicle profile
```
import pandas as pd

vehicleDataFrame = pd.read_csv('pathToVehicleCSV ') 
vehicleId = '221D1234' # usually the vehicle registration number is used as the ID
vehicleProf1 = vehicleProfileV2FullJsonWFprint.VehicleProfile(vehicleId, vehicleDataFrame)
```

Print and store the profile
```
print(vehicleProf1)
vehicleProf1.storeProfile('PATH_TO_STORAGE_DIR')
```

Create a second profile. Assume there is a second CSV file taken from the same vehicle at a different time, so the same ID is used
```
vehicleDataFrame2 = pd.read_csv('pathToVehicleCSV2 ') 
vehicleProf2 = vehicleProfileV2FullJsonWFprint.VehicleProfile(vehicleId, vehicleDataFrame2)
```

Compare the profile with any other profiles with the same ID.

```
vehicleProf2.compareProfiles(DIR_TO_SEARCH)
```

Get the most recently stored profile, and compare fingerprints

```
vehicleProf2.compareFprintsHavePath(vehicleProf2.getPathsProfilesSameID(DIR_TO_SEARCH)[-1])
```
### PIDs Required
These columns are needed in CSV the file as the profiler program will look for them in order to build the profile.These PIDs needed to be added manually when collecting vehicle data, they were not in the available PIDs at first:

* 0100
* 011c obd standards vehicle conforms to
* 0120
* 0140
* 0160
* 0900
* 0901 vin message count
* 0902
* 0903
* 0904
* 0905
* 0906
* 0907
* 0908
* 0909
* 090A
* 090B
