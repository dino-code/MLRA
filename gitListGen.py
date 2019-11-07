# This program generates a list of potentially multilingual repositories from Github
# This list is to be used for further research purposes

from bs4 import BeautifulSoup
import requests
import time
import random

cppLastPage = "cppLastPage.txt"
cppLastPage2 = "cppLastPage2.txt"
pyLastPage = "pyLastPage.txt"
pyLastPage2 = "pyLastPage2.txt"
jsLastPage = "jsLastPage.txt"
jsLastPage2 = "jsLastPage2.txt"
jsLastPage3 = "jsLastPage3.txt"

########################################
def lastPageChecker(searchLanguage):         
    try:
        f = open(searchLanguage, "r")
        
    except:
        f = open(searchLanguage, "w")
        f.close()
        

    if f.mode == 'r':
        contents = f.read()
        searchFrom = int(contents)
        f.close()
        f = open(searchLanguage, "w")

    else:
        searchFrom = 0
    
    return searchFrom

def pageRequest(parsePage, page, searchLanguage):
    time.sleep(int(random.random() * 20) + 1)
    response = requests.get(parsePage)
    print(response.status_code)
    print(response.headers)
    
    
    if response.status_code == 404:
        f = open(searchLanguage, "w")
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
        
        if errorCounter == 2:
            f = open(searchLanguage, "w")
            f.write(str(page))
            f.close()
            g.close()
            print()
            print("You have scraped too much and must relaunch the script.\nDon't worry, your place has been saved.")
            print()
            quit()
        else:
            errorCounter += 1
            time.sleep(61)
    
    return response

def pageParser(soup, searchLanguage, page):
    counter = 0
    for link in soup.find_all('a', class_= "v-align-middle"):
        g.write('https://github.com/'+link.text+',')
        counter += 1
        
    print(counter, "links have been added to your csv from page", page+1, "--", searchLanguage)
    print()
    
    if page == searchTo - 1:
        f = open(searchLanguage, "w")
        f.write(str(page + 1))
        f.close()
        g.close()

def webScraper(searchFrom, searchTo, lastPage, halfOne, halfTwo):
    for page in range(searchFrom, searchTo):    
        parsePage = halfOne+str(page)+halfTwo

        response = pageRequest(parsePage, page, lastPage)
     
        soup = BeautifulSoup(response.content, 'html.parser')

        pageParser(soup, lastPage, page)

#os.system("______"): list filenames command on command line to get a list of each repository's file names
#Then count the number of file types

#Feed links to download list of all

#Get small query filetype list -
        
g = open("cppRepositoryList.csv", "a")

searchFrom = lastPageChecker(cppLastPage)
increment = 90
searchTo = searchFrom + increment
halfOne = "https://github.com/search?p="
halfTwo = "&q=extension%3A+c%2B%2B+created%3A%3C2016&type=Repositories"

if searchFrom < 100:
    time.sleep(int(random.random() * 10) + 1)
    webScraper(searchFrom, searchTo, cppLastPage, halfOne, halfTwo)


g = open("cppRepositoryList.csv", "a")

searchFrom = lastPageChecker(cppLastPage2)
increment = 90
searchTo = searchFrom + increment
halfOne = "https://github.com/search?p="
halfTwo = "&q=extension%3A+c%2B%2B+created%3A%3E2016&type=Repositories"

if searchFrom < 100:
    time.sleep(int(random.random() * 10) + 1)
    webScraper(searchFrom, searchTo, cppLastPage2, halfOne, halfTwo)


g = open("pyRepositoryList.csv", "a")

searchFrom = lastPageChecker(pyLastPage)
increment = 90
searchTo = searchFrom + increment
halfOne = "https://github.com/search?p="
halfTwo = "&q=extension%3A+py+created%3A%3E2014&type=Repositories"

if searchFrom < 100:
    time.sleep(int(random.random() * 10) + 1)
    webScraper(searchFrom, searchTo, pyLastPage, halfOne, halfTwo)


g = open("pyRepositoryList.csv", "a")

searchFrom = lastPageChecker(pyLastPage2)
increment = 90
searchTo = searchFrom + increment
halfOne = "https://github.com/search?p="
halfTwo = "&q=extension%3A+py+created%3A%3C2014&type=Repositories"

if searchFrom < 100:
    time.sleep(int(random.random() * 10) + 1)
    webScraper(searchFrom, searchTo, pyLastPage2, halfOne, halfTwo)



g = open("jsRepositoryList.csv", "a")

searchFrom = lastPageChecker(jsLastPage)
increment = 90
searchTo = searchFrom + increment
halfOne = "https://github.com/search?p="
halfTwo = "&q=extension%3A+js+created%3A%3C2015&type=Repositories"

if searchFrom < 100:
    time.sleep(int(random.random() * 10) + 1)
    webScraper(searchFrom, searchTo, jsLastPage, halfOne, halfTwo)


g = open("jsRepositoryList.csv", "a")

searchFrom = lastPageChecker(jsLastPage2)
increment = 90
searchTo = searchFrom + increment
halfOne = "https://github.com/search?p="
halfTwo = "&q=extension%3A+js++created%3A%3E2017&type=Repositories"

if searchFrom < 100:
    time.sleep(int(random.random() * 10) + 1)
    webScraper(searchFrom, searchTo, jsLastPage2, halfOne, halfTwo)


g = open("jsRepositoryList.csv", "a")

searchFrom = lastPageChecker(jsLastPage3)
increment = 90
searchTo = searchFrom + increment
halfOne = "https://github.com/search?p="
halfTwo = "&q=extension%3A+js++created%3A2016+created%3A2015&type=Repositories"

if searchFrom < 100:
    time.sleep(int(random.random() * 10) + 1)
    webScraper(searchFrom, searchTo, jsLastPage3, halfOne, halfTwo)

print("Program has completed its intended function.")

