"""
parseStruct(string filename, int structNum)
returns structure number, lattice vector, concentrations
and atomic positions for structure of specified number in the struct_enum
file parameter
"""

import subprocess
 
def parseStruct(filename, structNum):
    
    #Excecutes the makestr command and pulls in to the stream
    p = subprocess.Popen(["makestr.x", filename,str(structNum)], stdout = subprocess.PIPE)

    #Pulls from stream into one long string
    raw = p.communicate()

    #split up the raw data by lines
    lines = raw[0].split('\n')

    #Grab the structure number
    num = int((lines[0].split())[-1])
    
     #Get the first lattice vector
    a1 = lines[2].split()
    for x in range(0,len(a1)):
        a1[x]=float(a1[x])

    #Get the second lattice vector
    a2 = lines[3].split()
    for x in range(0,len(a2)):
        a2[x] = float(a2[x])

    #Get the third lattice vector
    a3 = lines[4].split()
    for x in range(0, len(a3)):
        a3[x] = float(a3[x])

    #Get the concentrions, store in a list
    #with the form [speciesA, speciesB, speciesC]
    conc = lines[5].split()
    for x in range(0, len(conc)):
        conc[x] = int(conc[x])

    while (len(conc) < 3):
        conc.append(0)

    #Pull in the atomic positions and store in individual list
    #for each species
    positionsA = []
    positionsB = []
    positionsC = []

    for x in range(7, 7 + conc[0]):
        pos = lines[x].split()
        for y in range(0,3):
            pos[y] = float(pos[y])
    
        positionsA.append(pos)

    for x in range(7 + conc[0],7 + conc[0]+conc[1]):
        pos = lines[x].split()
        for y in range(0,3):
            pos[y] = float(pos[y])
    
        positionsB.append(pos)

    for x in range(7 + conc[0]+conc[1], 7 + conc[0] + conc[1] + conc[2]):
        pos = lines[x].split()
        for y in range(0,3):
            pos[y] = float(pos[y])
    
        positionsC.append(pos)

    return num, a1, a2, a3, conc, positionsA, positionsB, positionsC

# There may be a better way to return this data, look into it
