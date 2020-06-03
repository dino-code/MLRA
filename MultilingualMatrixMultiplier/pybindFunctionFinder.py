#!/usr/bin/env python
# coding: utf-8

# In[328]:


import os
import sys


# In[329]:


# creates a dictionary with cpp files as keys and their paths as values
def fileFinder(path):
    fileDict = {}
    for dirpath, dirname, filename in os.walk(path):
        for z in filename:
            if '.cpp' in str(z):
                 fileDict[str(z)] = str(dirpath)
    
    return fileDict

# takes dict made in fileFinder() and searches each cpp file for PYBIND MODULE functions created.
def functionFinder(fileDict): 
    mdefList = []
    returnList = []
    
    for fileName in fileDict:
        fileObject = open(fileDict[fileName]+'/'+fileName, 'r') 
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
    trigger = triggerFinder(path)
    wordsPresent = 0
    
    # Create fileText string which contains all text from original trigger file
    fileObject = open(trigger, 'r') 
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
            wordsPresent += 1
        else:
            continue
    # Write edited fileText to original trigger file
    
    stringThree = stringOne + stringTwo
    
    if wordsPresent == 0:
        return fileText
    else:
        return stringThree


# In[330]:


mydict = fileFinder(sys.argv[1])


# In[331]:


functionNameList = functionFinder(mydict)


# In[332]:


newTriggerFile = sinkWriter(functionNameList, sys.argv[1])
triggerFile = triggerFinder(sys.argv[1])


# In[334]:


# After editing the old file, I will overwrite it
f = open(triggerFile, 'w')
f.write(newTriggerFile)
f.close()


# In[335]:


print('Executing: ' + 'python3 -m pyt -t ' + triggerFile + ' main_prog.py')
print()


# In[336]:


os.system('python3 -m pyt -t ' + triggerFile + ' main_prog.py')


# In[ ]:




