cities=["Kolkata","delhi"]
heroes=["krish","thor","Captain america"]    
def print_len(list):
    print(len(list))
# print_len(cities)
# print_len(heroes)
def print_list(list):
    for item in list:
        print(item,end=" ")
print_list(cities)
print("\n")    
print_list(heroes)