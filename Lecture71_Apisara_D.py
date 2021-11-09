menuList = []
priceList = []

def showBill():
    total = 0
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])
        total += priceList[number]
    print("Total : ",total)

while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price :"))
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()