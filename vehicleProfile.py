class VehicleProfile():
    def __init__(self, reg, date, dataFrame):
        self.profileName = reg+'_'+date
        self.profileDetails = {}
        for pid in ['0100', '0120', '0140', '0903']:
            self.profileDetails[pid] = dataFrame.tail(1)[pid].values[0] # add values to dictionary for select pids

    def __str__(self):
        return self.profileName + '\n' + str(self.profileDetails)

