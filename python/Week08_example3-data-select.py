import pandas as pd

df = pd.read_csv("NCHS.csv", encoding='utf-8')

#print(df.describe()) #this is not helpful -- the data in this is too nuanced

#just get the Massachusetts data
mass = df[df['State']=='Massachusetts']
#print(mass.head(10))

#now that we have just the Massachusetts data, we can ask more interesting questions
mass_cancer = mass[mass['Cause Name']=='Cancer']
#print(mass_cancer.head())


mass_cancer_sorted = mass_cancer.sort_values(by='Deaths', ascending=False)
#print(mass_cancer_sorted.head())

#if you want to look at all the causes of death and sort them, we can go back to the 'mass' data set

mass_sorted = mass.sort_values(by='Deaths', ascending=False)
#print(mass_sorted.head(10))

#everything but 'all causes'
mass_only_causes = mass[mass['Cause Name']!='All causes']
print(mass_only_causes.sort_values(by='Deaths', ascending=False))
