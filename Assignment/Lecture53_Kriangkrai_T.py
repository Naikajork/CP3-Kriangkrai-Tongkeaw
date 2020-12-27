def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result

inputPrice = int(input("Please enter total price: "))
print(vatCalculate(inputPrice))
