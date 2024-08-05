#!/usr/bin/env python3
import pandas as pd
import csv
from lxml import etree
#First I will import pendant is and CSV Python libraries along with the etree library
#Then I will create a variable of the read CSV file and assigned the variables as as needed using pendas
GH=pd.read_csv("XML_project.csv",",", names=["Name","Email","Category","Amount","Date"])
#The program will XML file called total to hold the new information
output=open("Total.xml","w")
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
#These lines of code will write in the XML file. The for loop will create the data necessary through the data frame created earlier.
output.write('''<?xml version="1.0" encoding="UTF-8" ?>\n<budget xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:noNamespaceSchemaLocation="budgets.xsd">\n''')
for index, r in GH.iterrows():
    Date=(str(r["Date"]))
    Category=(r["Category"])
    Amount=(str(r["Amount"]))
    First=(r["First Name"])
    Last=(r["Last Name"])
    Email=(r["Email"])
    output.write("\t<budget_item>\n")
    output.write("\t\t<name>\n")
    output.write('\t\t\t<firstname>'+First+'</firstname>\n')
    output.write('\t\t\t<lastname>'+Last+'</lastname>\n')
    output.write('\t\t</name>\n')
    output.write('\t\t<email>'+Email+'</email>\n')
    output.write('\t\t<amount>'+Amount+'</amount>\n')
    output.write('\t\t<category>'+Category+'</category>\n')
    output.write('\t\t<date>'+Date+'</date>\n')
    output.write("\t</budget_item>\n")
#The last bit of writing in the program will place the ending tag and then check the XML file against the schema. After that the XML file will close.
output.write('</budget>')
JK= etree.parse('budgets.xsd')
the_schema= etree.XMLSchema(JK)
total= etree.parse("Total.xml")
print(the_schema.validate(total))
output.close()
