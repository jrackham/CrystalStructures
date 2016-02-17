"""
This method will take in the training set structure file and generate
a list of structure numbers

"""
import os
from genInput import makeInput
def getTrainingSet(filename):
    
    tmp = []
    file = open(filename)
    for line in file:
        tmp.append(int(line.split()[1]))
    
    return tmp


nums = getTrainingSet("training_set_structures.dat")

for i in nums:
    path = "structs/struct" + str(i)
    os.mkdir(path)
    makeInput(path, i)
	
    
    
