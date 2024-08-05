#LIS487
#Amber Stubbs


import os #need to get the os (operating system) library

#os.listdir by default lists the files in the directory the file you are running is in
files = sorted(os.listdir("Week02_exercises"))

#print each of the file names
for f in files:
    print(f)

#note that by default, listdir() doesn't list the directories in order
# -- you need to sort the list for that:
# files = sorted(os.listdir())
