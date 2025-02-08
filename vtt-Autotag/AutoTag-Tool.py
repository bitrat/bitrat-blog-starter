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