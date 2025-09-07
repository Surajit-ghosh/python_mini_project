print("Surajit Ghosh")
l=[11,45,1,2,3]
print(l)
l.append(7)                  #insert mnumber at last
print(l)
l.sort()                     # write the word at sequence
print(l)
l.sort(reverse=True)         # write the word at reverse sequence
print(l)
l.reverse()                  # write the word at reverse
print(l)
print(l.index(1))            # the number written in which index
print(l.count(1))            # the number present in the list how many time
m=l.copy()                   # copy the list frrom one to another
print(m)
l.insert(1,99)              
print(l)
n=[55,77]
l.extend(n)
print(l)
k=l+n
print(k)