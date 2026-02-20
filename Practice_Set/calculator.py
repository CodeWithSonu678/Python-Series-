result = 0
while True:
    print("      Calculater   In   Python  \n")
    
    print("1. Addition ")
    print("2. Subtration ")
    print("3. Multiply ")
    print("4. Divide")
    print("5. Exit")
    
    choice = int(input("Enter your chooice :- "))
    
    if choice ==5:
        print("Exiting...")
        break
    if choice >5:
        print("Invalid chooice !")
        continue
    try:
        num1 = int(input("Enter your first number :- "))
        num2 = int(input("Enter your second number :- "))
    
    except ValueError:
        print("Invalid number !")
        continue

    if choice ==1:
        result = num1+num2
        
    elif choice ==2:
        result = num1 - num2
        
    elif choice ==3:
        result = num1 * num2
        
    elif choice ==4:
        if num2 == 0:
            print("Zero se devide nhi hota h ")
            continue
        result = num1 / num2
    
    print(f"result :-  ",result)
