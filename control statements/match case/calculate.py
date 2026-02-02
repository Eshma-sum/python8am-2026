x = int(input("enter 1st number: "))
y = int(input("enter 2nd number: "))
print("choose the desired option: [1-4]")

z = input("1. + 2. - 3. * 4./ ")

match z:

    case 1:
        z= x+y
        print("x + y = ",z)
    case 2:
        z= x-y
        print("x - y = ",z)
    case 3:
        z= x*y
        print("x * y = ",z)
    case 4:
        z= x/y
        print("x / y = ",z)
    case _:
        print("please choose from the given options only")
        