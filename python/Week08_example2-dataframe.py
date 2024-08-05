import pandas as pd

#create the 2-dimensional array
data = [['Pat',4.0],['Chris',3.32],['Lee',2.89]]

#turn the data into a DataFrame. Add column labels
df = pd.DataFrame(data,columns=['Student','GPA'])

#print
print (df)

#print a row
print("\nRow 1:")
print(df.loc[1])
#notice that this prints the second student -- it ignores the column names, and the first student is row 0

#print(df[])
print("\nPrint just the students:")
print(df['Student'])

print("\nprint the mean:")
print(df.mean())

print("\nprint the sum:")
print(df.sum())
