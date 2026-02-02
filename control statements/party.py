print("===============welcome to Club Party===============")

username = input("enter your name: ")
age = int(input("enter your age: "))

print("=============== welcome ",username," ===============")

underage_drinks = ['water','lassi','milk','soda','juice']
adult_drinks = ['Water', 'Lassi', 'Juice', 'Vodka', 'Beer','wine']
senior_drinks = ['Warm Water', 'Herbal Tea', 'Milk']


if age>=18 and age<60:
    print("=====adult menu=====")
    print("1. water 2. Lassi 3. Juice 4. Vodka 5. Beer 6. wine")
    option = int(input("CHOOSE THE OPTION FROM [1-6]: "))

    if option == 1:
        print("you have selected: ",adult_drinks[0])
    elif option == 2:
        print("you have selected: ",adult_drinks[1])
    elif option == 3:
        print("you have selected: ",adult_drinks[2])
    elif option == 4:
        print("you have selected: ",adult_drinks[3])
    elif option == 5:
        print("you have selected: ",adult_drinks[4])
    elif option == 6:
        print("you have selected: ",adult_drinks[5])
    else:
        print("invalid option")
        exit()

elif age>60:
    print("=====senior menu=====")
    print("1. Warm Water 2. Herbal Tea 3. Milk")   
    option = int(input("CHOOSE THE OPTION FROM [1-3]: "))

    if option == 1:
        print("you have selected: ",senior_drinks[0])
    elif option == 2:
        print("you have selected: ",senior_drinks[1])
    elif option == 3:
        print("you have selected: ",senior_drinks[2])
    else:
        print("invalid option")
        exit()

else :
    print("=====underage menu=====")
    print("1. water 2. lassi 3. milk 4. soda 5. juice")
    option = int(input("CHOOSE THE OPTION FROM [1-5]: "))

    if option == 1:
        print("you have selected: ",underage_drinks[0])
    elif option == 2:
        print("you have selected: ",underage_drinks[1])
    elif option == 3:
        print("you have selected: ",underage_drinks[2])
    elif option == 4:
        print("you have selected: ",underage_drinks[3])
    elif option == 5:
        print("you have selected: ",underage_drinks[4])
    else:
        print("invalid option")
        exit()