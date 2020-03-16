#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import subprocess
from os import walk
from multiprocessing import Pool


# In[ ]:


def listMaker(urlList):
    newUrlList = []
    
    for repository in range(0, len(urlList)-1):
        currUrl = urlList[repository]
        directory = currUrl.split("/")      
     
        try:
            newUrlList.append(directory[len(directory)-1])     #Stores name of the repository so it can be deleted later
        except:
            continue
    
    return newUrlList

def keywordSearcher(keyword):
            process = subprocess.run(f'grep -n \'{keyword}\' {file} | cut -f1 -d:', shell=True, stdout = subprocess.PIPE)
            output = process.stdout.decode('utf-8')
        
            #If there is a keyword match, append the file and line to grep list.
            if output != "":
                output = keyword+"^^^"+file+"^^^"+output
                return output

def multCallsPerFileSearcher(filesList, ffiList):      
    for file in filesList:
        outputList = []
        
        pool = Pool(5)
        output = pool.map(keywordSearcher, ffiList)
        pool.close()
        pool.join()
        
        counter = 0
        for i in output:
            if i == "":
                counter += 1
            else:
                outputList.append(i)
        if counter < 3:
            return outputList
                
    return ["No files with multiple foreign function calls."]

def searchEngine(ffiList, repository):
    mainDir = "/Users/dinobecaj/LocalDocuments/LyonsDB/"
    multCallsPerFileDict = {}

    returnList = []

    os.chdir(mainDir)

    for (dirpath, dirnames, filenames) in walk(mainDir+repository):
    
        os.chdir(dirpath)
        
        returnList = multCallsPerFileSearcher(filenames, ffiList)
        if returnList != ['No files with multiple foreign function calls.']:
            if progDir in multCallsPerFileDict.keys():
                multCallsPerFileDict[repository].append(returnList)
            else:
                multCallsPerFileDict[repository] = returnList

    os.system(f"cd {mainDir}")

    return multCallsPerFileDict


# In[3]:


f = open("newFullList.csv", "r")
urlList = f.read()
f.close()
urlList = urlList.split(',')
#programDir = os.getcwd()


# In[4]:


ffiList = ["cythonize(", "Py_initialize(", "pyObject", "PYBIND11_MODULE(", "FFI()"]
#Tester ffiList = ["generate", "use"]
# IMPORTANT: Make sure I run a test to find other FFI's between other languages like Javascript


# In[5]:


repList = listMaker(urlList)
#test = [1,2,3,4,5,6,7,8,9,10]


# In[6]:


counter = 0
length = 1
for rep in range(0, length):
    print(f"Now analyzing: {repList[rep]}")
    multCallsPerFileDict = searchEngine(ffiList, repList[rep])
    counter+=1
    print(f"Progress: {counter}/{length}")
print("Done. Thank you!")


# In[7]:


print(multCallsPerFileDict)


# In[ ]:


#mainDir = "/Users/dinobecaj/LocalDocuments/LyonsDB/"
#fileDict = {}

#os.system(f"cd {mainDir}")
#for rep in repList:
    
  #  files = []
   # paths = []
    #for (dirpath, dirnames, filenames) in walk(mainDir+rep):
    #    returnList = multCallsPerFileSearcher(filenames, ffiList)
    #    if returnList != ["No files with multiple foreign function calls."]:
    #        multCallsPerFileDict["rep"] = returnList
     #       print("Score!")
            
      #  files.extend(filenames)
       # paths.extend(dirpath)
    
    #fileDict[rep] = (paths, files) 
    
    
    #os.system(f"cd {mainDir}")


# In[ ]:


# DOWNLOADER

#programDir = "/Users/dinobecaj/Documents/ComputerScienceMS/LyonsDB/"    #saves the main directory we are working from

#counter = 0
#for repository in range(0, len(urlList)-1):
 #   currUrl = urlList[repository]
  #  directory = currUrl.split("/")      
     
   # try:
    #    directory = directory[len(directory)-1]     #Stores name of the repository so it can be deleted later
#    except:
 #       continue

  #  currUrl = currUrl + ".git"
    
   # try:
    #    os.system(f"git clone {currUrl}")        #Clones repository to local machine for analysis 
     #   print("Downloading repository...")
    #except:
     #   continue
        
#    os.chdir(programDir)

 #   counter += 1                           #counter keeps track of script progress

  #  print(f"Progress: {counter}/{len(urlList)}")
#print("Done.")


# In[ ]:


g = open("results.csv", "w")

for i in multCallsPerFileDict:
    g.write(i+",")
    g.write(multCallsPerFileDict[i]+"\n")
    
g.close()
    

