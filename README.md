# Final Year Project - Creating Unique Identities for Vehicles

Run main.py in order to observe simple tests being carried out on v1, v2 and v3 of vehicleProfile. This will also create profiles in the relevant directories for each version.

## Example Usage

To create a vehicle profile, a CSV file of vehicle data is needed as input. This CSV file is converted to a Pandas Dataframe. The 'PIDs required' section details what PIDs must be collected, and what the columns must be named in the CSV file.

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
### PIDs required
Need these columns in CSV file, and need these PIDs added manually when collecting data:

* 
* 