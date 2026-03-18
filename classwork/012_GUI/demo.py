from tkinter import *
import mysql.connector as sql
con=sql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="company"
)
Cursor = con.cursor()

root = Tk()

root.geometry("400x400")
root.title("my app")

# b1 = Button(root, text="right").pack(side=RIGHT)
# b2 = Button(root, text="left").pack(side=LEFT)
# b3 = Button(root, text="top").pack(side=TOP)    
# b4 = Button(root, text="bottom").pack(side=BOTTOM)

# l1= Label(root, text="username").grid(row=0, column=0)
# l2= Label(root, text="password").grid(row=1, column=0)
# l3= Label(root, text="phone").grid(row=2, column=0)

# t1 = Entry(root).grid(row=0, column=1)
# t2 = Entry(root).grid(row=1, column=1)
# t3 = Entry(root).grid(row=2, column=1)

# b1 = Button(root, text="submit").grid(row=3, column=0)

def add():
    uname = t1.get()
    email = t2.get()
    phone = t3.get()
    Cursor.execute(f"insert into reg(uname, email, phone) values ('{uname}', '{email}', '{phone}')")
    con.commit()

    print("data inserted")
    t1.delete(0, END)
    t2.delete(0, END)
    t3.delete(0, END)

l1 = Label(root, text="username").place(x=100, y=100)
l2 = Label(root, text="email").place(x=100, y=150)
l3 = Label(root, text="phone").place(x=100, y=200)

t1 = Entry(root)
t1.place(x=200, y=100)
t2 = Entry(root)
t2.place(x=200, y=150)
t3 = Entry(root)
t3.place(x=200, y=200)

b1 = Button(root, text="submit", command=add).place(x=100, y=250)

root.mainloop()