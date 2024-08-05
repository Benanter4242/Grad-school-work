import pandas as pd

df = pd.read_csv("NCHS.csv")

#create groups of states
states = df.groupby('State')
#print(states.groups.keys())


#print(states.get_group('New York'))

for name,data in states:
    print(name)
    print (data.head())

"""
states.get_group('New York').to_csv('NewYork.csv')

"""