#Write a function to print the lenth of the list
def print_len(list):
    print("Lenth of the list is : ",len(list))
    print(list)
cities=[]
print("Enter the name of the cities")
i=0
while True:
    x=input()   
    if (x=="stop"):
        break
    cities.append(x)

print_len(cities)