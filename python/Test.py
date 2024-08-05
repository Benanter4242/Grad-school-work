import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd

years=[]
degrees_women=[]
degrees_man=[]

# Example data, stored in lists
GH=pd.read_csv("CS_degrees.csv",header=None)
print(GH)
for g in GH:
    years.append(g[0])
    degrees_women.append(int(g[1]))
    degrees_man.append(int(g[2]))

#set up the figure
fig = plt.figure()
#create axes - one row, one column, one plot
ax = fig.add_subplot(121)

#set up marks for the y axis
y_pos = np.arange(len(years))

#create the graph
ax.bar(y_pos, degrees_women,degrees_man, align='center', color='b', alpha=0.5)
#set labels and spacing for y axis
plt.xticks(y_pos, years)
#label x axis
plt.ylabel('Number of Paper things for jobs')
plt.xlabel("This is a bar!")
#label figure
plt.title("Computer Science Bachelor's degrees earned by women, 2000-2011")

#show the figure
plt.show()
