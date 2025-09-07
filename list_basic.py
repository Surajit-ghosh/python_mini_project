marks=[3,4,5,6,"Surajit",7,8,9,33,44]
print(marks)
print(marks[0])
if 6 in marks:
    print("yes")
else:
    print("no")    
if "ra" in "surajit":
    print("Yes")
if "raa" in "surajit":
    print("yes")     
print(marks[1:8])
print(marks[1:10:2])
list=[i*i for i in range(10) if i%2==0]
print(list)
