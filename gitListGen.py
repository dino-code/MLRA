# This program generates a list of potentially multilingual repositories from Github
# This list is to be used for further research purposes

from bs4 import BeautifulSoup
import requests
import time
import random


cPage = "cLastPage.txt"
pPage = "pLastPage.txt"
jPage = "jLastPage.txt"

listFile = "repositoryList.csv"

def fileOpener(pageTracker, listFile):
    try:
        f = open("lastPage.txt", "r")
    
    except:
        f = open("lastPage.txt", "w")
    

    if f.mode == 'r':
        contents = f.read()
        searchFrom = int(contents)
        f.close()
        f = open("lastPage.txt", "w")

    else:
        searchFrom = 0
    
    return searchFrom

def pageParser(soup):
    counter = 0
    for link in soup.find_all('a', class_= "v-align-middle"):
        g.write('https://github.com/'+link.text+',')
        counter += 1
        
    print(counter, "links have been added to your csv from page", page+1)
    print()
    
    if page == searchTo - 1:
        f.write(str(page + 1))
    
def pageRequest(webPage):
    time.sleep(int(random.random() * 10) + 1)
    response = requests.get(parsePage)
    print(response.status_code)
    print(response.headers)
    
    
    if response.status_code == 404:
        f.write(str(page))
        f.close()
        g.close()
        print()
        print("You have scraped too much and must relaunch the script.\nDon't worry, your place has been saved.")
        print()
        quit()
    
    errorCounter = 0
    
    while response.status_code == 429:
        response = requests.get(parsePage)
        print(response.status_code)
        print(response.headers)

        if response.status_code == 429:
            if (int(response.headers['Retry-After']) > 61) or (errorCounter == 3):
                f.write(str(page))
                f.close()
                g.close()
                print()
                print("You have scraped too much and must relaunch the script.\nDon't worry, your place has been saved.")
                print()
                quit()
            else:
                errorCounter += 1
                time.sleep(int(response.headers['Retry-After']))
    return response

######################################## OPENING FILES
searchFrom = fileOpener(cPage, listFile)

g = open(listFile, "a")

increment = 3
searchTo = searchFrom + increment

#######################################
#Do individual searches
#Do extension cpp and c++, js  py, but do them separately
#Should get 5 or 6 thousand repositories

#os.system("______"): list filenames command on command line to get a list of each repository's file names
#Then count the number of file types

#Feed links to download list of all

#Get small query filetype list -


##### WEBPAGE REQUESTS

for page in range(searchFrom, searchTo):    
    parsePage = 'https://github.com/search?p='+str(page)+'&q=git+extension%3A.py+extension%3A.cpp+extension%3A.js&type=Repositories'

    response = pageRequest(parsePage)
    
    
####### WEBPAGE PARSING    
    soup = BeautifulSoup(response.content, 'html.parser')

    pageParser(soup)
    

f.close()
    
g.close()

# Need to do 3 different searches
# Output 3 different csv files with the results