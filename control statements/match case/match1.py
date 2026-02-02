x = int(input("enter a number: "))
match x:
    case 0:
        print("zero")
    case 5:
        print("five")
    case _ if x<=10:
        print(x)
    case _ if x == 90:
        print(x)
    case _:
        print("guess")
