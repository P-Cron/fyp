import pandas as pd
import const

def processPid(pid, df):
    # process pid correctly from dataframe
    # rerurn false if no value, else return the value
    if pid in const.STATIC_PIDS:
        newDF = (df[(df[pid] != '-')].copy())
        if newDF.empty:
            return False
        else:
            # take from the last row
            return newDF.tail(1)[pid].values[0]

    elif pid in const.DYNAMIC_PIDS:
        # so is a dynamic pid
        # would use a match statement instead of if elses but 
        # only newer version of Python support "match" (Python's switch)
        if pid == const.RPM:
            # get where engine has heated up and remove rows where engine was not started
            newDF = df[(df[const.COOL_TEMP] > 25) & (df[const.RPM] > 0)].copy()
            return newDF[pid].median() # returns idling RPM

        elif pid == const.EGR:
            newDF = (df[(df[const.RPM] > 0)].copy())
            # engine is started
            newDF[pid] = pd.to_numeric(newDF[pid]) # convert to numeric
            return newDF[pid].quantile(.25)
        elif pid == const.VOL_EFF:
            # testDF = df[(df[const.RPM] == 0)]
            # testDf2 = df[df[const.VOL_EFF] != '-']
            # print(testDF.describe())
            # print(testDf2.describe())
            newDF = df[(df[const.RPM] == 0) & (df[const.VOL_EFF] != '-')].copy()
            # engine is not started. Often get - val so get rid of those rows
            # need to convert to numbers
            newDF[pid] = pd.to_numeric(newDF[pid])
            return newDF[pid].median()

        else:
            # pid not handled
            return False

    else:
        return False # pid not static or dynamic

def getValidColumns(df):
    validColumns = []
    for columnName in df.columns:
        # debugging
        print(columnName, "value is:", df.tail(1)[columnName].values[0])
        # print(columnName, df.tail(1)[columnName].values[0], ":equals:", "-")
        if df.tail(1)[columnName].values[0]!="-":
            validColumns.append(columnName)
    return validColumns
