from msilib.schema import IniFile
import pickle
class VehicleProfile():
    def __init__(self, reg, date, dataFrame):
        self.profileName = reg+'_'+date
        self.profileDetails = {}
        for pid in ['0100', '0120', '0140', '0903']:
            self.profileDetails[pid] = dataFrame.tail(1)[pid].values[0] # add values to dictionary for select pids

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