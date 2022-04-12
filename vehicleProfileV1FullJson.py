from datetime import datetime
import json
import os
from vehicleProfileBase import VehicleProfileBase 

class VehicleProfile(VehicleProfileBase):
    def __init__(self, reg, dataFrame):
        super().__init__(reg, dataFrame)

    def __str__(self):
        return super().__str__()

    def storeProfile(self):
        storeDir = 'v1JsonProfiles'
        profile = {"id": self.reg,
        "profile": self.profileDetails}
        outFile = open(storeDir + '\\'+self.profileName+'.json', 'w')
        json.dump(profile, outFile)
        outFile.close()

    def findProfilesSameId(self, dirToCheck="v1JsonProfiles"):
        return super().findProfilesSameId(dirToCheck)

    def compareProfiles(self):
        super().compareProfiles("v1JsonProfiles")
            
