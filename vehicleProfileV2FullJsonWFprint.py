import hashlib
import json
from vehicleProfileBase import VehicleProfileBase
class VehicleProfile(VehicleProfileBase):
    def __init__(self, reg, dataFrame):
        super().__init__(reg, dataFrame)

        self.fPrint = self.genFprint(self.profileDetails)
        # gen fPrint and set
        

    def __str__(self):
        return super().__str__() + '\n' '\nFingerprint: ' + self.fPrint

    def storeProfile(self):
        storeDir = 'v2JsonFprintProfiles'
        profile = {"id": self.reg,
        "profile": self.profileDetails,
        "fPrint": self.fPrint}
        outFile = open(storeDir + '/'+self.profileName+'.json', 'w')
        json.dump(profile, outFile)
        outFile.close()
 
    def findProfilesSameId(self, dirToCheck="v2JsonFprintProfiles"):
        return super().findProfilesSameId(dirToCheck)

    def getPathsProfilesSameID(self, dirToCheck="v2JsonFprintProfiles"):
        return super().getPathsProfilesSameID(dirToCheck)


    def compareProfiles(self):
        super().compareProfiles("v2JsonFprintProfiles")

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

    def tryBringDynValsToOther(self, pathToProfile):
        # bring dynamic values to a stable base from another profile
        # return true of False depending on successful or not
        infile = open(pathToProfile, "r")
        otherProf = json.loads(infile.read())
        infile.close()
        # already have dict of tolerances
        success = True # true by default
        for pid in self.dynPids:
            inRange = ((self.profileDetails[pid] >= otherProf["profile"][pid]-self.toleranceDict[pid]) and 
                    (otherProf["profile"][pid]+self.toleranceDict[pid] >=self.profileDetails[pid]))
            if inRange:
                self.profileDetails[pid] = otherProf["profile"][pid]# set to the previous val
            else:
                print("{} is out of range. \n Correct val: {}\nGiven val: {}\nRange: {}".format(
                    pid, otherProf["profile"][pid], self.toleranceDict[pid]))
                success = False
        return success

    def bringValsToBaseAndGenFprint(self, pathToProfile):
        if self.tryBringDynValsToOther(pathToProfile):
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
