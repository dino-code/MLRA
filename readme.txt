This "readme" file aims to help the reader understand how to use the programs contained within the MLSA repository.

First, the reader should understand that the purpose of the programs in the MLSA repository is to scrape GitHub to obtain the download links of several repositories so that an analysis can be run on those repositories to determine whether they are multilingual.

The "gitListGen.py" script scrapes GitHub searches of '.py', '.cpp', '.java' and '.js' for the purpose of creating a list of repository URLs that can be used to analyze files within repositories.

The "duplicateFinder.py" script was used to weed out any duplicates the first program might have generated - in the initial run, the duplicateFinder script reduced the list of URLs from 8,000 to 5,114 (yikes).

The "repositoryCloner.py" script uses the URLs from the first script to clone repositories. It does this by cloning a repository, capturing the file extensions in a dictionary, deleting the repository, and then proceeding to the next repository. The final output of the program is a "analysisData.txt" which will then be used in the next program to generate some statistics about the repositories.

Note: Some "locked" repositories are also added to the results and we still need to add a way to remove them before the analysisData.txt file is used for the next program.

The final script, "repAnalysis.py" takes the data from the repositoryCloner script and analyzes it, outputting relevant statistics to our experiment.


As of November 13, 2019 there are:
- 5,114 repositories
- 502 file extensions
- 635,884 total files

