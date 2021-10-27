userNameInput = input("UsernameInput : ")
passWordName = input("Password : ")
if userNameInput == "admin" and passWordName == "1234":
    print("--- Welcome to AAA Store ---")
    print("--------- Product ----------")
    print("1. Pencil Price 15 THB")
    print("2. Peper Price 1 THB")
    print("3. Pen Price 20 THB")
    print("4. Ruler Price 10 THB")
    print("5. Eraser Price 5 THB")
    product1 = input("select number of product1 : ")
    QuantityProduct1 = int(input("Quantity of product1 : "))
    if product1 == "1":
        print("Total Price : ",15*QuantityProduct1)
    elif product1 == "2":
        print("Total Price : ",1*QuantityProduct1)
    elif product1 == "3":
        print("Total Price : ",20*QuantityProduct1)
    elif product1 == "4":
        print("Total Price : ",10*QuantityProduct1)
    elif product1 == "5":
        print("Total Price : ",5*QuantityProduct1)
