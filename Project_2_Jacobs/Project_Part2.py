#!/usr/bin/env python3
import pandas as pd
import csv
#First I will import pendant is and CSV Python libraries
#Then I will create a variable of the read CSV file and assigned the variables as as needed using pendas
GH=pd.read_csv("XML_project.csv",",", names=["Name","Email","Category","Amount","Date"])

#These lines of code will split the name data column into first and last name. It will also delete the value name so that there is no confusion.
GH.dropna(inplace=True)
split=GH["Name"].str.split(' ', n = 1,expand=True)
GH["First Name"]=split[0]
GH["Last Name"]=split[1]
GH.drop(columns =["Name"], inplace = True)
GH["Date"]=pd.to_datetime(GH["Date"]).dt.strftime("%Y-%m-%d")
#The program will also reorganize the date function to make it more XML friendly, it will also remove the $ in order to do the same.
GH["Amount"]= GH["Amount"].str.replace("$",'')
GH["Amount"]=GH["Amount"].astype(float)
GH["Date"]= pd.to_datetime(GH["Date"])
#These two lines of code finds the person that spent the most money and places the value as Q1.
M=(GH.groupby(["Amount"]).max(level=["Amount"]))
Q1=(M["Last Name"].tail(1))
#This line of code tallies the total amounts for each category and puts it as Q2.
Q2=(GH.groupby(GH["Category"]).sum())
#Using the information gathered from Q2 the value of Q3 source the values by amount. After it takes the biggest amount and that becomes Q3
Q3=(Q2.sort_values(by=["Amount"]))
Q3=(Q3.iloc[[-1]])
#This line of code organize the value by date and shifts it to year and month and sums up the money that was spent in each of the time periods.

Q4=(GH.groupby(GH["Date"].dt.strftime("%Y-%m")).sum())
#These lines of code print out the answers to the question in a readable and understandable fashion.
print("\nThis is the person who spent the most money")
print(str(Q1))
print("\ntotal amounts for each budget category")
print(str(Q2))
print("\nThe budget category people spent the most money in")
print(str(Q3))
print("\nthe total amounts for each year-month")
print(str(Q4))

#LMAx=(MAx["Last Name"])
#FMAx=(MAx["First Name"])
#CMAx=(MAx["Amount"])
#print(FMAx,LMAx,CMAx)
