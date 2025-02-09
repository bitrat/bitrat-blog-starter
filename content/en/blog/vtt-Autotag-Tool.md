---
title: vtt-Autotag-Tool python script for Descript exported subtitle .vtt files
date: 2025-02-09T11:50:00+13:00
draft: false

---

Apps like Descript, when you export .vtt subtitle files, will not tag the speakers on every 42 character line, they only voice tag on speaker changes. This does not currently allow podcasting distributors like Pinecast to recognize the speakers and format the transcript accordingly. These platforms expect speaker tagging on ALL separate 42 character subtitle lines.
For a Disability podcast (like **Disability Disrupters**) that must have captions and transcriptions available for each Episode, this missing feature for Descript is a major manual time waster per Episode.
This is a demo site for the [Feb 2025 - Here's where I lodged the bug report with Descript in August 2024, before solving it with my janky python script](https://descript.canny.io/feature-requests/p/voice-tags-in-vtt) - upvote if you agree that Descript should solve this, so we don't have to do these crazy script hacks.
<p>This python script has made my 1-2 hour manual voice tag process into a 5 minute one, which is why I am sharing my process and the script.
<p>
NOTE: this python script is supplied, as is (it works for me, feel free to modify it for your own use)

##Pre-requisites
* The Descript speakers in the transcript before Export, need to already be labelled **&lt;v SPEAKERNAME&&gt;**  (the python script looks for **&lt;v** to change speaker tags where they are missing, this made the python script simpler for me to construct)
	* Basically, when you import speaker audio into Descript and transcribe, name that speaker from the get-go **&lt;v SPEAKERNAME&&gt;**
* Install python on your PC (one-time setup)
* Create a folder to contain the vtt-Autotag-Tool.py script 
* Add your .vtt file (exported from Descript - with 42 character setting) into the same folder as vtt-Autotag-Tool.py script
	* rename your .vtt input file to **IN-Epx.vtt** (this is what th python script expects - modify your script to suit your workflow)
* run the pythion script from the same folder that the IN-Epx.vtt is in
	* py .\vtt-AutoTag-Tool.py
* The output .vtt file will be called **OUT-Epx.vtt**. This is what you can upload as a Pinecast transcript 
# vtt-AutoTag-Tool.py script
[The python script and a test .vtt file](https://github.com/bitrat/bitrat-blog-starter/tree/main/vtt-Autotag) (an actual Descript .vtt exported file that shows the issue the script will solve) can be downloaded from my repository on github

{{< highlight html >}}
import re

from shutil import move

x = ""
currentTag = "<v TestPerson>"
filename = './IN-Epx.vtt'
filename2 = './OUT-Epx.vtt'

#with open(filename, "r") as finput, open(filename2, "w") as foutput:
fileIn = open(filename, "r")
readLines = fileIn.readlines()
print("readlines :",readLines)

fileOut = open(filename2, 'w')

line_count = 0
digit_line = 0
for line in readLines:
    line_count += 1
    #print(line_count,line)
    print(line)
    if line[0:2].isdigit():
        digit_line=line_count
        #print(digit_line)
    if (line_count == digit_line+1):
        #print(line)
        #print("1 line after digits")
        try:
            #x = re.search(r"^\<v[^\(]*[:]", line)
            x = re.search(r"^\<v[^\(]*[>]", line)
            #print('x: ',x.group(0))
            currentTag = x.group(0)
            fileOut.write(line)
        except AttributeError:
            out = currentTag+line  
            fileOut.write(out)
            #print('foutx: ',out)
    else:
        fileOut.write(line)
fileIn.close()     
fileOut.close() 

# writing to file an array of values L = ["Geeks\n", "for\n", "Geeks\n"]
#fileOut.writelines(L)       
{{< /highlight >}}

