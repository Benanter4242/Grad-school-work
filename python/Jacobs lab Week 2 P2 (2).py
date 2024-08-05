#!/usr/bin/env python3
import os
import random
#This program will need to import to libraries os and random
#this program will contain a if not statement that searches for the dictionary lab to numbers
if not (os.path.isdir("Lab2-numbers")):
    os.mkdir("Lab2-numbers")
# A file will then be written into the folder lab to numbers with numbers.txt
file= open(os.path.join("Lab2-numbers","numbers.txt"),"w")
#a for loop will then create random numbers from 1 to 100 200 times. Refence: https://www.pythoncentral.io/pythons-range-function-explained/
for x in range(200):
#the loop will write the random number selected and add a new line each time the loop is engaged

        part= str(random.randint(1,100))
        file.write(part+"\n")
#after the loop is done the file will close.
file.close()
