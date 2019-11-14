
f = open("analysisData.txt", 'r')
analysisData = f.read()
analysisData = analysisData.split('\n')

fileNum = ''
fileExt = ''

repAnalysis = {}                              # Stores first run-through of file extensions and numbers
repAnalysisFinal = {}                         # Stores edited version of file extensions and numbers
# a dictionary that keeps track of the number of significant Extensions
significantExtensions = {'.py': 0, '.java': 0, '.js': 0, '.cpp': 0, '.c': 0}                    

linkIndex = []

for i in range(0, len(analysisData)-1):                     # Create a list of all the indices where there is a url in the data
    if "https://github.com/" in analysisData[i]:            # So that we can know how far to go when scraping.
        linkIndex.append(i)
linkIndex.append(len(analysisData))

print("Number of repositories:",len(linkIndex))


start = linkIndex[0] + 1
last = linkIndex[len(linkIndex)-1]

for i in range(0, len(linkIndex)-1):
    if i != len(linkIndex)-1:
        start = linkIndex[i]+1
        finish = linkIndex[i+1]-2
    else:
        start = linkIndex[i]
        finish = analysisData[len(analysisData)-1]
        
    while start != finish:
        current = analysisData[start]
        whiteSpaceExt = current.find(' ')
        whiteSpaceNum = current.rfind(' ')
        for i in range(0, whiteSpaceExt):
            fileExt += current[i]
        for j in range(whiteSpaceNum+1, len(current)):
            fileNum += current[j]
        
        fileExt = fileExt.casefold()
        numFiles = int(fileNum)
        
        if fileExt in repAnalysis:
            repAnalysis[fileExt] += numFiles
        else:
            repAnalysis[fileExt] = numFiles
        
        fileExt = ''                             # reset fileExt and fileNum for the next iteration
        fileNum = ''
        
        start += 1

counter1 = 0
sumFiles1 = 0
for i in repAnalysis:
    if repAnalysis[i] > 20:
        repAnalysisFinal[i] = repAnalysis[i]
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
for i in repAnalysisFinal:
    counter2+=1
    sumFiles2 += repAnalysisFinal[i]
    if i in significantExtensions:
        significantExtensions[i] = repAnalysisFinal[i]
        
g.write("There are ")
g.write(str(counter2))
g.write(" fileExts in repAnalysisFinal\n")
g.write("There are ")
g.write(str(sumFiles2))
g.write(" total files\n\n")

print("There are", counter2, "fileExts in repAnalysisFinal")
print("There are", sumFiles2, "total files")


############
# OUTPUT SOME BASIC STATISTICS ABOUT THE REPOSITORIES

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
################################
# CREATING SQL DATABASE

