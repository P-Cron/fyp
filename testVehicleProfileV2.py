import vehicleProfileV1FullJson
import vehicleProfileV2FullJsonWFprint
from constsAndHelpers import logFilesAsDfs

def testStoreV2():
    acc10 = vehicleProfileV2FullJsonWFprint.VehicleProfile('08KY10099', logFilesAsDfs.accord10)
    print(acc10)

def testCompare():
    profileAcc2 = vehicleProfileV2FullJsonWFprint.VehicleProfile('08KY10099', logFilesAsDfs.accord6)
    profileAccord = vehicleProfileV2FullJsonWFprint.VehicleProfile('08KY10099', logFilesAsDfs.accord9)

    profileAcc2.compareFprints(profileAccord)
    profileAcc2.bringValsToBaseAndGenFprint('v1JsonProfiles/08KY10099_05-04-22-14_56.json')
    print(profileAcc2)
    profileAcc2.compareFprints(profileAccord)

def testGenFprint():
    acc1 = vehicleProfileV2FullJsonWFprint.VehicleProfile("08KY10099", logFilesAsDfs.accord9)
    acc1.genFprint(acc1.profileDetails)

def testGenFprintOfOther():
    profileAcc2 = vehicleProfileV2FullJsonWFprint.VehicleProfile('08KY10099', logFilesAsDfs.accord6)
    print(profileAcc2)
    profileAcc2.bringValsToBaseAndGenFprint('v1JsonProfiles/08KY10099_05-04-22-14_56.json')
    print(profileAcc2)
    profileAcc2.storeProfile()

if __name__ == "__main__":
    print("Main starting!")
    # testStore()
    # testMultiple([logFilesAsDfs.golf1NotRunning,
    #     logFilesAsDfs.golf2, logFilesAsDfs.golf3])
    # testCompare()
    # testGenFprint()
    testStoreV2()
    # testGenFprintOfOther()
