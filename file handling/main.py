# obj = open("file handling/students.txt", "w")
# obj.write("hello Nepal")
# obj.close()

# obj = open("file handling/students.txt", "a")
# obj.write("Hello Nepal \n")
# obj.close()


# obj = open("file handling/students.txt", "a")
# name = input("enter your name: ")
# email = input("enter your email: ")
# address = input("enter your address: ")
# obj.write(f"{name}, {email}, {address}\n")


obj = open("file handling/students.txt","a")
name = input("enter your name: ")
maths = int(input("enter maths marks: "))
science = int(input("enter science marks: "))
english = int(input("enter english marks: "))
java = int(input("enter java marks: "))
python = int(input("enter python marks: "))

total = maths+science+english+java+python
percentage = total/5

obj.write(f"{name} ,{maths} ,{science} ,{english} ,{java} ,{python} ,{total} ,{percentage}\n")
