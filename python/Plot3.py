#First I will import two libraries to access the data and be able to plot the data
import numpy as np
import matplotlib.pyplot as plt
#These two arrays will store the data that is extracted from the text document.
name=[]
number=[]
#This line of code to open the document and be able to read the files with the function reliance.
with open("doc.text","r") as E:
    line = E.readlines()
#This for a loop will go over each line to extract the data to put into the arrays
    for l in line:
        su=(l.split(";")[0])
        nu=(l.split(";")[1])
        nus=nu.rstrip()
        nuss=(int(nus))
        name.append(su)
        number.append(nuss)

#The code below uses the imported library to create a graph to showcase the data
y_pos = np.arange(len(name))
plt.barh(y_pos, number, align='center', color='b', alpha=0.4)
plt.yticks(y_pos, name)
plt.xlabel('Number of occurrences')
plt.title("How many formats are available in these books")
plt.show()
#Lastly the program will close the extracted text file at the end
E.Close()
