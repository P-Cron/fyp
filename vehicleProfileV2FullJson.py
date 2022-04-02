from datetime import datetime
import json
from constsAndHelpers import const
import pickle
from processPid import processPid, getValidColumns

class VehicleProfile():
    def __init__(self, reg, dataFrame):
        now = datetime.now()
        date = now.strftime("%d-%m-%y-%H_%M")
        infile = open("fprintRecipes.json", "r")
        recipes = infile.read()
        recDict = json.loads(recipes)
        infile.close()
        if reg in recDict:
            # get the rec of the reg given
            dynPids = recDict[reg]['dynPids'] # and the specific list of pids as well
            possiblePids = const.STATIC_PIDS + dynPids
        else:
            # set to default from const file
            possiblePids = const.DEFAULT_USEFUL_PIDS
        self.profileName = reg+'_'+date
        self.profileDetails = {}
        pidsForVehicle = getValidColumns(dataFrame)
        usablePids = list(set(pidsForVehicle) & set(possiblePids)) # get intersection of pids vehicle supports and ones that have been set as usable
        for pid in usablePids:
            pidValue = processPid(pid, dataFrame) 
            if pidValue:
                # if returns a value then add it to the profile
                self.profileDetails[pid] = pidValue # add values to dictionary for select pids


    def __str__(self):
        return self.profileName + '\n' + str(self.profileDetails)

    def storeProfile(self):
        storeDir = 'pickledProfiles'
        outFile = open(storeDir + '\\'+self.profileName+'.pkl', 'wb')
        pickle.dump(self, outFile)
        outFile.close()

    def compareProfiles(self, otherProfile):
        # naive impl currently
        for pid in self.profileDetails.keys():
            if self.profileDetails[pid] == otherProfile.profileDetails[pid]:
                print(pid+' matches')
            else:
                print(pid+' differs!')

def loadProfile(pklFile):
    inFile = open(pklFile, 'rb')
    loadedProfile = pickle.load(inFile)
    inFile.close()
    return loadedProfile