def print_list(list,idex=0):
    if(idex==len(list)):
        return
    # print(list[idex],end=" ")
    print(list[idex])
    print_list(list,idex+1)
fruits=["mango","banana","lichi"]
print_list(fruits)    