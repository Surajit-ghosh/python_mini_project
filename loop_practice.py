# Given a list of sales [1200, 3400, 560, 4500], find the total using a loop.
sales=[1200, 3400, 560, 4500]
total=0
for i in sales:
    total=total+i
print(total)    
# From the same list, find the maximum sale value manually (without using max()).
max_value=sales[0]
for i in sales:
    if i > max_value:
        max_value=i
print(max_value)        