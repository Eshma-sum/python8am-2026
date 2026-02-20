import sqlite3

conn  = sqlite3.connect("college.sqlite3")

mycru = conn.cursor()

def create_table():
    sql= """
    CREATE TABLE IF NOT EXISTS teacher(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT NOT NULL,
    address TEXT NOT NULL
    )
    """
    mycru.execute(sql)
    conn.commit()

    print("table created successfully")


create_table()