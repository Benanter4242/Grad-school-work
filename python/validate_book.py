from lxml import etree

#read in the schema, parse it, and save as a variable
xmlschema_doc = etree.parse("books.xsd")

#use the parsed data to create an XMLSchema object
xmlschema = etree.XMLSchema(xmlschema_doc)

#read in the XML file you want to validate
doc = etree.parse("books_with_xsd.xml")

#check to make sure the file adheres to the schema
print(xmlschema.validate(doc))

