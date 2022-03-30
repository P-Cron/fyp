import pandas as pd
import vehicleProfile
import logFilesAsDfs

def testStore():
    df = pd.read_csv("torqueLogs\\trackLog-2022-Mar-13_23-11-53_Accord08.csv")
    df = df.rename(columns={'100': '0100', '120': '0120', '903':'0903'})

    df2 = logFilesAsDfs.accord7
    profile1 = vehicleProfile.VehicleProfile('08KY123Test', logFilesAsDfs.accord8)
    print(profile1)
    # profile1.storeProfile() # not storing for now

def testLoad():
    loadedProfile = vehicleProfile.loadProfile('pickledProfiles\\08KY12345_16-01-26.pkl')
    print(loadedProfile)

def testCompare():
    loadedProfile1 = vehicleProfile.loadProfile('pickledProfiles\\08KY12345_16-01-26.pkl')
    loadedProfile2 = vehicleProfile.loadProfile('pickledProfiles\\08KY123Other_16-01-26.pkl')
    loadedProfile1.compareProfiles(loadedProfile2)


if __name__ == "__main__":
    print("Main starting!")
    testStore()
