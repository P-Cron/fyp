import json
storedFprint = {
    '0100' : 152,
    '0120' : 160,
    'InitialRPM' : 821
}
newFprint = {
    '0100' : 152,
    '0120' : 160,
    'InitialRPM' : 792
}

outfile = open("jsonFprints\\fprint1.json", "w")
fprint1Json = json.dumps(storedFprint)
outfile.write(fprint1Json)
outfile.close()
outfile = open("jsonFprints\\fprint2.json", "w")
fprint2Json = json.dumps(newFprint)
outfile.write(fprint2Json)
outfile.close()
# write out dict objs to json files for storage

def fprintsMatch(fprint, otherFprint):
    staticKeys = ['0100', '0120']
    rangeForDynamicVals = 30 # tolerance, value can be this amount above or below that is accepted

    for key in staticKeys:
        if fprint[key] != otherFprint[key]:
            return False
    if fprint['InitialRPM'] not in \
        range(otherFprint['InitialRPM']-rangeForDynamicVals, otherFprint['InitialRPM']+rangeForDynamicVals) :
        return False 
    return True

if __name__ == "__main__":
    infile = open("jsonFprints\\fprint1.json", "r")
    fprint1 = json.loads(infile.read())
    infile.close()
    infile = open("jsonFprints\\fprint2.json", "r")
    fprint2 = json.loads(infile.read())
    infile.close()
    # load in fprints from json files

    if fprintsMatch(fprint1, fprint2):
        print("fingerprints match")
    else:
        print("fingerprints do not match")