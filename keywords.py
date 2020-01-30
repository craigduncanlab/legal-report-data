# Craig Duncan
# (c) Craig Duncan 2019
# Last updated 29 August 2019
# This works with the austlii classic site
# http://www.austlii.edu.au/cgi-bin/sinosrch.cgi?method=auto&query=2019+wasc

import urllib.request
import re
from urllib.request import FancyURLopener

WAcases="/cases/wa/WASC/";
WAquery="method=auto&query=2019+wasc"

#
fp = urllib.request.urlopen("http://www.austlii.edu.au/cgi-bin/sinosrch.cgi?"+WAquery)
mybytes = fp.read()
myinfo=fp.info()
mystr = mybytes.decode("utf8")  # check this in header
fp.close()
print(mystr)
print(mystr.len)
exit(0)

#start here for file functions
Main("2019",92);


# always define python functions in the file before you need them
def getURLstring(case, year):
    caseID=str(case)
    print("Start of: "+caseID)
    #mystr2="http://www.austlii.edu.au/cgi-bin/viewdoc/au/cases/wa/WASC/2019/"+mycase+".html"
    mystr2="http://classic.austlii.edu.au/cgi-bin/sinodisp/au"+WAcases+year+"/"+caseID+".html"
    print("Now: "+mystr2)
    page=myopener.open(mystr2)
    mydownload=page.read()
    mycase=mydownload.decode("utf8")
    myopener.close()
    # print(austcase)
    print("End of: "+caseID)
    return mycase

# use the citation in a case as the filename
def writecase(austcase):
    citestring=r"(?:[\w\s\S\d]*)(\[2019\] WASC[\d ]+)(?:[\<\w\s\S\d]*)"
    casepattern=re.compile(citestring) # compile pattern
    citeresult=casepattern.match(austcase) # use pattern to match on worddata (string)
    if citeresult:
        print ("---match---")
        #print (result.group(0))
        print (citeresult.group(1))  # use the match as filename
        filename="./cases/"+str(citeresult.group(1))+".html"
        fileopen=open(filename,"w")
        fileopen.write(austcase)
        fileopen.close()
    return citeresult

# (.*?)word(.*?)
# lazy match on first, positive lookahead for Legislation: if match does not advance past it
def getCatchWords(caseref,austcase):
    catchpattern=r"(?:[\w\s\S\d]*)(\<a name=\"CatchwordsText\"[\<\w\s\S\d]*?)(?=Legislation:)(?:[\<\w\s\S\d]*)"
    cwpattern=re.compile(catchpattern) # compile pattern
    cwresult=cwpattern.match(austcase) # use pattern to match on worddata (string)
    output=""
    if cwresult:
        grabstring=str(cwresult.group(1))
        print(grabstring)
        output="<b>"+caseref+r"</b><br><br><br>"+grabstring+r"<br><br>"
    return output

# write catchwords to individual files (effectively a database)
def writecatchwords(filename,cw):
    filename="./cw/"+filename+".html"
    fileopen=open(filename,"w")
    fileopen.write(cw)
    fileopen.close()
    return

# You may need a valid browser-style user-agent (not python) to access
# create a class where the user agent is set to the default
class MyOpener(FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'


def Main(year,endID):
    
    myopener=MyOpener()
    # TO do: loop through all matches

    #catchwords file
    cwfilestring="<html><head><title>Catchwords</title></head><body>"

    # write the full case locally
    for case in range(1,endID):
        austcase=getURLstring(case,year)
        citation=writecase(austcase)
        # save catchwords from this case to a local file
        if citation:
            result=str(citation.group(1))
            cwset=getCatchWords(result,austcase)
            cwfilestring=cwfilestring+cwset
            writecatchwords(result,cwset)
           
    # write all the catchwords found to a single file
    cwfile="catchwords_"+year+".html"
    cwfilestring=cwfilestring+"</body></html>"
    fileopen=open(cwfile,"w")
    fileopen.write(cwfilestring)
    fileopen.close()
    


# http://www6.austlii.edu.au/copyright.html
# AustLII places particular restrictions upon the ways in which case-law documents on AustLII can be copied and used. AustLII specifically blocks all spiders and other automated agents from accessing its case-law via the Robots Exclusion Standard. AustLIIâ€™s policy is the same as nearly all similar organisations internationally. The reasons for this policy include:
# 2. End Use
# (a) Individual end-users of the AustLII system are free to access, copy and print materials for their own use in accordance with copyright law;
# (b) In relation to case law, this is subject to (1)(e) above.

# nb classic site is accessible via:
# http://classic.austlii.edu.au/cgi-bin/sinodisp/au/cases/wa/WASC/2019/82.html
