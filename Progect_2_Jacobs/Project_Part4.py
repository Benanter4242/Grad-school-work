from lxml import etree

books = etree.parse("Total.xml")
root = books.getroot()
results1 = root.xpath("/budget/budget_item[amount<5]/email")
results2 = root.xpath('''/budget/budget_item[category="Computers"]/date''')
results3 = root.xpath('''/budget/budget_item[date[contains(.,'2017-03')]]/name/firstname''')
for r in results1:
    print(r.text)
for r in results2:
    print(r.text)
for r in results3:
    print(r.text)
