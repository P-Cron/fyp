import pandas as pd
import constsAndHelpers.const as const

def processPid(pid, df):
    # process pid correctly from dataframe
    # return false if no value, else return the value
    newDF = df.copy()
    if pid in const.STATIC_PIDS:
        newDF = (df[(df[pid] != '-')].copy())
        if newDF.empty:
            return False
        else:
            # take from the last row
            return newDF.tail(1)[pid].values[0]

    else:
        # so is a dynamic pid
        # would use a match statement instead of if elses but 
        # only newer version of Python support "match" (Python's switch)
        if pid == const.RPM:
            # get where engine has heated up and remove rows where engine was not started
            for fixPid in [const.COOL_TEMP, const.RPM]:
                    newDF = newDF[(newDF[fixPid] != '-')].copy()
                    newDF[fixPid] = pd.to_numeric(newDF[fixPid])

            newDF = newDF[(newDF[const.COOL_TEMP] > 25) & (newDF[const.RPM] > 0)].copy()
            if newDF.empty:
                return False # if no matching rows then return False and do not use RPM
            return newDF[pid].median() # returns idling RPM, assuming vehicle had been idling for a long period

        elif pid == const.EGR:
            for fixPid in [const.EGR, const.RPM]:
                    newDF = newDF[(newDF[fixPid] != '-')].copy()
                    newDF[fixPid] = pd.to_numeric(newDF[fixPid])
            # value is more stable before engine is started as it turns out
            if not (newDF[ (newDF[const.RPM] == 0)].empty):
                # if is not empty, take rows with 0 RPM as they are more stable
                newDF = (newDF[ (newDF[const.RPM] == 0)].copy())

            if pd.isna(newDF[pid].median()):
                return newDF[pid].mode()
            return newDF[pid].median()
        elif pid == const.VOL_EFF:
           
            newDF = df[(df[const.RPM] == 0) & (df[const.VOL_EFF] != '-')].copy()
            # engine is not started. Often get - val so get rid of those rows
            # need to convert to numbers
            if newDF.empty:
                # occasionally not able to get the vol efficiency
                # so return false, as the new df will be empty
                return False
            newDF[pid] = pd.to_numeric(newDF[pid])
            if newDF[pid].median() is None:
                return newDF[pid].mode()
            return newDF[pid].median() # no need for else with return in this fashion

        elif pid == const.MPG:
            # does not especially matter when is taken
            # might as well take the median however, ignore slight fluctuations
            return newDF[pid].median()
        elif pid == const.THROT_POS:
            # want the throt pos when vehicle is not started
            newDF = (newDF[ (newDF[const.RPM] == 0)].copy()) # get when car not yet started
            # should be little variation but take the mean regardless
            return newDF[pid].median()
        else:
            # pid not handled
            return False

def getValidColumns(df):
    validColumns = []
    for columnName in df.columns:
         if df.tail(1)[columnName].values[0]!="-":
            validColumns.append(columnName)
    return validColumns
