#lis487
#Amber Stubbs

#Experimenting with reading files and lines

#Experiment with what happens if you use the 'filetext' variable
#in a for loop. (e.g. "for f in filetext").
#Does it make a difference if you used read() or readlines()?

#open the file and just read it
#jabberwocky.txt must be in the same directory as this file!
readFile = open('jabberwocky.txt','r')
fileText = readFile.read()
readFile.close()
#print(fileText)

"""
for f in fileText:
    print(f) #prints each letter

print("\n\n*****************************\n\n")
"""
#version2 - with readlines
readFile = open('jabberwocky.txt','r')
fileText = readFile.readlines()
readFile.close()
print(fileText)

for f in fileText:
    print(f) #prints each line
