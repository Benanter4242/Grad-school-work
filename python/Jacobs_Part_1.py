#!/usr/bin/env python3
import pandas as pd
import sqlite3 as s3

#This this line of code makes dataframe out of the Hospital_Data.csv.
Data= pd.read_csv("Hospital_Data.csv")
# this line code will make the database interactive.
conn=s3.connect("Data.db")
c= conn.cursor()

#These are dictionaries to contain data for future coding.
States={}
Types={}
Own={}
#limiting the data columns is necessary along with changing column names to be more intractable of SQL.
NData=Data[["Facility Name","Address","City","State","ZIP Code","County Name","Phone Number","Hospital Type","Hospital Ownership","Emergency Services","Location"]]
NData["Index"]= NData.index

NData.rename( columns= {"County Name":"County_Name","ZIP Code":"ZIP_Code","Phone Number":"Phone_Number","Hospital Type":"Hospital_Type","Hospital Ownership":"Hospital_Ownership","Emergency Services":"Emergency_Services"},inplace = True)


#these for loops will create a dictionarys that counts the different datatypes and add ID numbers to them.
Count=0
for S in NData["State"]:
    if S not in States:
        Count +=1
        States[S]=Count
Count=0
for Type in NData["Hospital_Type"]:
    if Type not in Types:
        Count +=1
        Types[Type]= Count
Count=0
for Owner in NData["Hospital_Ownership"]:
    if Owner not in Own:
        Count +=1
        Own[Owner]= Count
#These lines of code use the map function to change the original string  data into a foreign key data.

NData["State"]= NData["State"].map(States)
NData["Hospital_Type"]=NData["Hospital_Type"].map(Types)
NData["Hospital_Ownership"]=NData["Hospital_Ownership"].map(Own)
#These lines of code change the dictionaries into data frames.
DFStates=pd.DataFrame(list(States.items()), columns=["States","ID"])
DFTypes=pd.DataFrame(list(Types.items()), columns=["Types","ID"])
DFOwn=pd.DataFrame(list(Own.items()),columns=["Own","ID"])

#These lines of code turn the data frames into an SQL table.
DFStates.to_sql('States', conn, if_exists='replace', index = False)
DFTypes.to_sql('Types', conn, if_exists='replace', index = False)
DFOwn.to_sql('Own', conn, if_exists='replace', index = False)
NData.to_sql('Hospital', conn, if_exists='replace', index = False)

#These lines of code test to see if the database is actually present and close the database entirely.

c.execute('''SELECT * FROM States''')
rows=c.fetchall()
for row in rows:
    print(row)


conn.commit()
conn.close()
