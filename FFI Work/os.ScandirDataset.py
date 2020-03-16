#!/usr/bin/env python
# coding: utf-8

# In[143]:


import os
import subprocess
from os import scandir


# In[149]:


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

def multCallsPerFileSearcher(file, ffiList):      
    foundItems = []            #List of file and grep output
    foundKeywords = []
        
    for ffiString in ffiList:
        process = subprocess.run(f'grep -n \'{ffiString}\' {file} | cut -f1 -d:', shell=True, stdout = subprocess.PIPE)
        output = process.stdout.decode('utf-8')
        
        #If there is a keyword match, append the file and line to grep list.
        if output != "":
            foundItems.append(ffiString+"^^^"+file+"^^^"+output)
            foundKeywords.append(ffiString)
            if len(foundKeywords) > 1:
                return foundItems
                
    return ["No presence of multiple foreign function calls."]

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

def subdirs(path):
    """Yield directory names not starting with '.' under given path."""
    folders = []
    for entry in os.scandir(path):
        if not entry.name.startswith('.') and entry.is_dir():
            folders.append(entry.name)
    return folders

def fileListMaker(scandir):
    fileList = []
    for i in scandir:
        if not i.name.startswith('.') and i.is_dir() and i != ".git" and i != ".gitignore":
            continue
        else:
            fileList.append(i.name)
    return fileList

def walker(path, ffiList):    
    fileList = fileListMaker(scandir(path))
    result = []
    
    for file in fileList:
        result.extend(multCallsPerFileSearcher(path+file, ffiList))
    
    subFolders = subdirs(path)
    if len(subFolders) > 1:
        for folder in subFolders:
            result += (walker(path+folder+"/", ffiList))
    
    return result


# In[150]:


f = open("newFullList.csv", "r")
urlList = f.read()
f.close()
urlList = urlList.split(',')
#programDir = os.getcwd()


# In[151]:


ffiList = ["cythonize(", "Py_initialize(", "pyObject", "PYBIND11_MODULE(", "FFI()"]
#Tester ffiList = ["tool", "both"]
repList = listMaker(urlList)


# In[152]:


path = "/Users/dinobecaj/LocalDocuments/LyonsDB/PHP-CPP"

fileList = fileListMaker(scandir(path))
print(fileList)


# In[ ]:


result = {}
counter = 0
for rep in range(0, 5):
    print(f"{counter+1}. Analyzing {repList[rep]}...")
    path="/Users/dinobecaj/LocalDocuments/LyonsDB/"+repList[rep]+"/"

    allResults = walker(path, ffiList)

    resultList = []
    for res in allResults:
        if res != 'No presence of multiple foreign function calls.':
            resultList.append(res)
    result[repList[rep]] = resultList
    counter +=1
    
print(result)


# In[ ]:




