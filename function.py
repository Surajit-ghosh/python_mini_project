s="surajit"
b="SUrAjIT"
str1="I am a good boy"
d=s.upper()
print(d)
d=s.capitalize()
print(d)
print(d.lower())                     # make lower case

a="!! Surajit !!"
print(a.replace("Surajit","Ghosh"))  # replace first word with last
print(a.rstrip("!"))                 # remove ! from last
print(a.split(" "))                  # make a box

b="SUrAjIT"
print(b.capitalize())                # make the first letter capital and the other in small letter

str1="I am a good boy"
print(len(str1))                     # count length
print(str1.center(50))               # make the line 50 word by using space
print(a.count("Surajit"))            # how mutch time the word is in the line
print(str1.endswith("!"))            # the sentence ends with ! or not
print(a.endswith("!"))
print(str1.endswith("go",4,7))       # the sentence ends with go  or not between 4 and 7
print(str1.find("good"))             # good in which index
print("good" in str1)                # good is present or not in this line
print(str1.index("good"))
print(str1.replace("good","bad"))    # repalce the world word with new one

e="Surajit05"
print(e.isalnum())                   # a sentence have A-Z a-z 0-9
print(e.isalpha())                   # a sentence have A-Z a-z 

f="Surajit"
# k=f.lower()
# print(k)
print(f.islower())                   # the whole word is lower or not

g="he is a good boy"
print(g.isprintable())               # whole sentence is printable or not
print(g.title())                     # make first word capital
print(g.capitalize())

h="    "
print(h.isspace())                   # the sentence has space or not

i="He Is Good"
print(i.istitle())                   # the first letter of the word starts with capital latter
print(i.startswith("He"))            # sentence stars with he or not
print(i.swapcase())                  # make the upper case to lower case and lower case to upper case
print("Is" in i)