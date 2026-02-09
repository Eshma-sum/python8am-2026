# regex : regular expression
# tkinter module : it's a package.

import re

# name = 'ram rai'
# pattern = r'^[a-zA-Z \s]+$'
# if re.fullmatch(pattern,name):
#     print('valid')
# else:
#     print('invalid')



number = 9846024555
pattern = r'^[0-9 {10}]+$'
if re.fullmatch(pattern,str(number)):
    print('matched')
else:
    print('invalid')
