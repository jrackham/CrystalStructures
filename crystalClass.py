# This is a class containing information about a ternary
# alloy crystal structure

#!/usr/bin/env python
import numpy as np
from math import floor

class Crystal:
    # lattice parameters for parent species. Al, Ga, Ni is A,B,C respectively
    # in angstrom. [a1, a2, a3]
    latticeCo = 3.54
    latticeRe = 3.913
    latticeTi = 4.14
    
    # class constructor, takes num of atoms of species A, B, C, the three
    # lattice vectors, and a list containing atomic positions
    def __init__(self, num, a1in, a2in, a3in, concentrations, posA, posB, posC):
        # member data for concentrations
        self.structNum = num
        self.conA = concentrations[0] 
        self.conB = concentrations[1]
        self.conC = concentrations[2]
        self.numAtoms = self.conA + self.conB + self.conC
        
        #numpy arrays for lattice basis vectors
        self.a1 = np.array(a1in)
        self.a2 = np.array(a2in)
        self.a3 = np.array(a3in)

        #lists of positions
        self.pA = posA
        self.pB = posB
        self.pC = posC
        
    # Generates the reciprocal lattice vectors
    def reciprocalVecs(self):
        b1 = 2*np.pi*np.cross(self.a2,self.a3)/(np.dot(self.a1,np.cross(self.a2,self.a3)))
        b2 = 2*np.pi*np.cross(self.a3,self.a1)/(np.dot(self.a2,np.cross(self.a3,self.a1)))
        b3 = 2*np.pi*np.cross(self.a1,self.a2)/(np.dot(self.a3,np.cross(self.a1,self.a2)))
        return b1, b2, b3
    
    # Calculates the length of the FBZ in each of the 3 directions and divides
    # the width by the interval parameter and returns kpoint mesh
    def kpointMesh(self):
        # Determine the KPPA for the structure
        totalKPS = 10000 / self.numAtoms
        
        # find the magnitudes of the reciprocal lattice vectors
        Ra1, Ra2, Ra3 = self.reciprocalVecs()
        a = np.linalg.norm(Ra1)
        b = np.linalg.norm(Ra2)
        c = np.linalg.norm(Ra3)

        # Find the smallest of the three and determine the ratio
        smallest = c
        if (a < b and a < c):
            smallest = a
        elif (b < c):
            smallest = b
            
        # find the base ratios, one of these should be 1
        rA = floor(a / smallest)
        rB = floor(b / smallest)
        rC = floor(c / smallest)

        #increment the ratio up untill the closet ratio to the number of KPPA is reached
        i = 1
        kpA = rA
        kpB= rB
        kpC = rC
        while ((kpA * kpB * kpC) < totalKPS):
            kpA = rA * i
            kpB = rB * i
            kpC = rC * i
            i += 1
        tmp = str(int(kpA))+" "+str(int(kpB))+" "+str(int(kpC))

            
        return tmp
        
    # determines a starting point lattice parameter from a concentrated
    # weighted average of nearest neighbor distances
    def latticeP(self):
        percentA = self.conA / float(self.numAtoms)
        percentB = self.conB / float(self.numAtoms)
        percentC = self.conC / float(self.numAtoms)
        
        latP = percentA * self.latticeCo + percentB * self.latticeRe + percentC * self.latticeTi
        
        return latP
        
