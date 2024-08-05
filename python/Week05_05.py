import re

p = re.compile('(.)\\1')
# p = re.compile(r'(.)\1')
m = p.finditer('aabbccddee')
for l in m:
    print(l)