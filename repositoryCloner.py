import os
import subprocess

f = open("fullList.csv", "r")
urlList = f.read()
f.close()

g = open("analysisData.txt", 'a')

urlList = urlList.split(",")

fileDict = {}
totalDict = {}

for i in range(0, len(urlList)-1):
    url = urlList[i]
    directory = url.split("/")
    directory = directory[4]                      #Stores name of the local directory so it can be deleted later
    g.write(directory+'\n'+url+'\n')
    
    url = url + ".git"
    os.system("git clone {}".format(url))        #Clones repository to local machine for analysis
    
    programDir = os.getcwd()
    
    try:
        os.chdir(directory)
    except:
        continue
    
    process = subprocess.run('git ls-files', shell=True, stdout = subprocess.PIPE)
    filesList = process.stdout.decode('utf-8')
    
    filesList = filesList.split('\n')
    
    for j in filesList:
        if '.' in j:
            period = j.rfind('.')
            fileExt = ''
            
            for i in range(period, len(j)):
                fileExt += j[i]
            
            if fileExt != '.':
                if fileExt in fileDict:
                    totalDict[fileExt] += 1
                    fileDict[fileExt] += 1               
                else:
                    totalDict[fileExt] = 1
                    fileDict[fileExt] = 1
        
    for t in fileDict:
        g.write(t+' '+str(fileDict[t])+'\n')
        fileDict[t] = 0
            
    
    os.chdir(programDir)
    os.system("rm -r " + directory)              #Deletes repository clone after analysis

    

# This segment of code is what will go in the analysis script
sumExts = 0
critFiles = 0
for i in totalDict:
    if i == '.h' or i == '.c' or i == '.cpp' or i == '.java ' or i == '.py' or i == '.html':
        critFiles += totalDict[i]
    sumExts += totalDict[i]
    print(i, totalDict[i])

print('critical extensions', critFiles)
print('total extensions', sumExts)
print('percentage of critical files = ' + str((critFiles/sumExts)*100) +'%')
    
g.close()