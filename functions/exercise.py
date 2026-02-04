# def add(x,y):
#     print(x+y)

# a= int(input("enter a number: "))
# b= int(input("enter a number: "))
# add(a,b)



# def add():
#     a= int(input("enter a number: "))
#     b= int(input("enter a number: "))
#     print(a+b)
# add()



# def mul(n):
#     x=1
#     while x<=10:
#         print(f"{n} * {x} = {n*x}")
          # print(f"{n} * {x} = ",n*x)
#         x+=1
# num = int(input("enter a number: "))
# mul(num)



# def take_value():
#     p = int(input("enter principle: "))
#     t = int(input("enter time: "))
#     r = int(input("enter rate: "))
#     return [p,t,r]


# def cal_value():
    # res = take_value()
    # a = res[0]
    # b = res[1]
    # c = res[2]
#     a,b,c = take_value()
#     return (a*b*c)/100

# def display_value():
#     print("the simple interest: ", cal_value())

# display_value()



# def take_marks():
#     a = int(input("enter maths marks: "))
#     b = int(input("enter science marks: "))
#     c = int(input("enter java marks: "))
#     d = int(input("enter python marks: "))
#     e = int(input("enter c++ marks: "))
#     return [a,b,c,d,e]

# def total():
#     f,s,t,r,v = take_marks()
#     return f+s+t+r+v

# def percentage():
#     t = total()
#     p = t/5
#     return [t,p]

# def division():
#     grade = ""
#     result = percentage()
#     per = result[1]
#     tot = result[0]

#     if per >= 80:
#         grade = "Dis"
#     elif per >=60:
#         grade = "First"
#     elif per >=45:
#         grade = "Second"
#     elif per >=32:
#         grade= "Third"
#     else:
#         grade = "FAIL"

#     return [tot,per,grade]
    
# def result():
#     res = division()
#     print("total: ",res[0])
#     print("percentage: ",res[1])
#     print("grade: ",res[2])

# result()







# def login():
#     username = input("enter username: ")
#     password = input("enter password: ")

#     if username=='admin' and password == 'admin0123':
         # print("login success!")
#         return True
#     else:
#         return False
         # print("unsuccessful!")
# print (login())


# def message():
#     return "admin"
# name = input("enter username: ")

# if name == message():
#     print("success")
# else:
#     print("access denied")
#     question = input("do u want to try again, yes/no: ")
#     if question.lower() == "yes":
#         message()
#     else:
#         print("goodbye!!!!")





















def ascending_order(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers

# input
numbers = []
n = int(input("How many numbers? "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

print("Ascending order:", ascending_order(numbers))




