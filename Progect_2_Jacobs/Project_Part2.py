#!/usr/bin/env python3
import pandas as pd
import csv
GH=pd.read_csv("XML_project.csv",",", names=["Name","Email","Category","Amount","Date"])

anser=open("anser.txt","w")

GH.dropna(inplace=True)
split=GH["Name"].str.split(' ', n = 1,expand=True)
GH["First Name"]=split[0]
GH["Last Name"]=split[1]
GH.drop(columns =["Name"], inplace = True)
GH["Date"]=pd.to_datetime(GH["Date"]).dt.strftime("%Y-%m-%d")

GH["Amount"]= GH["Amount"].str.replace("$",'')
GH["Amount"]=GH["Amount"].astype(float)
GH["Date"]= pd.to_datetime(GH["Date"])

M=(GH.groupby(["Amount"]).max(level=["Amount"]))

Q1=(M["Last Name"].tail(1))
Q2=(GH.groupby(GH["Category"]).sum())
Q3=(Q2.sort_values(by=["Amount"]))
Q3=(Q3.iloc[[-1]])

Q4=(GH.groupby(GH["Date"].dt.strftime("%Y-%m")).sum())
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


anser.close()
