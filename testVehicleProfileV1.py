import pandas as pd
import vehicleProfileV1FullJson
from constsAndHelpers import logFilesAsDfs

profileGolf1 = vehicleProfileV1FullJson.VehicleProfile('07D22551', logFilesAsDfs.golf2)
profileGolf2 = vehicleProfileV1FullJson.VehicleProfile('07D22551', logFilesAsDfs.golf3)


def testStore():


    print(profileGolf1)
    profileGolf1.storeProfile()
    print(profileGolf2)
    profileGolf2.storeProfile()


def testCompare():
    # finds profiles with the same id (reg number) and compares them
    # observe that golf1 and golf2 differ slightly but they are still considered a match
    # because the values are within the specified threshold 
    profileGolf1.compareProfiles()

def testMultiple(dfs):
    count = 0
    for df in dfs:
        count += 1
        profile = vehicleProfileV1FullJson.VehicleProfile('08KY123Test'+str(count), df)
        print(profile)
        profile.storeProfile()

def main():
    print("\n----- testing v1 -----\n")    
    testStore()
    print("----- two profiles stored. testing compare -----")
    testCompare()

if __name__ == "__main__":
    main()
    