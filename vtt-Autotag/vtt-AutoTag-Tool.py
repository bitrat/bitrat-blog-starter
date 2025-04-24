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
            #x = re.search(r"^\<v[^\(]*[:]", line)
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