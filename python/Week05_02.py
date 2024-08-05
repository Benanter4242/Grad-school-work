import re

pat = re.compile("cat")
string = "the cat at bat wears hats"
m = pat.search(string)
print(m)
