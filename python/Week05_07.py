import re

p = re.compile("LIS\d\d\d")
print(p.sub("LIS487","I really enjoyed "+ "LIS407 and LIS415"))
print(p.subn("LIS487","I really enjoyed "+  "LIS407 and LIS415"))
