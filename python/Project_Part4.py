#!/usr/bin/env python3
from lxml import etree

#First the program will import etree from the LXML library.

#Then the program will phase the total XML file and create a variable for the XML root.


books = etree.parse("Total.xml")
root = books.getroot()
date=[]
#The program will then use X path to answer the quarries that were given.
results1 = root.xpath("/budget/budget_item[amount<5]/email")
results2 = root.xpath('''/budget/budget_item[category="Computers"]/date''')
results3 = root.xpath('''/budget/budget_item[date[contains(.,'2017-03')]]/name/firstname''')
#Using a for loop it will display the information that was found
print("Emails of the cheap people to spam for more money.\n")
for r in results1:
    print(r.text)
print("The date in which people bought from the computers category\n")
# In this for loop the program will append results into a list that can be made into a sorted order
for r in results2:
    date.append(r.text)
date=sorted(date)
for d in date:
    print(d)
print("The first names of people who bought items in the month of March in 2017\n")
for r in results3:
    print(r.text)
