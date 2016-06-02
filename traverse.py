import subprocess as subp
import os

startDir = '/fslhome/jmrackha/compute/CoReTi/structs'
for dirName, subdirList, fileList in os.walk(startDir): 
    foundLock = False
    for fname in fileList: 
        if(fname == 'lock.out'):
            foundLock = True
           
    if (foundLock == False):
        print("Currently in: " + dirName)
        os.chdir(dirName)
        #os.system("touch lock.out")
        child = subp.Popen("touch lock.out", shell=True)
        os.waitpid(child.pid, 0)
        #os.system("cp CoReTi* running.in")
        child = subp.Popen("cp CoReTi* running.in", shell=True)
        os.waitpid(child.pid, 0)
        print("Starting QE run")
        #os.system("pw.x <running.in  >ran1.out")
        child = subp.Popen("pw.x <running.in >run1.out", shell=True)
        os.waitpid(child.pid, 0)

    if 'CoReTi.save' in subdirList:
        subdirList.remove('CoReTi.save')
