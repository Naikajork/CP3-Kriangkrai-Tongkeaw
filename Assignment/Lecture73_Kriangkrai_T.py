listMenu ={"ข้าวมันไก่": 40, "ข้าวขาหมู": 40, "ข้าวผัดกระเพราไก่": 35, "ข้าวหมููกระเทียม": 35, "ไข่ดาว": 10}
selectMenu = []

def showBill():
    print("My Shop".center(20,"-"))
    print("Your Order:")
    totalPrice = 0
    for i in range(len(selectMenu)):
        print(selectMenu[i],listMenu[selectMenu[i]],"THB")
        totalPrice += listMenu[selectMenu[i]]
    print("")
    print("Total Price:", totalPrice)
while True:
    menuName = input("Please select menu: ")
    if (menuName.lower() == "exit"):
        break
    else:
        selectMenu.append(menuName)

showBill()


