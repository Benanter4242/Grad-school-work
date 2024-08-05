#LIS487
#Amber Stubbs


import os #need to get the os (operating system) library

files = os.listdir("LIS487"+os.sep+"folder_b") #use os.sep so the code will run on any os

for f in files:
    print(f)
