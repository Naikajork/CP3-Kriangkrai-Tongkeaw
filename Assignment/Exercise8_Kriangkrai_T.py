username = input("Username: ")
password = input("Password: ")
if username == "kriangkrai" and password == "1234":
    print("----------Welcome to ManU Shop----------")
    print("1.T-Shirt        Price  550 THB")
    print('2.Home Jersey    Price 2250 THB')
    print("3.Away Jersey    Price 2250 THB")
    print("4.Sock           Price  250 THB")
    selectItem = int(input("Please select your item: "))
    if selectItem == 1:
        price = 550
    elif selectItem == 2:
        price = 2250
    elif selectItem == 3:
        price = 2250
    elif selectItem == 4:
        price = 250
    itemQuatity = int(input('Please input your item quantity: '))
    totalPrice = price * itemQuatity
    print("Your order price is",totalPrice,"THB")
else:
    print("Username or Password incorrect!")