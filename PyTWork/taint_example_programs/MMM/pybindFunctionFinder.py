#!/usr/bin/env python
# coding: utf-8

# In[30]:


import os
import sys
import glob


# In[91]:


# creates a list of all files of the specified extension type: 'cpp', 'py', 'pyt', etc.
def findFilesByExt(path, fileExt):
    myList = []

    for dirpath, directories, files in os.walk(path):
        myList.extend(glob.glob(dirpath+'/*.' + fileExt))
    
    return myList

# takes dict made in fileFinder() and searches each cpp file for PYBIND MODULE functions created.
def functionFinder(cppFileList): 
    mdefList = []
    returnList = []
    
    for file in cppFileList:
        fileObject = open(file, 'r') 
        fileText = fileObject.read()
        fileObject.close()
        
        if 'PYBIND11' in fileText:
            startIndex = fileText.find('m.def(')
            
            while(startIndex != -1):    
                endIndex = fileText.find(')', startIndex)
                mdefList.append(fileText[startIndex:endIndex+1])
                startIndex = fileText.find('m.def(', startIndex+5)

    returnList = mdefCleaner(mdefList)
    
    return returnList

# cleans list of mdef findings in functionFinder(fileDict)
def mdefCleaner(mdefList):
    newList = []
    for func in mdefList:
        startIndex = func.find("\"")
        endIndex = func.find("\"", startIndex+1)
        
        newList.append(func[startIndex+1:endIndex] + '(')
    
    return newList

# Will be a problem here if there are multiple trigger files
def triggerFinder(path):
    dirFiles = os.listdir(path)
    
    for file in dirFiles:
        if 'pyt' in file:
            trigger = file
        
    return trigger


def sinkWriter(functionNameList, path):
    baseTriggerFile = '/Users/dinobecaj/Documents/ComputerScienceMS/LyonsWork/MLRA/base_trigger.pyt'
    sinksAdded = 0
    
    # Create fileText string which contains all text from original trigger file
    fileObject = open(baseTriggerFile, 'r') 
    fileText = fileObject.read()
    fileObject.close()
    
    # Edit fileText by adding new sinks
    startIndex = fileText.find('sinks')
    startIndex = startIndex + 10 # We do this because .find() puts us at the index where "s" in "sinks" is located
    
    stringOne = fileText[0:startIndex]
    stringTwo = fileText[startIndex:-1]
    
    for func in functionNameList:
        if func not in fileText:
            stringTwo = '        \"' + func + '\": {},\n' + stringTwo
            sinksAdded += 1
        else:
            continue
    # Write edited fileText to original trigger file
    
    stringThree = stringOne + stringTwo
    
    if sinksAdded == 0:
        return fileText
    else:
        return stringThree

# create a function that searches through python files for mentions of the sink
# Recursive function that does the same thing at all levels of the recursion
def sinkSearcher(functionNameList, fileList):
    filesContainingFunc = []
    #trigger = '/Users/dinobecaj/Documents/ComputerScienceMS/LyonsWork/MLRA/base_trigger.pyt'
    
    for file in fileList:
        fileObject = open(file, 'r')
        fileText = fileObject.read()
        fileObject.close()
        
        for func in functionNameList:
            if func in fileText:
                filesContainingFunc.append(file)
                break
    
    return filesContainingFunc


# generates a list of python files within the program and 
def findFuncUsages(functionNameList, pythonFileList):
    filesContainingFunc = []
    
    for file in pythonFileList:
        fileObject = open(file, 'r')
        fileText = fileObject.read()
        fileObject.close()
        
        for func in functionNameList:
            if func in fileText:
                filesContainingFunc.append(file)
                break
    return filesContainingFunc
    


# In[92]:


#pythonFiles = findFilesByExt('/Users/dinobecaj/Documents/ComputerScienceMS/LyonsWork/MLRA/', 'py')
pythonFiles = findFilesByExt(sys.argv[1], 'py')


# In[93]:


# this trigger file is used while scanning any repository. An updated trigger file will be created and placed
# in the repository being analyzed along with the csv.
baseTriggerFile = '/Users/dinobecaj/Documents/ComputerScienceMS/LyonsWork/MLRA/base_trigger.pyt'


# In[94]:


#cppFiles = findFilesByExt('/Users/dinobecaj/Documents/ComputerScienceMS/LyonsWork/MLRA/', 'cpp')
cppFiles = findFilesByExt(sys.argv[1], 'cpp')
functionList = functionFinder(cppFiles)
print(functionList)


# In[95]:


#newTriggerText = sinkWriter(functionList, '/Users/dinobecaj/Documents/ComputerScienceMS/LyonsWork/MLRA/')
#newTriggerFile = baseTriggerFile = '/Users/dinobecaj/Documents/ComputerScienceMS/LyonsWork/MLRA/' +'new_base_trigger.pyt'

newTriggerText = sinkWriter(functionList, sys.argv[1])
newTriggerFile = baseTriggerFile = sys.argv[1] +'new_base_trigger.pyt'

f = open(newTriggerFile, 'w')
f.write(newTriggerText)
f.close()


# In[96]:


filesWithFuncUsages = findFuncUsages(functionList, pythonFiles)
print(filesWithFuncUsages)


# In[98]:


# this for loop runs pyt on all python files containing cpp function calls
for file in filesWithFuncUsages:
    print('Executing: ' + 'python3 -m pyt -t ' + baseTriggerFile + ' ' + file)
    print()
    os.system('python3 -m pyt -t ' + baseTriggerFile + ' ' + file)

