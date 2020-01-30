# Craig Duncan (c) 2019
# This program works in the current working directory, with the 'cw' directory
# use the 'keywords.py' program first, to download the source data

import os
import re

var subdir="cw";
var taskyear="2019";

def checkWord(testword,citation,catchwords):    
    output=""
    catch=r"(?:[\w\s\S\d]*)("+testword+")(?:[\w\s\S\d]*)"
    pattern=re.compile(catch) # compile pattern
    result=pattern.match(mystring) 
    if result:
        output=catchwords
    return output

myyear=str(taskyear)
header="<html><head><title>Catchwords</title></head><body>"
result=header
startdirectory=os.getcwd()
os.chdir(subdir)

# take search term and remove case
userinput=input("Enter the search term:")
firstltr=userinput[0]
uc=firstltr.upper()
lc=firstltr.lower()
endword=userinput[1:]  # from 2nd character of string onwards
myword="["+lc+"|"+uc+"]"+endword # prepare for either case in search

# check for word in all catchword files in the cwd   
for filename in os.listdir(os.getcwd()):
    fileopen=open(filename,"r")
    mystring=fileopen.read()
    # build a file of results
    result=result+checkWord(myword,filename,mystring) 

# return to start directory and write search results to file   
os.chdir(startdirectory)
pfile=userinput+"_"+myyear+".html"
outfile=result+"</body></html>"
fileopen=open(pfile,"w")
fileopen.write(outfile)
fileopen.close()
