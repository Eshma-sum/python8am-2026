# function = reusable block of code

# def total(x):
#     sum = 0
#     for a in x:
#         sum +=a
#     print(f"sum:{sum}")

# total([1,2,3,4,5])


# optional parameter : always have regular parameter in the front and optional after that : def user(name="",age) is wrong

# def user(name,age=0):
#     print(name)
#     print(age)
# user("ram",25)

# *args
# **kargs



# function scope: 
# 1. local scope: inside the function, can only be accessed inside of the function block.
# 2. global scope: outside of function, can be accessed by any

# global:
# x=10
# def info():
#     print(x)
# info()
# local:
# def info():
#     x=10
#     print(x)
# print(x)   -> this wont work as the x variabl is local; inside the function
# info()

# x=10
# def info():
#     x=50
#     print(x)
# print(x)
# info()



# x=10
# def info():                #OUTPUT:
#     a=x+50                 #60
#     print(a)               #10
# info()
# print(x)


# x=10
# def info():                #OUTPUT: shows error that the code is not able to identify whether
#     x=x+50                 the x is local or global
#     print(x)               
# info()
# print(x)


# we can change the local variable into global by the following way:
# x=10
# def info():
#     global x
#     x=x+50
#     print(x)
# info()
# print(x)           # now this print will have 60 as the x variable inside the function block was considered global
