import pandas as pd
import vehicleProfileV2FullJson
import vehicleProfileV3FullJsonWFprint
from constsAndHelpers import logFilesAsDfs


def testStore():
    df = pd.read_csv("torqueLogs/trackLog-2022-Mar-13_23-11-53_Accord08.csv")
    df = df.rename(columns={'100': '0100', '120': '0120', '903':'0903'})

    # df2 = logFilesAsDfs.accord7
    profileAccord = vehicleProfileV2FullJson.VehicleProfile('08KY10099', logFilesAsDfs.accord9)
    # profileGolf = vehicleProfileV2FullJson.VehicleProfile('07D22551', logFilesAsDfs.golf2)
    profileGolf = vehicleProfileV2FullJson.VehicleProfile('07D22551', logFilesAsDfs.golf3)


    print(profileGolf)
    profileGolf.storeProfile()

def testStoreV3():
    profileAccord = vehicleProfileV2FullJson.VehicleProfile('08KY10099', logFilesAsDfs.accord9)
    profileAccord.storeProfile()
    print(profileAccord)

def testLoad():
    loadedProfile = vehicleProfileV2FullJson.loadProfile('pickledProfiles/08KY12345_16-01-26.pkl')
    print(loadedProfile)

def testCompare():
    profileGolf = vehicleProfileV2FullJson.VehicleProfile('07D22551', logFilesAsDfs.golf3)
    profileGolf.compareProfiles()

def testMultiple(dfs):
    count = 0
    for df in dfs:
        count += 1
        profile = vehicleProfileV2FullJson.VehicleProfile('08KY123Test'+str(count), df)
        print(profile)
        profile.storeProfile()

def testGenFprint():
    acc1 = vehicleProfileV3FullJsonWFprint.VehicleProfile("08KY10099", logFilesAsDfs.accord9)
    acc1.genFprint()


if __name__ == "__main__":
    print("Main starting!")
    # testStore()
    # testMultiple([logFilesAsDfs.golf1NotRunning,
    #     logFilesAsDfs.golf2, logFilesAsDfs.golf3])
    # testCompare()
    # testGenFprint()
    testStoreV3()