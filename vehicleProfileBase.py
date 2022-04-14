from datetime import datetime
import os
import json
from constsAndHelpers import const
from processPid import processPid, getValidColumns

class VehicleProfileBase():
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

    def __str__(self):
        return self.profileName + '\n' + str(self.profileDetails)

    def findProfilesSameId(self, dirToCheck="v1JsonProfiles"):
        matchingProfiles = []
        with os.scandir(dirToCheck) as profiles:
            for profileEntry in profiles:
                infile = open(profileEntry.path, "r")
                profileDict = json.loads(infile.read())
                infile.close()
                if profileDict["id"] == self.reg:
                    matchingProfiles.append(profileDict)
        return matchingProfiles

    def getPathsProfilesSameID(self, dirToCheck="v1JsonProfiles"):
        # returns a list of paths of profiles with the same ID (reg number)
        matchingProfilePaths = []
        with os.scandir(dirToCheck) as profiles:
            for profileEntry in profiles:
                infile = open(profileEntry.path, "r")
                profileDict = json.loads(infile.read())
                infile.close()
                if profileDict["id"] == self.reg:
                    matchingProfilePaths.append(profileEntry.path)
        return matchingProfilePaths

        
    def compareProfiles(self, dirToCheck):
        matchProfs = self.findProfilesSameId(dirToCheck)
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