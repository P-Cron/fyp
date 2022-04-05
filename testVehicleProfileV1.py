import pandas as pd
import vehicleProfileV1FullJson
import vehicleProfileV2FullJsonWFprint
from constsAndHelpers import logFilesAsDfs

profileGolf1 = vehicleProfileV1FullJson.VehicleProfile('07D22551', logFilesAsDfs.golf2)
profileGolf2 = vehicleProfileV1FullJson.VehicleProfile('07D22551', logFilesAsDfs.golf3)


def testStore():


    print(profileGolf1)
    profileGolf1.storeProfile()
    print(profileGolf2)
    profileGolf2.storeProfile()


def testLoad():
    loadedProfile = vehicleProfileV1FullJson.loadProfile('pickledProfiles/08KY12345_16-01-26.pkl')
    print(loadedProfile)

def testCompare():
    profileGolf1.compareProfiles()

def testMultiple(dfs):
    count = 0
    for df in dfs:
        count += 1
        profile = vehicleProfileV1FullJson.VehicleProfile('08KY123Test'+str(count), df)
        print(profile)
        profile.storeProfile()

def main():
    print("Main starting!")
    # testStore()
    # testMultiple([logFilesAsDfs.golf1NotRunning,
    #     logFilesAsDfs.golf2, logFilesAsDfs.golf3])
    print("----- testing compare -----")
    testCompare()

if __name__ == "__main__":
    main()
    