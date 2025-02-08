---
title: vtt-Autotag-Tool python script for Descript exported subtitle .vtt files
#date: 2025-02-09T11:50:00+13:00
draft: false

---

Apps like Descript, when you export .vtt subtitle files, will not tag the speakers on every 42 character line.
For a Disability podcast that must have captions and transcriptions avaiolable for each Episode, this missing feature for Descript is a major manual time waster per Episode (Feb 2025, here's where the bug request was lodged, upvote, so we don;t have to do these crazy hacks)
<p>
This lack of true 42 character voice tagging, creates issues with podcast subtitle files, if you want to use it for transcripts in Pinecast (a podcast distributor).
The python script I created solves my own problem, of spending 1 to 2 hours per Episode having to auto-tag the vtt file every time the speaker switches.
This has made a 1-2 hour job in my current workflow into a 5 minute one, which is why I am sharing the process and the script.
<p>
NOTE: this python script is supplied, as is (it works for me, feel free to mod for your own use)
<p>
##Pre-requisites
* The Descript speakers need to be labelled **&lt;v SPEAKERNAME&&gt;**  (the python script looks for **&lt;v** to change speaker tags where they are missing, this made the python script simpler for me to construct)
	* Basically, when you import speaker audio into Descript and transcribe, name that speaker **&lt;v SPEAKERNAME&&gt;**
* Install python on your PC
* Create a folder to contain the vtt-auto.py script 
* Add your .vtt file (exported from Descript - with 42 character setting) into the same folder as vtt-auto.py script
	* rename your .vtt input file to **IN-Epx.vtt**
* run the pythion script from the same folder that the IN-Epx.vtt in
	* py .\vtt-AutoTag-Tool.py
* The output .vtt file called OUT-Epx.vtt is what you can upload to Pinecast transcript 
# vtt-AutoTag-Tool.py script
[The python script and a test .vtt file](https://github.com/bitrat/bitrat-blog-starter/tree/main/vtt-Autotag) (an actual Descript .vtt exported file that shows the issue the script will solve) can be downloaded from my repository on github

{{< highlight html >}}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>vtt-Autotag-Tool.py</title>
</head>
<body>
  <p>import re

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
</p>
</body>
</html>
{{< /highlight >}}

