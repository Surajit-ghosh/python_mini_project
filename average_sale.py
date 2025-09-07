# Write a function avg_sales(sales_list) that returns the average.
def avg_sale(sales_list):
    total_sale=0
    for i in sales_list:
        total_sale=total_sale+i
    equipment=len(sales_list)    
    average=total_sale/equipment
    print( "Average value of this sales list is ",average)
sales_list=[]    
while True:
    x=int(input("If you want to add sales value press 1 or press anything : "))
    if x==1:
        price=float(input("Enter the sale value : "))
        sales_list.append(price)
        avg_sale(sales_list)
    else:
        break    

