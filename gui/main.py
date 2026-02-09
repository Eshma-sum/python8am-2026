# import tkinter as tk

# app = tk.Tk()
# app.title("My Form")
# app.geometry("500x500")

# # message = tk.Label(app, text="welcome to my app")
# # message.pack()
# # name = tk.Label(app,text="my name is kusum")
# # name.pack()
# # name = tk.Label(app, text="Enter your name: ")
# # name.grid(row=0,column=0)

# # result = tk.StringVar()

# # name = tk.Entry(app,textvariable=result)
# # name.grid(row=0,column=1)

# # email = tk.Label(app,text="punkusum76@gmail.com")
# # email.pack()

# # email = tk.Label(app,text="Enter your email: ")
# # email.grid(row=2,column=0)

# # email = tk.Entry(app,textvariable=result)
# # email.grid(row=2,column=1)

# # def get_Value():
# #     print(result.get())

# # button = tk.Button(app,text="Submit", command=get_Value)
# # button.grid(row=3,column=0,columnspan=2)


# nameVariable = 

# app.mainloop()














import tkinter as tk

app = tk.Tk()
app.title("My Form")
app.geometry("500x500")

# ---------- Variables ----------
name_var = tk.StringVar()
email_var = tk.StringVar()
password_var = tk.StringVar()

# ---------- Labels ----------
tk.Label(app, text="Enter your name:").grid(row=0, column=0, padx=10, pady=5)
tk.Label(app, text="Enter your email:").grid(row=1, column=0, padx=10, pady=5)
tk.Label(app, text="Enter your password:").grid(row=2, column=0, padx=10, pady=5)

# ---------- Entries ----------
tk.Entry(app, textvariable=name_var).grid(row=0, column=1)
tk.Entry(app, textvariable=email_var).grid(row=1, column=1)
tk.Entry(app, textvariable=password_var, show="*").grid(row=2, column=1)

# ---------- Result Label ----------
result_label = tk.Label(app, text="", fg="green")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# ---------- Button Function ----------
def get_value():
    name = name_var.get()
    email = email_var.get()
    password = password_var.get()

    result_label.config(
        text=f"Name: {name}\nEmail: {email}\nPassword: {password}"
    )

# ---------- Button ----------
tk.Button(app, text="Submit", command=get_value).grid(
    row=3, column=0, columnspan=2, pady=10
)

app.mainloop()
