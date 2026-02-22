import sqlite3

conn = sqlite3.connect("database/student.sqlite3")

myCur = conn.cursor()

# def create_Table():
#     myCur.execute("""
#         CREATE TABLE IF NOT EXISTS course(
#                   id INTEGER PRIMARY KEY AUTOINCREMENT,
#                   name TEXT NOT NULL,
#                   teacher TEXT NOT NULL,
#                   phone INTEGER NOT NULL,
#                   email TEXT NOT NULL UNIQUE,
#                   address TEXT NOT NULL
#                   )
#                   """)
    
#     conn.commit()
#     print("table created")


# create_Table()

# def create_Table():
#     myCur.execute("""
#         CREATE TABLE IF NOT EXISTS user(
#                   id INTEGER PRIMARY KEY AUTOINCREMENT,
#                   name TEXT NOT NULL,
#                   email TEXT NOT NULL UNIQUE,
#                   address TEXT NOT NULL
#                   )
#                   """)
    
#     conn.commit()
#     print("table created")

# create_Table()


# def insert_Table(name,email,address):
#     myCur.execute(f"""
#         INSERT INTO user(name,email,address) VALUES ('{name}','{email}','{address}')
#                  """)
#     conn.commit()
#     print('data entered successfully')

# name = input("enter name: ")
# email = input("enter email: ")
# address = input("enter address: ")
# insert_Table(name,email,address)


# def show():
#     data = myCur.execute("SELECT * FROM user")
#     # data = myCur.execute("SELECT * FROM user WHERE name='sita'")
#     # data = myCur.execute("SELECT name,email FROM user WHERE name='admin' OR name='anil'")
#     # data = myCur.execute("SELECT COUNT(*) FROM user")
#     # data = myCur.execute("SELECT * FROM user WHERE name LIKE '%a%'")
#     # data = myCur.execute("SELECT * FROM user WHERE name LIKE '_a%'")
#     data = myCur.fetchall()
#     print(data)
# show()



# def delete(id):
#     myCur.execute(f"DELETE FROM user WHERE id={id}")
#     conn.commit()
#     print("DELETED SUCCESSFULLY")

# delete(3)



def update(id,name,email):
    myCur.execute("UPDATE user SET name '{name}' ")

update(2,"laxmi","laxmi@gmail.com")
