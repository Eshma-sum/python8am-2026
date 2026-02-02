print("===============welcome to book store===============")
username = input("enter username: ")
password = input("enter password: ")

if username=="admin" and password == "admin0123":
    books = ['python','java','c++','javascript']
    print("1. View Books 2. Insert Books 3. Delete Book")
    option=int(input("Choose an option (1-3): "))
    if option ==1:
        print(books)
    elif option == 2:
        name = input("enter book name: ")
        books.append(name)
        print(books)
    else:
        print("Invalid credentials. Access denied.")
        exit()