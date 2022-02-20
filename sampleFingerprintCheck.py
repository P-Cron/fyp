storedFprint = {
    '0100' : 152,
    '0120' : 152,
    'InitialRPM' : 821
}
newFprint = {
    '0100' : 152,
    '0120' : 152,
    'InitialRPM' : 792
}

def fprintsMatch(fprint1, otherFprint):
    staticKeys = ['0100', '0120']
    rangeForDynamicVals = 30 # tolerance, value can be this amount above or below

    for key in staticKeys:
        if fprint1[key] != otherFprint[key]:
            return False
    if fprint1['InitialRPM'] not in \
        range(otherFprint['InitialRPM']-rangeForDynamicVals, otherFprint['InitialRPM']+rangeForDynamicVals) :
        return False 
    return True

if __name__ == "__main__":
    if fprintsMatch(newFprint, storedFprint):
        print("fingerprints match")
    else:
        print("fingerprints do not match")