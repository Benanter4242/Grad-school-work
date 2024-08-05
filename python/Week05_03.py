import re

pat = re.compile("(\d\d)-(\d\d)-(\d\d\d\d)")
m = pat.match("20-07-1969")


print(m.group())
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
