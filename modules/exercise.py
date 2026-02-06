# 
# import datetime
# import time
# print(datetime.datetime.now())
# print(dir(datetime))
# print(datetime.MAXYEAR)

# b_date = datetime.date(1993,5,10)
# today = datetime.date.today()
# dif = today - b_date
# print(dif)

# today = datetime.date.today()
# print(today.strftime("%d/%m/%y"))


# jobs = [
#     {'title':'python developer','exp_date':'2024-12-31'},
#     {'title':'data scientist','exp_date':'2026-11-3'},
#     {'title':'web developer','exp_date':'2024-1-15'}
# ]

# for job in jobs:
#     exp_date = datetime.datetime.strptime(job['exp_date'], "%Y-%m-%d")
#     today = datetime.datetime.now()
#     if exp_date > today:
#         print(f"job '{job['title']}' is still valid. ")
#     else:
#         print(f"Job '{job['title']}' has expired.")



# import os

# os.makedirs('students')
# os.rmdir('students')





# import datetime

# jobtitle = input("enter the job you want: ")
# jobs = [
#     {'title':'python developer','exp_date':'2024-12-31'},
#     {'title':'data scientist','exp_date':'2026-11-3'},
#     {'title':'web developer','exp_date':'2024-1-15'}
# ]
# found = False
# for job in jobs:
#     exp_date = datetime.datetime.strptime(job['exp_date'], "%Y-%m-%d")
#     today = datetime.datetime.now()
#     if jobtitle == job['title']:
#         found = True
#         if exp_date > today:
#             print(f"the job '{job['title']}' is still available.")
#         else:
#             print(f"job '{job['title']}' has expired")
# if not found:
#             print("job not available.")




# import datetime
# def display(jobs):
#     jobtitle = input("enter the job: ")
#     found = False
#     # try:
#     for job in jobs:
#         if jobtitle == job['title']:
#             found = True
#             exp_date = datetime.datetime.strptime(job['exp_date'], "%Y-%m-%d")
#             today = datetime.datetime.today()
#             if exp_date > today:
#                 print(f"job '{job['title']}' is available.")
#             else:
#                 print(f"job '{job['title']}'has expired.")
#     if not found:
#         print("job is not available")

# display(jobs = [
#     {'title':'python developer','exp_date':'2024-12-31'},
#     {'title':'data scientist','exp_date':'2026-11-3'},
#     {'title':'web developer','exp_date':'2024-1-15'}
# ])
