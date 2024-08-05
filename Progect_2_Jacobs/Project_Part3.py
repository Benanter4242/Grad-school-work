#!/usr/bin/env python3
import pandas as pd
import csv
from lxml import etree
GH=pd.read_csv("XML_project.csv",",", names=["Name","Email","Category","Amount","Date"])
output=open("Total.xml","w")

GH.dropna(inplace=True)
split=GH["Name"].str.split(' ', n = 1,expand=True)
GH["First Name"]=split[0]
GH["Last Name"]=split[1]
GH.drop(columns =["Name"], inplace = True)




GH["Date"]=pd.to_datetime(GH["Date"]).dt.strftime("%Y-%m-%d")




GH["Amount"]= GH["Amount"].str.replace("$",'')
GH["Amount"]=GH["Amount"].astype(float)

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
output.write('</budget>')
JK= etree.parse('budgets.xsd')
the_schema= etree.XMLSchema(JK)
total= etree.parse("Total.xml")
print(the_schema.validate(total))
output.close()
