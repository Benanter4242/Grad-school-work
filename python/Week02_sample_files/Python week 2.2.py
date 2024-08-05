import os
newfile= open('jabberwocky.txt','r')
newfile=newfile.readlines()

for l in newfile:
    l=l.split()
    count=len(l)
    print(l,count)

# next time do not use the same variable in the for loop
