import time
import pandas as pd
import matplotlib.pyplot as plt

def linkIndexFinder(analysisData):
    linkIndexList = []
    for i in range(0, len(analysisData)-1):                     # Create a list of all the indices where there is a url in the data
        if "https://github.com/" in analysisData[i]:            # So that we can know how far to go when scraping.
            linkIndexList.append(i)
    linkIndexList.append(len(analysisData))
    
    return linkIndexList
    
def extensionFinder(analysisData, linkIndexList):
    fileExtensions = []
    # This for loop navigates analysisData
    for link in range(0, len(linkIndexList)-1):
        
        if link != len(linkIndexList)-1:
            start = linkIndexList[link]+1
            finish = linkIndexList[link+1]-2
    
        else:
            start = linkIndexList[link]         
            finish = analysisData[len(analysisData)-1]

        fileExt = ''
            
        while start != finish:
            current = analysisData[start]              #begins analyzing file extension found after link in analysisData
            whiteSpaceExt = current.find(' ')          #analysisData format "fileExt_numFiles", where _ is whitespace
            
            for i in range(0, whiteSpaceExt):          #adds every character up to the whitespace
                fileExt += current[i]
            
            fileExt = fileExt.casefold()                #makes all fileExts lowercase to prevent duplicate entries
            
            if fileExt not in fileExtensions:
                fileExtensions.append(fileExt)
            
            start += 1
            fileExt = ''  
    
    return fileExtensions

def filesFinder(analysisData, linkIndexFinder, dataDict):
    
    dataDict = dataDict
    
    for link in range(0, len(linkIndexList)-1):
        
        if link != len(linkIndexList)-1:
            start = linkIndexList[link]+1
            finish = linkIndexList[link+1]-2
        
        else:
            start = linkIndexList[link]         
            finish = analysisData[len(analysisData)-1]
        
        currLink = analysisData[linkIndexList[link]]
        dataDict[currLink] = {}
                
        fileNum = ''
        fileExt = ''
        
        
        while start != finish:
            current = analysisData[start]              #begins analyzing file extension found after link in analysisData
            whiteSpaceExt = current.find(' ')          #analysisData format "fileExt_numFiles", where _ is whitespace
            whiteSpaceNum = current.rfind(' ')
            for i in range(0, whiteSpaceExt):          #adds every character up to the whitespace
                fileExt += current[i]
            for j in range(whiteSpaceNum+1, len(current)):       #diff variable used bc some Extensions had extra whitespace
                fileNum += current[j]
            
            fileExt = fileExt.casefold()                #makes all fileExts lowercase to prevent duplicate entries
            numFiles = int(fileNum)
            
            if numFiles != 0:
                dataDict[currLink][fileExt] = numFiles
            
            start += 1
            fileExt = ''
            fileNum = ''
            
    return dataDict

def repUrlList(linkIndexList, analysisData):
    repUrls = []
    
    for i in range(0, len(linkIndexList)-1):
        index = linkIndexList[i]
        repUrls.append(analysisData[index])
        
    return repUrls

# SCRIPT BEGINS HERE #

begin = time.time()

f = open("analysisData.txt", 'r')
analysisData = f.read()
analysisData = analysisData.split('\n')

fileNum = ''
fileExt = ''                 

linkIndexList = linkIndexFinder(analysisData)
print("Number of repositories:",len(linkIndexList))

start = linkIndexList[0]
last = linkIndexList[len(linkIndexList)-1]

#fileExtensions = extensionFinder(analysisData, linkIndexList)
#print("Number of file extensions:", len(fileExtensions))

dataDict = {}
    
start = linkIndexList[0]
last = linkIndexList[len(linkIndexList)-1]    
dataDict = filesFinder(analysisData, linkIndexFinder, dataDict)

# totalFiles = 0
# 
# # for key in dataDict:
# #     for nestedKey in dataDict[key]:
# #         totalFiles += dataDict[key][nestedKey]
# 
# print("Number of files in all repositories:", totalFiles)

df = pd.DataFrame.from_dict(dataDict)
df = df.transpose()

topTen = df.sum(axis=0).sort_values(ascending=False).head(10)

topTen.plot.bar()
plt.ylabel('Number of Files Found')
plt.xlabel('File Extension')
plt.title('Top 10 File Extensions')
plt.show()





df.to_csv('dictTest.csv')
    
complete = time.time()
print("Execution time:", (complete - begin), "seconds")
