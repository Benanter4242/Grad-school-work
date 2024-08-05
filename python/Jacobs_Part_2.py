import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
#These lines of code are similar to part two in it creates a data frame out of columns from the CSV file
Data= pd.read_csv("Hospital_Data.csv")
NData=Data[["Facility Name","Address","City","State","ZIP Code","County Name","Phone Number","Hospital Type","Hospital Ownership","Emergency Services","Location"]]

#These blank arrays will be used in creating the graph.
Does=[]
Doesnot=[]
labels=["MA","US"]
#These next few lines of code will create data to place into the blank arrays out of the emergency services data from the data frame as a whole and those containing Massachusetts is a state.
Q6=NData.loc[NData["State"]=="MA"]
Q6=(Q6["Emergency Services"].value_counts(normalize=True) * 100)
Q6= Q6.astype(int)
print(Q6)

Q4=NData["Emergency Services"].value_counts(normalize=True) * 100
Q4= Q4.astype(int)
print(Q4)
Does.append(Q6[1])
Does.append(Q4[1])
Doesnot.append(Q6[0])
Doesnot.append(Q4[0])

#This line of code will create the graph using the data found previously
x = np.arange(len(labels))
width = 0.35
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, Does, width, label='Has Emergency Care',color="r")
rects2 = ax.bar(x + width/2, Doesnot, width, label='Does not have Emergency Care')
ax.set_ylabel('Percentege')
ax.set_title('Massachusetts to the US in Emergency Care')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')
autolabel(rects1)
autolabel(rects2)

fig.tight_layout()
#Finally the program will close the CSV file.
plt.show()
Data.close()
