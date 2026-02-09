import tkinter as tk

app = tk.Tk()
app.title("Calculator")
app.geometry("355x300")

screen = tk.Entry(app,width=25,borderwidth=5,font=('Arial',18))
screen.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def get_Value(value):
    screen.insert(tk.END,value)

def get_result():
    oldvalue = screen.get()
    result = eval(oldvalue)
    screen.delete(0,tk.END)
    screen.insert(tk.END,result)

def clear_screen():
    screen.delete(0,tk.END)

one = tk.Button(app,text="1", padx=30, pady=15, command=lambda: get_Value(1))
two = tk.Button(app,text="2", padx=30, pady=15, command=lambda: get_Value(2))
three = tk.Button(app,text="3", padx=30, pady=15, command=lambda: get_Value(3))
four = tk.Button(app,text="4", padx=30, pady=15, command=lambda: get_Value(4))
five = tk.Button(app,text="5", padx=30, pady=15, command=lambda: get_Value(5))
six = tk.Button(app,text="6", padx=30, pady=15, command=lambda: get_Value(6))
seven = tk.Button(app,text="7", padx=30, pady=15, command=lambda: get_Value(7))
eight = tk.Button(app,text="8", padx=30, pady=15, command=lambda: get_Value(8))
nine = tk.Button(app,text="9", padx=30, pady=15, command=lambda: get_Value(9))
zero = tk.Button(app,text="0", padx=30, pady=15, command=lambda: get_Value(0))
add = tk.Button(app,text="+", padx=30, pady=15, command=lambda: get_Value('+'))
sub = tk.Button(app,text="-", padx=30, pady=15, command=lambda: get_Value('-'))
divide = tk.Button(app,text="/", padx=30, pady=15, command=lambda: get_Value('/'))
multiply = tk.Button(app,text="*", padx=30, pady=15, command=lambda: get_Value('*'))
equal = tk.Button(app,text="=", padx=30, pady=15, command=get_result)
clear = tk.Button(app,text="C", padx=30, pady=15, command=clear_screen)

seven.grid(row=1,column=0)
eight.grid(row=1,column=1)
nine.grid(row=1,column=2)
divide.grid(row=1,column=3)
four.grid(row=2,column=0)
five.grid(row=2,column=1)
six.grid(row=2,column=2)
multiply.grid(row=2,column=3)
one.grid(row=3,column=0)
two.grid(row=3,column=1)
three.grid(row=3,column=2)
sub.grid(row=3,column=3)
zero.grid(row=4,column=0)
equal.grid(row=4,column=1)
add.grid(row=4,column=2)
clear.grid(row=4,column=3)


app.mainloop()