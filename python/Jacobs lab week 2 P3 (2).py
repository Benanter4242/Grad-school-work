#!/usr/bin/env python3
import os
#This program will need an import from the OS library
#A variable will be written to read the numbers.txt file
File = open("numbers.txt","r")
 # This variable is to be used as a container for the numbers taken out of numbers.txt.
numbers = []
 #This for a loop will read the file and split each number apart.  Then the numbers will be added as an integer into the numbers list variable
for val in File.read().split():
    numbers.append(int(val))
# After the loop has ended the file will close.
File.close()

# Two variables are created to calculate the sum of all the numbers in the list and the length of how he numbers there are.

Sum=sum(numbers)
Len= len(numbers)

#Afterwards this new variable will write a new file placed in "Lab2-numbers" folder.
#What it will write is both the sum and length of the list of numbers along with the description. In order to use the write function we will change the variables that resulted from calculating the length and some of the list of numbers to a string.
X= open(os.path.join("Lab2-numbers","counts.txt"),"w")
X.write("This is the sum of the numbers:")
X.write(str(Sum)+"\n")
X.write("And this is the length:")
X.write(str(Len)+"\n")
#Afterwards the new written file will close.
X.close()
