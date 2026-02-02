data = [
    {'username':'admin','password':'admin002'},
    {'username':'sita','password':'sita2002'},
    {'username':'ram','password':'ram2002'}
]
username = input('enter username: ')
password = input('enter password: ')

if username==data[0]['username'] and password==data[0]['password']:
    print("welcome",username)

elif username==data[1]['username'] and password==data[1]['password']:
    print("welcome",username)

elif username==data[2]['username'] and password==data[2]['password']:
    print("welcome",username)

else:
    print(" didnot match") 