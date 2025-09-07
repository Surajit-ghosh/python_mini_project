class bikeshop:
    def __init__(self, quantity):
        self.quantity = quantity

    def display(self):
        print("Available bikes are", self.quantity)

    def rent(self, n):
        if n <= 0:
            print("Enter a positive value")
        elif n > self.quantity:
            print("Enter a value less than or equal to", self.quantity)
        else:
            print("Total price:", n * 100)
            self.quantity -= n   # update available bikes
            print("Available bikes now:", self.quantity)

    def return_bike(self, n):
        if n <= 0:
            print("Enter a positive value")
        else:
            self.quantity += n   # increase available bikes
            print(n, "bike(s) returned successfully")
            print("Available bikes now:", self.quantity)


# create object once
obj = bikeshop(100)

while True:
    a = int(input('''
1 for display bike
2 for rent bike
3 for return bike
4 for exit
          '''))

    if a == 1:
        obj.display()
    elif a == 2:
        n = int(input("Enter number of bikes to rent: "))
        obj.rent(n)
    elif a == 3:
        n = int(input("Enter number of bikes to return: "))
        obj.return_bike(n)
    elif a == 4:
        break
    else:
        print("Invalid choice")
