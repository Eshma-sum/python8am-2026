# for i in range(1,4):
#     print(f"====={i}=====")
#     for a in range(1,3):
#         print(a)


# *
# **
# ***
# ****
# *****
# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# *****
# ****
# ***
# **
# *
# for i in range(6,0,-1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# 1
# 12
# 123
# 1234
# 12345
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# 1
# 22
# 333
# 4444
# 55555
# for i in range(1,6):
#     for j in range(i):
#         print(i,end=" ")
#     print()

# data = [
#     [12,34,56,78,97],
#     [23,45,67,89,90],
#     [34,56,78,90,12]
# ]
# sum_value = ?
# total_even_number = ?
# total_odd_number = ?

data = [
    [12,34,56,78,97],
    [23,45,67,89,90],
    [34,56,78,90,12]
]
sum = 0
total_even_number = 0
total_odd_number = 0
for i in data:
    for j in i:
        sum += j
        if j%2 == 0:
            total_even_number += 1
        else:
            total_odd_number += 1
print(f"the total sum: {sum} \t the total even number: {total_even_number} \t the total odd numbers: {total_odd_number}")