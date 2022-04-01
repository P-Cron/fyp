import pandas as pd
import vehicleProfile
import logFilesAsDfs

def testStore():
    df = pd.read_csv("torqueLogs\\trackLog-2022-Mar-13_23-11-53_Accord08.csv")
    df = df.rename(columns={'100': '0100', '120': '0120', '903':'0903'})

    df2 = logFilesAsDfs.accord7
    profile1 = vehicleProfile.VehicleProfile('08KY10099', logFilesAsDfs.accord9)
    print(profile1)
    profile1.storeProfile() # not storing for now

def testLoad():
    loadedProfile = vehicleProfile.loadProfile('pickledProfiles\\08KY12345_16-01-26.pkl')
    print(loadedProfile)

def testCompare():
    loadedProfile1 = vehicleProfile.loadProfile('pickledProfiles\\08KY12345_16-01-26.pkl')
    loadedProfile2 = vehicleProfile.loadProfile('pickledProfiles\\08KY123Other_16-01-26.pkl')
    loadedProfile1.compareProfiles(loadedProfile2)

def testMultiple(dfs):
    count = 0
    for df in dfs:
        count += 1
        profile = vehicleProfile.VehicleProfile('08KY123Test'+str(count), df)
        print(profile)
        profile.storeProfile()
    


if __name__ == "__main__":
    print("Main starting!")
    testStore()
    # testMultiple([logFilesAsDfs.golf1NotRunning,
    #     logFilesAsDfs.golf2, logFilesAsDfs.golf3])
