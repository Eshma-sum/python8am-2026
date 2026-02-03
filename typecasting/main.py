# what is typecasting?
# it is the process of converting a variable from one datatype to another.

# type() : used to get the datatype of the variable
# int() : used to convert a variable to integer
# str() : used to convert a variable to string
# float() : used to convert a variable to float

# a = 5
# print(type(a))

# x='5'
# y=7+int(x)
# print(y)


# a=int(input("enter a number: "))
# b=int(input("enter anothr number: "))
# print(a+b)


# p = int(input("enter principle: "))
# t = int(input("enter time: "))
# r = int(input("enter rate: "))
# si = (p*t*r)/100
# print(si)

# WAP to enter 5 subject marks and calculate total and percentage.
m1 = int(input("enter maths marks: "))
m2 = int(input("enter science marks: "))
m3 = int(input("enter english marks: "))
m4 = int(input("enter nepali marks: "))
m5 = int(input("enter computer marks: "))

total = m1+m2+m3+m4+m5
percentage = (total/500)*100
print(f"total: {total} and percentage: {percentage}")