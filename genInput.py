import crystalClass
from parseStruct import parseStruct

def genInput(structNum):
    num, a1, a2, a3, conc, positionsA, positionsB, positionsC = parseStruct("struct_enum.out", structNum)
    x = crystalClass.Crystal(num, a1, a2, a3, conc, positionsA, positionsB, positionsC)

    inputFilename = "CoReTi_struct" + str(x.structNum) + ".in"

    inFile = open(inputFilename,'w')

    inFile.write('&control\n')
    inFile.write('   verbosity=\'debug\'\n')
    inFile.write('   calculation=\'vc-relax\'\n')
    inFile.write('   restart_mode=\'from_scratch\',\n')
    inFile.write('   pseudo_dir = \'/fslhome/jmrackha/fsl_groups/fslg_byui_materials/pslibrary.1.0.0/pbe/PSEUDOPOTENTIALS\',\n')
    inFile.write('   outdir=\'./\',\n')
    inFile.write('   prefix=\'CoReTi\'\n')
    inFile.write('   tprnfor = .true.\n')
    inFile.write('   tstress = .true.\n')
    inFile.write('/\n')

    inFile.write('&system\n')
    inFile.write('   ibrav=0, celldm(1)='+str(x.latticeP())+', nat='+str(x.numAtoms)+', ntyp= 3, ecutwfc= 40.0,\n')
    inFile.write('   occupations=\'smearing\', smearing=\'mp\', degauss=0.2, nspin=2, starting_magnetization(3)=0.7,\n')
    inFile.write('   lda_plus_u = .false.\n')
    inFile.write('/\n')

    inFile.write('&electrons\n')
    inFile.write('   conv_thr = 1.D-6\n')
    inFile.write('   diagonalization=\'david\'\n')
    inFile.write('!   mixing_beta = 0.3')
    inFile.write('/\n')

    inFile.write('&ions\n')
    inFile.write('/\n')

    inFile.write('&cell\n')
    inFile.write('!cell_dynamics = \'bfgs\'\n')
    inFile.write('press = 0.00,\n')
    inFile.write('wmass = 0.007,\n')
    inFile.write('/\n')
    inFile.write('\n')
    inFile.write('CELL_PARAMTERS angstrom\n')
    inFile.write(str(x.a1)[1:-1] + '\n')
    inFile.write(str(x.a2)[1:-1] + '\n')
    inFile.write(str(x.a3)[1:-1] + '\n')
    inFile.write('\n')
    inFile.write('ATOMIC_SPECIES\n')
    for a in x.pA:
        inFile.write('Co ' + str(a)[1:-1].replace(',','') + '\n')
    
    for b in x.pB:
        inFile.write('Re ' + str(b)[1:-1].replace(',','') + '\n')

    for c in x.pC:
        inFile.write('Ti ' + str(c)[1:-1].replace(',','') + '\n')

    inFile.write('\n')
    inFile.write('K_POINTS automatic\n')
    inFile.write(x.kpointMesh() + ' 0 0 0')
