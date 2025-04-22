---
title: vtt-Autotag-Tool python script for Descript exported subtitle .vtt files
date: 2025-04-22T18:10:00+13:00
draft: false

---

Apps like Descript, when you export .vtt subtitle files, will not tag the speakers on every 42 character line output, they only voice tag on speaker changes. This does not currently allow podcasting distributors like Pinecast to recognize the speakers and format the transcript accordingly. These platforms expect speaker tagging on ALL separate 42 character subtitle lines.
For a Disability podcast like [Disability Disrupters](https://pinecast.com/feed/disability-disrupters) that must have captions and transcriptions available for each Episode, this missing feature for Descript is a major manual time waster for me, per Episode.
[Here's where I lodged the bug report with Descript in August 2024, before solving it with my janky python script](https://descript.canny.io/feature-requests/p/voice-tags-in-vtt) - upvote if you agree that Descript should solve this, so we don't have to do these crazy script hacks.
<p>This python script has made my 1-2 hour manual voice tag process a 5 minute process, which is why I am sharing this.
<p>
NOTE: this python script is supplied, as is (it works for me, feel free to modify it for your own use)

# Pre-Requisites
* The Descript speakers in the transcript before Export, need to already be labelled **&lt;v SPEAKERNAME&gt;**
	* the python script looks for **&lt;v SPEAKERNAME&gt;** to add speaker tags to the .vtt file where they are missing, this made the python script simpler for me to construct than pure speaker names
	* Basically, when you import speaker audio into Descript and transcribe, name that speaker from the get-go **&lt;v SPEAKERNAME&gt;**
* Install python on your PC (one-time setup)
* Create a **vtt-Autotag** folder to contain the **vtt-Autotag-Tool.py** script 
* Add your .vtt file (exported from Descript - with 42 character setting) into the same folder as the vtt-Autotag-Tool.py script
	* rename your .vtt input file to **IN-Epx.vtt** (this is what the python script expects - modify your script to suit your own workflow)
* run the python script from the same folder that the IN-Epx.vtt is in
	* py .\vtt-AutoTag-Tool.py
		* NOTE: If you get an error, you might have macrons/non utf-8 unicode in your text - change the encoding type in the script
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

fileIn = open(filename, "r", encoding="utf-8")
readLines = fileIn.readlines()
print("readlines :",readLines)

fileOut = open(filename2, 'w')

line_count = 0
digit_line = 0
for line in readLines:
    line_count += 1
    print(line)
    
	if line[0:2].isdigit():
        digit_line=line_count

    if (line_count == digit_line+1):
        try:
            x = re.search(r"^\<v[^\(]*[>]", line)
            currentTag = x.group(0)
            fileOut.write(line)
        except AttributeError:
            out = currentTag+line  
            fileOut.write(out)
    else:
        fileOut.write(line)
		
fileIn.close()     
fileOut.close() 
     
{{< /highlight >}}

