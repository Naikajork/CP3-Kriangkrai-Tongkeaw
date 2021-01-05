listMenu =[]

def showBill():
    print("My Shop".center(20,"-"))
    print("Your Order:")
    totalPrice = 0
    for i in range(len(listMenu)):
        print(listMenu[i][0],listMenu[i][1],"THB")
        totalPrice += listMenu[i][1]
    print("")
    print("Total Price:", totalPrice)
while True:
    menuName = input("Please select menu: ")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Please select menu price: "))
    listMenu.append([menuName,menuPrice])

showBill()


