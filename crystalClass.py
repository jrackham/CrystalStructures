import numpy as np
# This is a class containing information about a ternary
# alloy crystal structure
class Crystal:
   # lattice parameters for parent species. Al, Ga, Ni is A,B,C respectively
   # in angstrom. [a1, a2, a3]
    latticeAl = [4.04, 4.04, 4.04]
    latticeGa = [4.52, 7.66, 4.52]
    latticeNi = [3.52, 3.52, 3.52]
    
    def __init__(self, A, B, C, a1in, a2in, a3in, positions):
        self.conA = A 
        self.conB = B
        self.conC = C
        
        #numpy arrays
        self.a1 = a1in
        self.a2 = a2in
        self.a3 = a3in
        
    def reciprocalVecs():
        b1 = 2*np.pi*np.cross(a2,a3)/(np.dot(a1,np.cross(a2,a3))
        b2 = 2*np.pi*np.cross(a3,a1)/(np.dot(a2,np.cross(a3,a1))
        b3 = 2*np.pi*np.cross(a1,a2)/(np.dot(a3,np.cross(a1,a2))