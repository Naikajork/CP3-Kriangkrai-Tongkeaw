inputLevel = int(input("Please enter piramid level: "))
for x in range(inputLevel):
    y = 1+x
    starSymbol = ""
    for y in range(y+x):
        tabSymbol = ""
        starSymbol = "*" + starSymbol
        for z in range(inputLevel-(x+1)):
            tabSymbol = " " + tabSymbol
    print(tabSymbol+starSymbol)