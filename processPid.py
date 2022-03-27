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

    else:
        # so is a dynamic pid
        # would use a match statement instead of if elses but 
        # only newer version of Python support "match" (Python's switch)
        if pid == const.RPM:
            # get where engine has heated up and remove rows where engine was not started
            newDF = (df[(df[const.COOL_TEMP] > 25 & df[const.RPM] > 0)].copy())
            return newDF[pid].min() # returns idling RPM

        elif pid == const.EGR:
            newDF = (df[(df[const.RPM] > 0)].copy())
            # engine is started
            newDF[pid].quartile(.25)
        else:
            # pid not handled
            return False
