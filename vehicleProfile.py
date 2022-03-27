from datetime import datetime
import const
import pickle
from processPid import processPid, getValidColumns

class VehicleProfile():
    def __init__(self, reg, dataFrame):
        now = datetime.now()
        date = now.strftime("%d-%m-%y-%H_%M")
        self.profileName = reg+'_'+date
        self.profileDetails = {}
        pidsForVehicle = getValidColumns(dataFrame)
        usablePids = list(set(pidsForVehicle) & set(const.USEFUL_PIDS)) # get intersection of pids vehicle supports and ones that have been set as usable
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