from lxml import etree

tree = etree.parse("books.xml")
x=(etree.tostring(tree))
print(x)
