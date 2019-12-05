import os
import sqlite3
import pandas as pd

linkIndexList = []
wantedExtensions = ['.yml', '.txt', '.md', '.cpp', '.sln', '.hpp', '.html', '.h', '.cmake',
                    '.pdf', '.c', '.css', '.js', '.sql', '.ttf', '.jpg', '.csv', '.mo', '.po',
                    '.phtml', '.volt', '.gyp', '.py', '.xls', '.nsi', '.ac', '.xlsx', '.xcf',
                    '.bat', '.lib', '.props', '.cmd', '.scm', '.java', '.pl', '.r', '.shtml',
                    '.xlsm', '.bmp', '.eps', '.wmf', '.gif', '.doc', '.db', '.docx', '.swift',
                    '.cshtml', '.cxx', '.pyx', '.psd', '.hh', '.htm', '.pxd',  '.mxml', '.pyc',
                    '.dot', '.mp3', '.pyd', '.pyui', '.xhtml', '.m4a']

def databaseCreator():
    conn = sqlite3.connect('MLRA.db')
    c = conn.cursor()
    
    c.execute(".mode csv")
    c.execute(".import \'MLRAdata.csv\' fileExt")

def linkIndexFinder(linkIndexList, analysisData):
    for i in range(0, len(analysisData)-1):                     # Create a list of all the indices where there is a url in the data
        if "https://github.com/" in analysisData[i]:            # So that we can know how far to go when scraping.
            linkIndexList.append(i)
    linkIndexList.append(len(analysisData))
    
#def removeExts(repAnalysisEdited, wantedExtensions, repAnalysisFinal):
    
