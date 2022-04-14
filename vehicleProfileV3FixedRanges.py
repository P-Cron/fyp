import hashlib
import json
from constsAndHelpers import const, fixedRangesToFloor
from vehicleProfileBase import VehicleProfileBase


class VehicleProfile(VehicleProfileBase):
    def __init__(self, reg, dataFrame):
        super().__init__(reg, dataFrame)
        self.fixedRanges = const.FIXED_RANGES
        self.fPrint = self.genFprint(self.profileDetails)
        # gen fPrint and set
        

    def __str__(self):
        return super().__str__() + '\n' '\nFingerprint: ' + self.fPrint

    def storeProfile(self):
        storeDir = 'v3ProfilesFixedRanges'
        profile = {"id": self.reg,
        "profile": self.profileDetails,
        "fPrint": self.fPrint}
        outFile = open(storeDir + '/'+self.profileName+'.json', 'w')
        json.dump(profile, outFile)
        outFile.close()

    def findProfilesSameId(self, dirToCheck="v3ProfilesFixedRanges"):
        return super().findProfilesSameId(dirToCheck)

    def getPathsProfilesSameID(self, dirToCheck="v3ProfilesFixedRanges"):
        return super().getPathsProfilesSameID(dirToCheck)

    def compareProfiles(self):
        super().compareProfiles("v3ProfilesFixedRanges")

    def compareFprints(self):
        matchProfs = self.findProfilesSameId()
        if len(matchProfs) == 0:
            print("No matching profiles")
        else:
            print("{} matching profiles".format(len(matchProfs)))
            profNum = 0
            for prof in matchProfs: # print all the profiles
                profNum += 1
                print(profNum, ":\n", prof)
        profNum = 0
        for otherProf in matchProfs:
            matching = True
            profNum += 1
            print("Profile number: {}".format(profNum))
            if self.fPrint.split(".")[0] != otherProf["fPrint"].split(".")[0]:
                matching = False
                print("static portion of fingerprint does not match")
                # means first part of fprint does not match
            if self.fPrint.split(".")[1] != otherProf["fPrint"].split(".")[1]:
                # means 2ndPart does not match
                matching = False
                print("dynamic portion of fingerprint does not match")
            if matching:
                print("fingerprints match")
        return matching

    def genFprint(self, profile):
        # have static and dynamic portion to fprint
        dynamicVals = [profile[pid] for pid in profile if pid in self.dynPids]
        dynamicVals.sort()
        # list of values for dynamic vars, needs to be sorted to keep stable
        staticVals = [profile[pid] for pid in profile if pid not in self.dynPids]
        staticVals.sort()
        dynValStr = "".join([str(val) for val in dynamicVals]) # concat all in the list
        # after converting everything to a string using list comprehension
        staticValsStr = "".join([str(val) for val in staticVals])# same for static vals
        statHexDig = hashlib.sha3_224(staticValsStr.encode()).hexdigest()
        dynHexDig = hashlib.sha3_224(dynValStr.encode()).hexdigest()
        fullFprint = statHexDig+"."+dynHexDig
        return fullFprint    

    def bringDynValsToFixedBase(self):
        # bring dynamic values to a stable base using fixed ranges
        # already have dict of fixed ranges
        for pid in self.dynPids:
            baseVal = fixedRangesToFloor.find_le(self.fixedRanges[pid], self.profileDetails[pid])
            self.profileDetails[pid] = baseVal
        return True

    def bringValsToBaseAndGenFprint(self):
        if self.bringDynValsToFixedBase():
            # successfully brought to base vals
            self.fPrint = self.genFprint(self.profileDetails) # generate a new fprint
        else:
            print("Not generating a new fingerprint. Failed to bring dynamic values to correct base values")

    def compareFprintsHavePath(self, pathToProfile):
        infile = open(pathToProfile, "r")
        otherProf = json.loads(infile.read())
        infile.close()
        # self.fPrint
        matching = True
        if self.fPrint.split(".")[0] != otherProf["fPrint"].split(".")[0]:
            matching = False
            print("static portion of fingerprint does not match")
            # means first part of fprint does not match
        if self.fPrint.split(".")[1] != otherProf["fPrint"].split(".")[1]:
            # means 2ndPart does not match
            matching = False
            print("dynamic portion of fingerprint does not match")
        if matching:
            print("fingerprints match")
        return matching
