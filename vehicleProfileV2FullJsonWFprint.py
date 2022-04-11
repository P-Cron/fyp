from datetime import datetime
import hashlib
import json
import os
from constsAndHelpers import const
from processPid import processPid, getValidColumns

class VehicleProfile():
    def __init__(self, reg, dataFrame):
        now = datetime.now()
        date = now.strftime("%d-%m-%y-%H_%M%S.%f")[:-3]
        infile = open("fprintRecipes.json", "r")
        recDict = json.loads(infile.read())
        infile.close()
        self.reg = reg # need to keep the reg in order to use as an id later in the JSON
        if self.reg in recDict:
            # get the rec of the reg given
            self.dynPids = recDict[reg]['dynPids'] # and the specific list of pids as well
            
        else:
            # set to default from const file
            self.dynPids = const.DEFAULT_DYN_PIDS # and the specific list of pids as well
        possiblePids = const.STATIC_PIDS + self.dynPids

        if recDict[self.reg]["tolerances"]:
            self.toleranceDict = recDict[self.reg]["tolerances"] # if exists set it
        else:
            self.toleranceDict = const.DEFAULT_TOLERANCES # else take default tolerances
        self.profileName = reg+'_'+date
        self.profileDetails = {}
       
        pidsForVehicle = getValidColumns(dataFrame)
        usablePids = list(set(pidsForVehicle) & set(possiblePids)) # get intersection of pids vehicle supports and ones that have been set as usable
        for pid in usablePids:
            pidValue = processPid(pid, dataFrame) 
            if pidValue:
                # if returns a value then add it to the profile
                self.profileDetails[pid] = float(pidValue) # add values to dictionary for select pids
                # must convert to int in order to be able to write as JSON
        self.fPrint = self.genFprint(self.profileDetails)
        # gen fPrint and set
        

    def __str__(self):
        return self.profileName + '\n' + str(self.profileDetails) + '\nFingerprint: ' + self.fPrint

    def storeProfile(self):
        storeDir = 'v2JsonFprintProfiles'
        profile = {"id": self.reg,
        "profile": self.profileDetails,
        "fPrint": self.fPrint}
        outFile = open(storeDir + '/'+self.profileName+'.json', 'w')
        json.dump(profile, outFile)
        outFile.close()

    def findProfilesSameId(self):
        matchingProfiles = []
        with os.scandir("v2JsonProfiles") as profiles:
            for profileEntry in profiles:
                infile = open(profileEntry.path, "r")
                profileDict = json.loads(infile.read())
                infile.close()
                if profileDict["id"] == self.reg:
                    matchingProfiles.append(profileDict)
        return matchingProfiles

    def compareProfiles(self):
        matchProfs = self.findProfilesSameId()
        if len(matchProfs) == 0:
            print("No matching profiles")
        else:
            print("{} matching profiles".format(len(matchProfs)))
        profNum = 0
        for prof in matchProfs:
            entireProfMatch = True
            profNum += 1
            print("profile number {}".format(profNum))
            for pid in self.profileDetails.keys():
                if pid in self.dynPids:
                    # if a dynamic pid need to deal with possible range
                    # cannot use range function as it only takes integers
                    match = ((self.profileDetails[pid] >= prof["profile"][pid]-self.toleranceDict[pid]) and 
                    (prof["profile"][pid]+self.toleranceDict[pid] >=self.profileDetails[pid]))
               
                else:
                    match = (self.profileDetails[pid] == prof["profile"][pid]) # boolean
                if not match:
                    print(pid+' differs!')
                    entireProfMatch = False
            if entireProfMatch:
                print("profiles match")
            else:
                print("profiles do not match!")

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

    def compareFprints(self, pathToProfile):
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