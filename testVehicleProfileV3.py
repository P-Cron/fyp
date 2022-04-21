import vehicleProfileV3FixedRanges
from constsAndHelpers import logFilesAsDfs

acc10 = vehicleProfileV3FixedRanges.VehicleProfile('08KY10099', logFilesAsDfs.accord10)
acc9 = vehicleProfileV3FixedRanges.VehicleProfile('08KY10099', logFilesAsDfs.accord9)


def testCompareFprint():
    acc10 = vehicleProfileV3FixedRanges.VehicleProfile('08KY10099', logFilesAsDfs.accord10)
    print(acc10)
    print(acc9)
    acc9.bringValsToBaseAndGenFprint()
    print("check vals after bringing to base")
    print(acc9)
    acc9.storeProfile()
    acc10.compareFprintsHavePath(acc10.getPathsProfilesSameID()[-1])
    acc10.bringValsToBaseAndGenFprint()
    print("have brought to base, checking f print again")
    acc10.compareFprintsHavePath(acc10.getPathsProfilesSameID()[-1])

def main():
    print("\n----- testing v3 -----\n")    

    testCompareFprint()


if __name__ == "__main__":
    main()
