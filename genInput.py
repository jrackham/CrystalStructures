#!/usr/bin/env python

"""
This function will take in template file and file containing a list of which
structures to generate quantum espresso input files. Each file will be saved
in its own folder and 
"""
import crystalClass.py
import parseStruct.py

workinglist = open(template.in).read().split()

options = {"#lattice": struct.latticeP(),
           "#numAtoms": struct.numAtoms,
           "#a1": struct.a1,
           "#a2": struct.a2,
           "#a3": struct.a3,
           "#positionsA": "Co ",
           "#positionsB": "Re ",
           "#positionsC": "Ti ",}
               
