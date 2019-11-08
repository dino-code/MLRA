import os
import subprocess

f = open("fullList.csv", "r")
urlList = f.read()
f.close()

g = open("analysisData.txt", 'a')

urlList = urlList.split(",")

cppCounter = 0
cCounter = 0
javaCounter = 0
jsCounter = 0
htmlCounter = 0
pyCounter = 0
hCounter = 0

for i in range(1200, len(urlList)-1):
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
        j = j + " "
        if '.cpp ' in j:
            cppCounter += 1
        if '.c ' in j:
            cCounter += 1
        if '.js ' in j:
            jsCounter += 1
        if '.java ' in j:
            javaCounter += 1
        if '.html ' in j:
            htmlCounter += 1
        if '.py ' in j:
            pyCounter += 1
        if '.h ' in j:
            hCounter += 1
    
    os.chdir(programDir)
    os.system("rm -r " + directory)              #Deletes repository clone after analysis
    
    g.write(str(cppCounter)+'\n'+str(cCounter)+'\n'+str(jsCounter)+'\n'+str(javaCounter)+'\n'+str(htmlCounter)+'\n'+str(pyCounter)+'\n'+str(hCounter)+'\n')
    print("For " + url + ":")
    print("-------------------------------")
    print("cpp files:", cppCounter)
    print("c files:", cCounter)
    print("javascript files:", jsCounter)
    print("java files:", javaCounter)
    print("html files:", htmlCounter)
    print("python files:", pyCounter)
    print("header files:", hCounter)
    print("=====================")
    
    cppCounter = 0
    cCounter = 0
    jsCounter = 0
    javaCounter = 0
    htmlCounter = 0                  #make a function for this
    pyCounter = 0
    hCounter = 0

g.close()