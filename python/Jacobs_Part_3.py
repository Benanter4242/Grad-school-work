import pandas as pd
#Like the previous programs this will require the same code that takes the CSV file into a database.
Data= pd.read_csv("Hospital_Data.csv")
NData=Data[["Facility Name","Address","City","State","ZIP Code","County Name","Phone Number","Hospital Type","Hospital Ownership","Emergency Services","Location"]]
#This line of code uses the value count to answer the question which state has the most hospitals.
Q1=NData["State"].value_counts()
print("The state with the most hospitals is:\n")
print(Q1.head(1))


#This line of code tries to figure out what is the most used form of hospital ownership in the US.
Q2=NData["Hospital Ownership"].value_counts()
print("The most used form of hospital ownership in the US is:\n")
print(Q2.head(1))
#With this line of code it extracts data from the data frame and takes the data that has the hospital ownership of tribal. It then uses the unique function to count the states that have tribal ownership.
Q3=NData.loc[NData["Hospital Ownership"]=="Tribal"]
Q3=Q3.State.unique()
print("States that have tribal ownership hospitals are:\n")
print(Q3)
#This line of code count how many hospitals of emergency services as opposed to those who do not.
Q4=NData["Emergency Services"].value_counts(normalize=True) * 100
print("Percentage of hospitals that do and do not have emergency services are:\n")
print(Q4)
#This answers the final question of what are the addresses that are in Washington DC.
Q5=NData.loc[NData["State"]=="DC"]
Q5=Q5["Address"]
print("Addresses for hospitals that are in Washington DC:\n")
print(Q5)
