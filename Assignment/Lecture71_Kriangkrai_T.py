listMenu =[]
listPrice =[]
def showBill():
    print("My Shop".center(20,"-"))
    print("Your Order:")
    totalPrice = 0
    for i in range(len(listMenu)):
        print(listMenu[i],listPrice[i],"THB")
        totalPrice += listPrice[i]
    print("")
    print("Total Price:", totalPrice)
while True:
    menuName = input("Please select menu: ")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Please select menu price: "))
    listMenu.append(menuName)
    listPrice.append(menuPrice)
showBill()


