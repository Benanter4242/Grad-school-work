import re
# In the program is a quote made by Szymborska. The quote is assigned to a variable with the same name.
Szymborska=("When I pronounce the word Future, the first syllable already belongs to the past. When I pronouncethe word Silence, I destroy it. When I pronounce the word Nothing, I make something no nonbeing can hold")
#the next three lines edit the phrase so that way it can all be lowercase, spaces are removed, and only the letters are extracted.
Szymborska = Szymborska.lower() # used as reference: https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/
Szymborska = Szymborska.replace(" ", "")
Szymborska = re.sub("[^a-z]+", "", Szymborska) #   used as reference:  https://docs.python.org/3/library/re.html
#next is a dictionary to hold the counting of letters.
counts ={}
#A for loop which counts every letter and adds it to the dictionary.
for word in Szymborska:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
#Lastly a print function that shows what was counted.
print(counts)
