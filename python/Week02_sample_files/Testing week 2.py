import codecs
file1 = codecs.open("MOCK_DATA.txt","r","utf-8")
for z in file1:
    if z[-4]:
        print(z)
