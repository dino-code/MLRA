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


December 4, 2019

To import data frame csv from repAnalysis.py to sqlite3, simply type commands ".mode csv" and then ".import MLRAdata.csv files1". Once that is done, you must create a new table called files:

CREATE TABLE files (repName, repUrl , yml, txt, md, cpp,
                        sln , hpp , html , h , cmake , pdf , c ,
                        css , js , sql , ttf , jpg , csv , mo ,
                        po , phtml , volt, gyp , py , xls , nsi ,
                        ac , xlsx , xcf , bat , lib , props , cmd ,
                        scm , java , pl , r , shtml , xlsm , bmp ,
                        eps , wmf , gif , doc , db , docx , swift ,
                        cshtml , cxx , pyx , psd , hh , htm , pxd ,
                        mxml , pyc , dot , mp3 , pyd , pyui , xhtml ,
                        m4a , cs);

Then do:

INSERT INTO files (repName, repUrl , yml, txt, md, cpp,
                        sln , hpp , html , h , cmake , pdf , c ,
                        css , js , sql , ttf , jpg , csv , mo ,
                        po , phtml , volt, gyp , py , xls , nsi ,
                        ac , xlsx , xcf , bat , lib , props , cmd ,
                        scm , java , pl , r , shtml , xlsm , bmp ,
                        eps , wmf , gif , doc , db , docx , swift ,
                        cshtml , cxx , pyx , psd , hh , htm , pxd ,
                        mxml , pyc , dot , mp3 , pyd , pyui , xhtml ,
                        m4a , cs) SELECT repName, repUrl , yml, txt, md, cpp,
                        sln , hpp , html , h , cmake , pdf , c ,
                        css , js , sql , ttf , jpg , csv , mo ,
                        po , phtml , volt, gyp , py , xls , nsi ,
                        ac , xlsx , xcf , bat , lib , props , cmd ,
                        scm , java , pl , r , shtml , xlsm , bmp ,
                        eps , wmf , gif , doc , db , docx , swift ,
                        cshtml , cxx , pyx , psd , hh , htm , pxd ,
                        mxml , pyc , dot , mp3 , pyd , pyui , xhtml ,
                        m4a , cs FROM files1;

QUERY FOR SQL STATS:


CREATE VIEW programmingLanguageStats AS

SELECT round((SUM(CAST(cpp AS FLOAT))/(SUM(CAST(py AS FLOAT))+ SUM(CAST(java AS FLOAT)) + SUM(CAST(js AS FLOAT))
                                 + SUM(CAST(cs AS FLOAT)) + SUM(CAST(c AS FLOAT)) + SUM(CAST(cpp AS FLOAT))
                                 )), 4)*100 AS "C++ Percent",
round((SUM(CAST(py AS FLOAT))/(SUM(CAST(py AS FLOAT))+ SUM(CAST(java AS FLOAT)) + SUM(CAST(js AS FLOAT))
                                 + SUM(CAST(cs AS FLOAT)) + SUM(CAST(c AS FLOAT)) + SUM(CAST(cpp AS FLOAT))
                                 )), 4)*100 AS "Python Percent",
round((SUM(CAST(cs AS FLOAT))/(SUM(CAST(py AS FLOAT))+ SUM(CAST(java AS FLOAT)) + SUM(CAST(js AS FLOAT))
                                 + SUM(CAST(cs AS FLOAT)) + SUM(CAST(c AS FLOAT)) + SUM(CAST(cpp AS FLOAT))
                                 )), 4)*100 AS "C Sharp Percent",
round((SUM(CAST(java AS FLOAT))/(SUM(CAST(py AS FLOAT))+ SUM(CAST(java AS FLOAT)) + SUM(CAST(js AS FLOAT))
                                 + SUM(CAST(cs AS FLOAT)) + SUM(CAST(c AS FLOAT)) + SUM(CAST(cpp AS FLOAT))
                                 )), 4)*100 AS "Java Percent",
round((SUM(CAST(js AS FLOAT))/(SUM(CAST(py AS FLOAT))+ SUM(CAST(java AS FLOAT)) + SUM(CAST(js AS FLOAT))
                                 + SUM(CAST(cs AS FLOAT)) + SUM(CAST(c AS FLOAT)) + SUM(CAST(cpp AS FLOAT))
                                 )), 4)*100 AS "Javascript Percent",
round((SUM(CAST(c AS FLOAT))/(SUM(CAST(py AS FLOAT))+ SUM(CAST(java AS FLOAT)) + SUM(CAST(js AS FLOAT))
                                 + SUM(CAST(cs AS FLOAT)) + SUM(CAST(c AS FLOAT)) + SUM(CAST(cpp AS FLOAT))
                                 )), 4)*100 AS "C Percent"

FROM files1;

SELECT * FROM programmingLanguageStats;


CREATE VIEW totalFilesStats AS

SELECT round((SUM(CAST(a.cpp AS FLOAT))/(SUM(CAST(b.total AS FLOAT))
                                 )), 10)*100 AS "C++ Percent",
round((SUM(CAST(py AS FLOAT))/(SUM(CAST(b.total AS FLOAT))
                                 )), 10)*100 AS "Python Percent",
round((SUM(CAST(cs AS FLOAT))/(SUM(CAST(b.total AS FLOAT))
                                 )), 10)*100 AS "C Sharp Percent",
round((SUM(CAST(java AS FLOAT))/(SUM(CAST(b.total AS FLOAT))
                                 )), 10)*100 AS  "Java Percent",
round((SUM(CAST(js AS FLOAT))/(SUM(CAST(b.total AS FLOAT))
                                 )), 10)*100 AS  "Javascript Percent",
round((SUM(CAST(c AS FLOAT))/(SUM(CAST(b.total AS FLOAT))
                                 )), 10)*100 AS  "C Percent"

FROM files1 a, totalFiles b;

SELECT * FROM totalFilesStats;