# fileExtList = []
# for i in repAnalysisFinal:
#     fileExtList.append(i)
# 
# print(fileExtList)
# 
# conn = sqlite3.connect('MLRA.db')
# 
# c = conn.cursor()
# 
# 
#  
# c.execute('''CREATE TABLE files
#                ('.editorconfig', '.gitattributes', '.gitignore', '.gitmodules', '.yml', '.txt', '.md', '.cpp',
#                '.sln', '.vcxproj', '.filters', '.hpp', '.html', '.h', '.cmake', '.in', '.dox', '.sh', '.config',
#                '.cs', '.resx', '.settings', '.csproj', '.pdf', '.vb', '.vbproj', '.png', '.m4', '.w32', '.c', '.xml',
#                '.phpt', '.inc', '.ini', '.tpl', '.php', '.dsp', '.markdown', '.lock', '.gemspec', '.rb', '.bak', '.dist',
#                '.json', '.zep', '.example', '.gitkeep', '.css', '.js', '.sql', '.ttf', '.jpg', '.csv', '.mo', '.po',
#                '.phtml', '.volt', '.gyp', '.pbxproj', '.xcworkspacedata', '.m', '.am', '.vcproj', '.ico', '.docs', '.py',
#                '.xls', '.nsi', '.ac', '.xlsx', '.xcf', '.bat', '.lib', '.props', '.cmd', '.scm', '.java', '.pl', '.r',
#                '.i', '.scala', '.shtml', '.dat', '.tex', '.zip', '.rtf', '.dev', '.1', '.el', '.def', '.types', '.xlsm',
#                '.bmp', '.eps', '.wmf', '.gif', '.doc', '.xla', '.awk', '.manifest', '.map', '.rdf', '.spec', '.dsw',
#                '.conf', '.guess', '.sub', '.rc', '.mc', '.bin', '.htaccess', '.db', '.properties', '.dtd', '.2', '.3', '.4',
#                '.log', '.5', '.6', '.7', '.0', '.gz', '.ps1', '.template', '.xsl', '.tab', '.nuspec', '.docx', '.fs',
#                '.fsproj', '.cu', '.svg', '.xcscheme', '.plist', '.swift', '.xib', '.suo', '.npmignore', '.cshtml', '.yaml',
#                '.snk', '.dotsettings', '.vsct', '.vsixmanifest', '.xaml', '.cc', '.user', '.pump', '.dll', '.sample',
#                '.tt', '.exe', '.vim', '.pch', '.strings', '.rst', '.mm', '.podspec', '.xcuserstate', '.mk', '.swg',
#                '.list', '.patch', '.ml', '.mli', '.swig', '.framework', '.dylib', '.coveragerc', '.cfg', '.cxx', '.pyx',
#                '.storyboard', '.rspec', '.pem', '.project', '.vscodeignore', '.ts', '.less', '.xsd', '.vstemplate', '.pdb',
#                '.proj', '.asm', '.feature', '.opts', '.rake', '.ex', '.info', '.lua', '.nupkg', '.vspscc', '.scss',
#                '.testsettings', '.s', '.texi', '.rdoc', '._', '.mdb', '.key', '.pro', '.psd', '.hh', '.erb', '.jar', '.so',
#                '.classpath', '.prefs', '.tcc', '.ll', '.mak', '.sv', '.disabled', '.xc', '.mit', '.targets', '.ipp', '.res',
#                '.go', '.bc', '.modulemap', '.td', '.build', '.test', '.mir', '.o', '.elf-x86-64', '.a', '.macho-x86_64',
#                '.proftext', '.prof', '.output', '.obj', '.dsym', '.toml', '.rs', '.cache', '.orig', '.sor', '.hxx', '.out',
#                '.prettierrc', '.eslintignore', '.vsix', '.meta', '.mat', '.asset', '.hgignore', '.il', '.htm', '.ipch',
#                '.reference_output', '.small', '.f', '.y', '.ps', '.make', '.proto', '.wav', '.ld', '.asc', '.par',
#                '.makefile', '.mp4', '.f90', '.bats', '.bash', '.ipynb', '.pxd', '.tcl', '.dm', '.d', '.sed', '.l', '.save',
#                '.old', '.man', '.pm', '.t', '.as', '.exp', '.ds_store', '.rd', '.cproject', '.status', '.lo', '.swf',
#                '.mxml', '.pyc', '.dot', '.mp3', '.ogg', '.bundle', '.inl', '.at', '.mid', '.snippet', '.dart', '.crt',
#                '.bsd', '.diff', '.xcconfig', '.crx', '.resources', '.sch', '.sld', '.pod', '.result', '.cl', '.keep',
#                '.data', '.hx', '.spark', '.plo', '.gypi', '.pp', '.wsdl', '.datasource', '.com', '.adb', '.ads', '.pas',
#                '.idb', '.tlog', '.lastbuildstate', '.psp', '.isframe', '.17beta03', '.dfa', '.cvsignore', '.trig', '.ref',
#                '.ver', '.include', '.t4', '.qml', '.err', '.sym', '.pyd', '.oom', '.vec', '.svn', '.svn-base', '.class',
#                '.tga', '.mps', '.caches', '.history', '.eot', '.woff', '.gradle', '.xdt', '.frag', '.p7s', '.sol', '.iml',
#                '.dbk', '.4th', '.ok', '.blk', '.adoc', '.iop', '.babelrc', '.hbs', '.vue', '.mjs', '.http', '.tsx', '.woff2',
#                '.tmpl', '.pi', '.npmrc', '.h5', '.vhd', '.otf', '.node', '.tgz', '.eslintrc', '.jscsrc', '.htc', '.bowerrc',
#                '.tsv', '.jshintrc', '.jsx', '.coffee', '.cls', '.nvmrc', '.pyui', '.flow', '.jj2', '.yas-parents', '.top',
#                '.yasnippet', '.hg', '.xhtml', '.f77', '.tre', '.rsp', '.pkl', '.rsd', '.cpu', '.sm', '.em', '.sc', '.dd',
#                '.sd', '.gd', '.nd', '.od', '.cgs', '.ms', '.shellitem', '.18', '.__subject_id_sub-01', '.__subject_id_sub-02',
#                '.__subject_id_sub-03', '.__subject_id_sub-04', '.__subject_id_sub-05', '.__subject_id_sub-06',
#                '.__subject_id_sub-07', '.__subject_id_sub-08', '.__subject_id_sub-09', '.__subject_id_sub-10',
#                '.__subject_id_sub-11', '.__subject_id_sub-12', '.__subject_id_sub-13', '.__subject_id_sub-14',
#                '.__subject_id_sub-15', '.__subject_id_sub-16', '.__runcode_1', '.__runcode_2', '.__runcode_3',
#                '.__warpstats_linear0', '.__warpstats_linear1', '.__warpstats_linear2', '.__warpstats_linear3',
#                '.__warpstats_linear4', '.__warpstats_linear5', '.__warpstats_linear6', '.__warpstats_linear7',
#                '.__warpstats0', '.__warpstats1', '.__warpstats2', '.__warpstats3', '.__warpstats4', '.__warpstats5',
#                '.__warpstats6', '.__warpstats7', '.__bbrstats0', '.__bbrstats1', '.__bbrstats2', '.__bbrstats3',
#                '.__bbrstats4', '.__bbrstats5', '.__bbrstats6', '.__bbrstats7', '.__regtype_affine', '.__regtype_ants',
#                '.__fwhm_0', '.__fwhm_16', '.__fwhm_32', '.__fwhm_4', '.__fwhm_8', '._dof', '.__flameo0', '.lis', '.golden',
#                '.golden_py3', '.jst', '.apache2', '.bnf', '.cnf', '.dectest', '.mustache', '.lhpdf', '.n3', '.license',
#                '.m4a', '.md2', '.mpd', '.ejs', '.oex', '.snap', '.qext', '.pug', '.xul', '.bcmap', '.jade', '.tld',
#                '.blend', '.b64', '.co', '.jsm', '.io', '.io-client', '.flf', '.ctp', '.ors', '.gn', '.priv', '.pub')''')
# 
# conn.commit()
# conn.execute("select * from files")
# conn.close()

