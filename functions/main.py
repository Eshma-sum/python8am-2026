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
# 1. local scope: inside the function, can only be accessed inside of the function.
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