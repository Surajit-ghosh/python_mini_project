def account(price,discount):
    new_price=price-((discount/100)*price)
    print("New price is ",new_price)
while True:
  price=float(input("Enter the price : "))
  discount=float(input("Enter the discount : "))
  account(price,discount)       
