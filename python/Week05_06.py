import re

p = re.compile("((\w)\\2)", re.IGNORECASE)
s = "Look, Aaron's book Balloons and Bookkeeping fell on the floor"
print(p.split(s))


