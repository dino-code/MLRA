import os
import bs4

# Use beautiful soup to gather the links on each page
# Output a file that remembers the page last scraped
# Outer for loop that controls which page I'm on
# Inner loops that downloads the repository contained in each link


startPage = 'https://github.com/search?o=desc&p=1&q=language%3A+python%2C+language%3A+c%2B%2B&s=stars&type=Repositories'

os.system("git clone {}".format(git_url))



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