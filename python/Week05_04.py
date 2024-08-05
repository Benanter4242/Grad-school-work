import re

p = re.compile('(\d\d)-(\d\d)-(?P<year>\d\d\d\d)')
m = p.search( "20-07-1969" )
print(m.group('year'))