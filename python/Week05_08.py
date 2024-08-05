import re

p = re.compile("(\d\d)-(\d\d)-(\d\d\d\d)")
print(p.sub(r"\3-\2-\1","07-20-1969"))

