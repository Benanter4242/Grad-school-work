import re
pat = re.compile("cat")
string = "the cat at bat wears hats with a cat"
m = pat.findall(string)
print(m)
