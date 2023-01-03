while True:
    print("For Addition Press 1")
    print("For Subtraction Press 2")
    print("For Multuplication Press 3")
    print("For Divide Press 4")
    print("For Modulas Press 5")
    print("Press Q for Exit")
    choice=input("Enter The Choice\n")
    if choice=='q' or choice=='Q':
        break

    number_1=int(input("Enter The First Number\n"))
    number_2=int(input("Enter The Second Number\n"))
    
    if choice=='1':
        print("Yours Choic Is", choice)
        print("Result Is" ,number_1+number_2)
    elif choice=='2':
        print("Yours Choic Is", choice)
        print("Result Is" ,number_1-number_2)
    elif choice=='3':
        print("Yours Choic Is", choice)
        print("Result Is" ,number_1*number_2)
    elif choice=='4':
        print("Yours Choic Is", choice)
        print("Result Is" ,number_1/number_2)
    elif choice=='5':
        print("Yours Choic Is", choice)
        print("Result Is" ,number_1%number_2)
    else:
        print("Wrong Press")
