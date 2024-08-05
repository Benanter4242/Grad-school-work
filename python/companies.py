from lxml import etree
import csv


#read in csv file
csvfile = open('companies.csv')
fileLines = csv.reader(csvfile, delimiter=',')

#open the xml file
xmlout = open('companies.xml','w')

#the following allows us to write a bunch of text to the file without a lot of concatenation
xmlout.write('''<?xml version="1.0" encoding="UTF-8"?>
<companies xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:noNamespaceSchemaLocation="companies.xsd">
''')

#the following is an early test line to make sure the xml file is being created
#xmlout.close()

for f in fileLines:
    print(f)
    print(f[0])
    print(f[1])
    s = '''
    <company>%s</company>
    <year>%s</year>''' % (f[0],f[1])
    xmlout.write(s)

xmlout.write("\n</companies>")

csvfile.close()
xmlout.close()

#time to check how we did

#read in the schema, parse it, and save as a variable
xmlschema_doc = etree.parse("companies.xsd")

#use the parsed data to create an XMLSchema object
xmlschema = etree.XMLSchema(xmlschema_doc)

#read in the XML file you want to validate
doc = etree.parse("companies.xml")

#check to make sure the file adheres to the schema
print(xmlschema.validate(doc))

