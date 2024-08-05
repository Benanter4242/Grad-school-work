import os
import codecs

if not (os.patt.isdir("output")):
    os.mkdir("output")
file1 = codecs.open("Japanese_utf8.txt","r","utf-8")
print(file1.read)
