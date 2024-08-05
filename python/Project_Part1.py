import pandas as pd
import csv
#First I will import pendant is and CSV Python libraries
#Then I will create a variable of the read CSV file and assigned the variables as as needed using pendas
GH=pd.read_csv("XML_project.csv",",", names=["Name","Email","Category","Amount","Date"])
#The program will then create a new HTML file.
table=open("table.html","w")
#These lines of code will split the name data column into first and last name. It will also delete the value name so that there is no confusion.
GH.dropna(inplace=True)
split=GH["Name"].str.split(' ', n = 1,expand=True)
GH["First Name"]=split[0]
GH["Last Name"]=split[1]
GH.drop(columns =["Name"], inplace = True)

#The program will also reorganize the date function to make it more XML friendly, it will also remove the $ in order to do the same.
GH["Date"]=pd.to_datetime(GH["Date"]).dt.strftime("%Y-%m-%d")

GH["Amount"]= GH["Amount"].str.replace("$",'')
GH["Amount"]=GH["Amount"].astype(float)

#These lines of code will write in the HTML file and create a table
table.write("<!DOCTYPE html>"+"\n"+"<html>"+"\n"+"<body>"+"\n")
table.write("<table>\n<tr>\n<th>date</th>\n<th>category</th>\n<th>amount</th>\n")
#The for loop in the middle will write in the date, category, and amount spent.
for index, row in GH.iterrows():
    Date2=(str(row["Date"]))
    Category2=(row["Category"])
    Amount2=(str(row["Amount"]))
    table.write("<tr><td>"+Date2+"</td><td>"+Category2+"</td><td>"+Amount2+"</td></tr>")
#The final lines of code will complete the HTML table and close the file.
table.write("</table>\n")
table.write("</body>"+"\n"+"</html>")

table.close()
