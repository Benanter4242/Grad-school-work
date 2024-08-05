#First I'm going to import the xml.etree.ElementTree library to utilize its functions.
import xml.etree.ElementTree as ET
#Then I shall use the parse function to extract data from the XML file.
tree = ET.parse("simmons_programming_books.xml")
root= tree.getroot()
#Afterwords the program will open multiple text documents to write the data on outside document to be extracted later.
#These dictionaries will contain the data that is collected from the for loops when interacting with the  documents.
w_sub=open("sub.text","w")
w_year=open("year.text","w")
w_doc=open("doc.text","w")
D={}
E={}
F={}
#These four loops extracts the data necessary into the dictionaries.
for child in root.iter("subj"):
    Sub=(child.text)
    if Sub in D:
        D[Sub]=D[Sub] + 1
    else:
        D[Sub] = 1
for child in root.iter("dt"):
    year=child.get("year")
    if year in E:
        E[year]= E[year]+1
    else:
        E[year] = 1
for child in root.iter("doctype"):
    leg=(child.text)
    if leg in F:
        F[leg]=F[leg] + 1
    else:
        F[leg] = 1
DD=D.items()
EE=E.items()
FF=F.items()
#These four loops write  data collected from the dictionaries and a easily extractable format
for d in DD:
    w_sub.write(d[0]+";"+str(d[1])+"\n")
for e in EE:
    w_year.write(e[0]+";"+str(e[1])+"\n")
for f in FF:
    w_doc.write(f[0]+";"+str(f[1])+"\n")
#Finally the program will close the text documents 
w_sub.close()
w_year.close()
w_doc.close()
