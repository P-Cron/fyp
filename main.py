import pandas as pd
import vehicleProfile

def testStore():
    print("Main starting!")
    df = pd.read_csv("torqueLogs\\trackLog-2022-Jan-23_19-26-14.csv")
    profile1 = vehicleProfile.VehicleProfile('08KY123Other', '16-01-26', df)
    print(profile1)
    profile1.storeProfile()

def testLoad():
    loadedProfile = vehicleProfile.loadProfile('pickledProfiles\\08KY12345_16-01-26.pkl')
    print(loadedProfile)

def testCompare():
    loadedProfile1 = vehicleProfile.loadProfile('pickledProfiles\\08KY12345_16-01-26.pkl')
    loadedProfile2 = vehicleProfile.loadProfile('pickledProfiles\\08KY123Other_16-01-26.pkl')
    loadedProfile1.compareProfiles(loadedProfile2)


if __name__ == "__main__":
    #main()
    #testStore()
    testCompare()