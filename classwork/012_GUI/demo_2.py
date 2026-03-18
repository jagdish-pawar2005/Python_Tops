from tkinter import *
import mysql.connector as sql

con = sql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="company"
)

cursor = con.cursor()

root = Tk()
root.geometry("400x400")
root.title("My App")

def add():
    uname = t1.get()
    email = t2.get()
    phone = t3.get()

    query = "INSERT INTO reg (uname,email,phone) VALUES (%s,%s,%s)"
    values = (uname,email,phone)

    cursor.execute(query,values)
    con.commit()

    print("Data Inserted")

    t1.delete(0,END)
    t2.delete(0,END)
    t3.delete(0,END)

Label(root,text="Username").place(x=100,y=100)
Label(root,text="Email").place(x=100,y=150)
Label(root,text="Phone").place(x=100,y=200)

t1 = Entry(root)
t1.place(x=200,y=100)

t2 = Entry(root)
t2.place(x=200,y=150)

t3 = Entry(root)
t3.place(x=200,y=200)

Button(root,text="Submit",command=add).place(x=150,y=250)

root.mainloop()