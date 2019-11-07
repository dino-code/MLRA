import os
import subprocess

# Use beautiful soup to gather the links on each page
# Output a file that remembers the page last scraped
# Outer for loop that controls which page I'm on
# Inner loops that downloads the repository contained in each link


f = open("fullList.csv", "r")
urlList = f.read()
f.close()

g = open("analysisData.txt", 'a')
h = open("lastRep.txt", 'a')

urlList = urlList.split(",")

cppCounter = 0
javaCounter = 0
jsCounter = 0
htmlCounter = 0
pyCounter = 0

for i in range(0, len(urlList)-1):
    url = urlList[i]
    directory = url.split("/")
    directory = directory[4]                      #Stores name of the local directory so it can be deleted later
    g.write(directory+'\n'+url+'\n')
    
    url = url + ".git"
    os.system("git clone {}".format(url))        #Clones repository to local machine for analysis
    
    programDir = os.getcwd()
    
    os.chdir(directory)
    
    process = subprocess.run('git ls-files', shell=True, stdout = subprocess.PIPE)
    filesList = process.stdout.decode('utf-8')
    
    filesList = filesList.split('\n')

    
    for j in filesList:
        if '.cpp' in j:
            cppCounter += 1
        if '.js' in j:
            jsCounter += 1
        if '.java' in j:
            javaCounter += 1
        if '.html' in j:
            htmlCounter += 1
        if '.py' in j:
            pyCounter += 1
    
    
    os.chdir(programDir)
    os.system("rm -r " + directory)              #Deletes repository clone after analysis
    
    g.write(str(cppCounter)+'\n'+str(jsCounter)+'\n'+str(javaCounter)+'\n'+str(htmlCounter)+'\n')
    print("For " + url + ":")
    print("-------------------------------")
    print("cpp files:", cppCounter)
    print("javascript files:", jsCounter)
    print("java files:", javaCounter)
    print("html files:", htmlCounter)
    print("python files:", pyCounter)
    print("=====================")
    
    cppCounter = 0
    jsCounter = 0
    javaCounter = 0
    htmlCounter = 0                  #make a function for this
    pyCounter = 0
    
    h.write(str(i)+"\n")

g.close()
h.close()

#for i in urlList:
#    print(i)

#startPage = 'https://github.com/search?o=desc&p=1&q=language%3A+python%2C+language%3A+c%2B%2B&s=stars&type=Repositories'
#
#os.system("git clone {}".format(git_url))



# figure out how to get the rest of the links and then do a for loop to access download them all

# find a way to make python script go into each file individually within the downloaded directory


# Do all 4 million repositories and check for (py, c++) (py, js) (c++, js)
# 
# Store the list of repositories - this will be used for your more complicated searches. This is my subset.
# 
# Get this list by next week. --> Then we have to check for the foreign function interface within those files.
# Is it using IPC or FFI
# 
# Related FFI on Google - read up on it
# 
# For searching for FFI's with a list of "trigger strings" that will tell you whether an FFI was called.
# PYBIND_MODULE(...)

# Keep track of pyv8, python, c++, etc. and tag which repositories have those FFI's etc as well as the count.

#for cython, make sure it uses python code to call c++ code

# read the other paper mentioned in the paper I read





# print('Downloading file...')
# 
# 
# url = 'https://github.com/apache/arrow.git'
# 
# urllib.request.urlretrieve(url, '/Users/dinobecaj/Documents/GitScrape.git')