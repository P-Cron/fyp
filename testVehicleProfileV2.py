import vehicleProfileV2FullJsonWFprint
from constsAndHelpers import logFilesAsDfs

acc10 = vehicleProfileV2FullJsonWFprint.VehicleProfile('08KY10099', logFilesAsDfs.accord10)
acc9 = vehicleProfileV2FullJsonWFprint.VehicleProfile('08KY10099', logFilesAsDfs.accord9)

def testStoreV2():

    acc9.storeProfile()


def checkProfsAreDiff():
    # show that different vehicles create different profiles and fingerprints
    print("---- printing accord08 ----")
    print(acc10)
    cor06 = vehicleProfileV2FullJsonWFprint.VehicleProfile('corolla06', logFilesAsDfs.corolla1)
    print("---- printing corolla06 ----")
    print(cor06)
    aven08 = vehicleProfileV2FullJsonWFprint.VehicleProfile('avensis08', logFilesAsDfs.avensis2)
    print("---- printing avensis08 ----")
    print(aven08)


def testCompareFprintUsingPath():
    # show how a profile which differs from another in its dynamic values
    # can regenerate its fingerprint in order for the fingerprints to match
    print(acc10)
    acc10.storeProfile()
    print(acc9)
    acc9.compareFprintsHavePath(acc9.getPathsProfilesSameID()[-1])
    print("----- generating new fingerprint from previous profile-----")
    acc9.bringValsToBaseAndGenFprint(acc9.getPathsProfilesSameID()[-1])
    print(acc9)
    acc9.compareFprintsHavePath(acc9.getPathsProfilesSameID()[-1])

def testCompareFprint():
    acc10 = vehicleProfileV2FullJsonWFprint.VehicleProfile('08KY10099', logFilesAsDfs.accord10)
    print(acc10)
    acc10.compareFprints()
    acc10.bringValsToBaseAndGenFprint('v2JsonFprintProfiles\\08KY10099_05-04-22-22_5220.318.json')
    
    acc10.compareFprints()
    print(acc10.getPathsProfilesSameID())



def testGenFprint():
    acc1 = vehicleProfileV2FullJsonWFprint.VehicleProfile("08KY10099", logFilesAsDfs.accord9)
    acc1.genFprint(acc1.profileDetails)

def testGenFprintOfOther():
    profileAcc2 = vehicleProfileV2FullJsonWFprint.VehicleProfile('08KY10099', logFilesAsDfs.accord6)
    print(profileAcc2)
    profileAcc2.bringValsToBaseAndGenFprint('v1JsonProfiles/08KY10099_05-04-22-14_56.json')
    print(profileAcc2)
    profileAcc2.storeProfile()

def main():
    print("\n----- testing v2 -----\n")    
    testCompareFprintUsingPath()

if __name__ == "__main__":
    main()
