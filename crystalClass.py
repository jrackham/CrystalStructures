# This is a class containing information about a ternary
# alloy crystal structure

#!/usr/bin/env python
import numpy as np

class Crystal:
    # lattice parameters for parent species. Al, Ga, Ni is A,B,C respectively
    # in angstrom. [a1, a2, a3]
    latticeAl = [4.04, 4.04, 4.04]
    latticeGa = [4.52, 7.66, 4.52]
    latticeNi = [3.52, 3.52, 3.52]
    
    # class constructor, takes num of atoms of species A, B, C, the three
    # lattice vectors, and a list containing atomic positions
    def __init__(self, num, concentrations, a1in, a2in, a3in, positions):
        # member data for concentrations
        self.structNum = num
        self.conA = concentrations[0] 
        self.conB = concentrations[1]
        self.conC = concentrations[2]
        self.numAtoms = A + B + C
        
        #numpy arrays for lattice basis vectors
        self.a1 = np.array(a1in)
        self.a2 = np.array(a2in)
        self.a3 = np.array(a3in)
        
    # Generates the reciprocal lattice vectors
    def reciprocalVecs():
        b1 = 2*np.pi*np.cross(a2,a3)/(np.dot(a1,np.cross(a2,a3)))
        b2 = 2*np.pi*np.cross(a3,a1)/(np.dot(a2,np.cross(a3,a1)))
        b3 = 2*np.pi*np.cross(a1,a2)/(np.dot(a3,np.cross(a1,a2)))
        return b1, b2, b3
    
    # Calculates the length of the FBZ in each of the 3 directions and divides
    # the width by the interval parameter and returns kpoint mesh
    def kpointMesh(density):
        k1 = int(density * np.linalg.norm(a1))
        k2 = int(density * np.linalg.norm(a2))
        k3 = int(density * np.linalg.norm(a3))
        return k1, k2, k3
        
    # determines a starting point lattice parameter from a concentrated
    # weighted average of nearest neighbor distances
    def latticeP():
        percentA = self.conA/self.numAtoms
        percentB = self.conB/self.numAtoms
        percentC = self.conC/self.numAtoms
        
        latPA = np.linalg.norm(latticeAL*[0.5,0.5,0])
        latPB = latticeGa[0]
        latPC = np.linalg.norm(latticeNi*[0.5, 0.5, 0])
        
        latP = percentA*latPA + percentB*latPB + percentC*latPC
        
        return latP
        
