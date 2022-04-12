import vehicleProfileV3FixedRanges
from constsAndHelpers import logFilesAsDfs

acc10 = vehicleProfileV3FixedRanges.VehicleProfile('08KY10099', logFilesAsDfs.accord10)
acc9 = vehicleProfileV3FixedRanges.VehicleProfile('08KY10099', logFilesAsDfs.accord9)

def testStoreV2():
    acc9 = vehicleProfileV3FixedRanges.VehicleProfile('08KY10099', logFilesAsDfs.accord9)
    # acc10.storeProfile()
    # print(acc10)
    acc9.storeProfile()
    print(acc9)

def testCompareFprint():
    acc10 = vehicleProfileV3FixedRanges.VehicleProfile('08KY10099', logFilesAsDfs.accord10)
    print(acc10)
    acc10.compareFprintsHavePath('v2JsonFprintProfiles\\08KY10099_05-04-22-22_5220.318.json')
    print("----- generating new fingerprint after bringing to base vals -----")
    acc10.bringValsToBaseAndGenFprint('v2JsonFprintProfiles\\08KY10099_05-04-22-22_5220.318.json')
    print(acc10)
    acc10.compareFprintsHavePath('v2JsonFprintProfiles\\08KY10099_05-04-22-22_5220.318.json')


def testGenFprint():
    acc1 = vehicleProfileV3FixedRanges.VehicleProfile("08KY10099", logFilesAsDfs.accord9)
    acc1.genFprint(acc1.profileDetails)

def testGenFprintOfOther():
    profileAcc2 = vehicleProfileV3FixedRanges.VehicleProfile('08KY10099', logFilesAsDfs.accord6)
    print(profileAcc2)
    profileAcc2.bringValsToBaseAndGenFprint('v1JsonProfiles/08KY10099_05-04-22-14_56.json')
    print(profileAcc2)
    profileAcc2.storeProfile()

def main():
    print("----- testing v2 -----")    
    # testMultiple([logFilesAsDfs.golf1NotRunning,
    #     logFilesAsDfs.golf2, logFilesAsDfs.golf3])
    testCompareFprint()
    # testGenFprint()
    # testStoreV2()
    # testGenFprintOfOther()

if __name__ == "__main__":
    main()
