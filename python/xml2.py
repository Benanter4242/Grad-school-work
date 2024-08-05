from lxml import etree

parser = etree.XMLParser(dtd_validation=True)
tree2 = etree.parse("books_with_dtd_broken.xml",parser)
root2 = tree2.getroot()
print(root2.tag)
for e in root2.iter("*"):
    print(e.tag)