def dataNormalizer(analysisData, linkIndexList):

    normAnalysisData = [['repName', 'repUrl', '.yml', '.txt', '.md', '.cpp',
                        '.sln', '.hpp', '.html', '.h', '.cmake', '.pdf', '.c',
                        '.css', '.js', '.sql', '.ttf', '.jpg', '.csv', '.mo',
                        '.po', '.phtml', '.volt', '.gyp', '.py', '.xls', '.nsi',
                        '.ac', '.xlsx', '.xcf', '.bat', '.lib', '.props', '.cmd',
                        '.scm', '.java', '.pl', '.r', '.shtml', '.xlsm', '.bmp',
                        '.eps', '.wmf', '.gif', '.doc', '.db', '.docx', '.swift',
                        '.cshtml', '.cxx', '.pyx', '.psd', '.hh', '.htm', '.pxd',
                        '.mxml', '.pyc', '.dot', '.mp3', '.pyd', '.pyui', '.xhtml',
                        '.m4a', '.cs']]


    # This for loop navigates analysisData
    for link in range(0, len(linkIndexList)-1):
        
        row = ['', '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0]
        
        if link != len(linkIndexList)-1:
            start = linkIndexList[link]+1
            finish = linkIndexList[link+1]-2
            
            row[0] = analysisData[start - 2]
            row[1] = analysisData[start - 1]
        else:
            start = linkIndexList[link]         
            finish = analysisData[len(analysisData)-1]
            
            row[0] = analysisData[start - 1]
            row[1] = analysisData[start]
         
        
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
            
            if fileExt in normAnalysisData[0]:
                index = normAnalysisData[0].index(fileExt)
                row[index] = numFiles
                
            
#             if fileExt in normAnalysisData:
#                 repAnalysis[fileExt] += numFiles
#             else:
#                 repAnalysis[fileExt] = numFiles
            
            start += 1
            fileExt = ''
            fileNum = ''
            
        normAnalysisData.append(row)
        
        
    
    return normAnalysisData
    
    

f = open("analysisData.txt", 'r')
analysisData = f.read()
analysisData = analysisData.split('\n')

fileNum = ''
fileExt = ''

repAnalysis = {}                              # Stores first run-through of file extensions and numbers
repAnalysisEdited = {}                         # Stores edited version of file extensions and numbers
repAnalysisFinal = {}
# a dictionary that keeps track of the number of significant Extensions
significantExtensions = {'.py': 0, '.java': 0, '.js': 0, '.cpp': 0, '.c': 0}                    


linkIndexFinder(linkIndexList, analysisData)
print("Number of repositories:",len(linkIndexList))


start = linkIndexList[0]
last = linkIndexList[len(linkIndexList)-1]

# This for loop navigates analysisData
for link in range(0, len(linkIndexList)-1):
    if link != len(linkIndexList)-1:
        start = linkIndexList[link]+1
        finish = linkIndexList[link+1]-2
    else:
        start = linkIndexList[link]         
        finish = analysisData[len(analysisData)-1]
        
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
        
        if fileExt in repAnalysis:
            repAnalysis[fileExt] += numFiles
        else:
            repAnalysis[fileExt] = numFiles
        
        fileExt = ''                             # reset fileExt and fileNum for the next iteration
        fileNum = ''
        
        start += 1


### Gathering some statistics about the data
counter1 = 0
sumFiles1 = 0
for i in repAnalysis:
    if repAnalysis[i] > 20:
        repAnalysisEdited[i] = repAnalysis[i]
    sumFiles1 += repAnalysis[i]
    counter1 += 1

g = open("statistics.txt", 'w')

g.write("There are ")
g.write(str(counter1))
g.write(" fileExts in repAnalysis\n")
g.write("There are ")
g.write(str(sumFiles1))
g.write(" total files\n")

print("There are", counter1, "fileExts in repAnalysis")
print("There are", sumFiles1, "total files")
print()

counter2 = 0
sumFiles2 = 0
for i in repAnalysisEdited:
    counter2+=1
    sumFiles2 += repAnalysisEdited[i]
    if i in significantExtensions:
        significantExtensions[i] = repAnalysisEdited[i]
        
g.write("There are ")
g.write(str(counter2))
g.write(" fileExts in repAnalysisFinal\n")
g.write("There are ")
g.write(str(sumFiles2))
g.write(" total files\n\n")

print("There are", counter2, "fileExts in repAnalysisFinal")
print("There are", sumFiles2, "total files")

g.write("Percentages:\n")
g.write("---------------\n")

print()
print("Percentages:\n")
print("---------------\n")
for i in significantExtensions:
    g.write('{:<10}'.format(i))
    g.write('  %.3f' % (100*significantExtensions[i]/sumFiles2)+'%\n')
    print('{:<10}'.format(i), '  %.3f' % (100*significantExtensions[i]/sumFiles2)+'%')


g.close()

for i in repAnalysisEdited:
    if i in wantedExtensions:
        repAnalysisFinal[i] = repAnalysisEdited[i]
####################################################################

normalizedData = dataNormalizer(analysisData, linkIndexList)
columnsPd = normalizedData[0]

for i in range(2, len(columnsPd)):
    columnsPd[i] = columnsPd[i][1:]
print(columnsPd)
    
normalizedData.pop(0)

df = pd.DataFrame(normalizedData, columns = columnsPd)
df.to_csv('MLRAdata.csv')

#databaseCreator()

# create table files1 (repName TEXT, repUrl TEXT, yml INT, txt INT, md INT, cpp INT,
#                         sln INT, hpp INT, html INT, h INT, cmake INT, pdf INT, c INT,
#                         css INT, js INT, sql INT, ttf INT, jpg INT, csv INT, mo INT,
#                         po INT, phtml INT, volt, gyp INT, py INT, xls INT, nsi INT,
#                         ac INT, xlsx INT, xcf INT, bat INT, lib INT, props INT, cmd INT,
#                         scm INT, java INT, pl INT, r INT, shtml INT, xlsm INT, bmp INT,
#                         eps INT, wmf INT, gif INT, doc INT, db INT, docx INT, swift INT,
#                         cshtml INT, cxx INT, pyx INT, psd INT, hh INT, htm INT, pxd INT,
#                         mxml INT, pyc INT, dot INT, mp3 INT, pyd INT, pyui INT, xhtml INT,
#                         m4a INT, cs INT);
# 
# repName, repUrl , yml, txt, md, cpp,
#                         sln , hpp , html , h , cmake , pdf , c ,
#                         css , js , sql , ttf , jpg , csv , mo ,
#                         po , phtml , volt, gyp , py , xls , nsi ,
#                         ac , xlsx , xcf , bat , lib , props , cmd ,
#                         scm , java , pl , r , shtml , xlsm , bmp ,
#                         eps , wmf , gif , doc , db , docx , swift ,
#                         cshtml , cxx , pyx , psd , hh , htm , pxd ,
#                         mxml , pyc , dot , mp3 , pyd , pyui , xhtml ,
#                         m4a , cs 