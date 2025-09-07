student={
    "name" : "Surajit",
    "Subjects" : {
        "phy" : "96",
        "chem" : "98",
    }
}
if "name" in student:
    print("yes")
else:
    print("no")    

print(student.keys())
print(student.values())
print(student.items())
o=list(student.items())
print(o[1])
print(student["name"])
student.update({"city" :"kolkata"})
print(student)