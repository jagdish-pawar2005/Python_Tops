from tkinter import *
from tkinter import ttk
import mysql.connector as sql

con = sql.connect(
    host="localhost",
    user="root",
    password="root",
    database="company"
)

cursor = con.cursor()

root = Tk()
root.title("Employee Registration System")
root.geometry("1000x600")
root.config(bg="#f0f0f0")

# ---------------- TITLE ----------------
title = Label(root,text="Employee Registration System",
              font=("Arial",20,"bold"),
              bg="#2c3e50",fg="white",pady=10)

title.pack(fill=X)

# ---------------- LEFT FRAME (FORM) ----------------
form_frame = Frame(root,bg="white",bd=2,relief=RIDGE)
form_frame.place(x=20,y=80,width=350,height=450)

Label(form_frame,text="Registration Form",
      font=("Arial",16,"bold"),bg="white").pack(pady=10)

# Labels
Label(form_frame,text="ID",bg="white").place(x=30,y=70)
Label(form_frame,text="Username",bg="white").place(x=30,y=110)
Label(form_frame,text="Email",bg="white").place(x=30,y=150)
Label(form_frame,text="Phone",bg="white").place(x=30,y=190)
Label(form_frame,text="Password",bg="white").place(x=30,y=230)
Label(form_frame,text="Address",bg="white").place(x=30,y=270)

# Entry fields
t6 = Entry(form_frame)
t6.place(x=120,y=70)

t1 = Entry(form_frame)
t1.place(x=120,y=110)

t2 = Entry(form_frame)
t2.place(x=120,y=150)

t3 = Entry(form_frame)
t3.place(x=120,y=190)

t4 = Entry(form_frame)
t4.place(x=120,y=230)

t5 = Entry(form_frame)
t5.place(x=120,y=270)

# ---------------- FUNCTIONS ----------------
def insert_data():
    qry = "INSERT INTO registration(uname,email,phone,password,address) VALUES(%s,%s,%s,%s,%s)"
    cursor.execute(qry,(t1.get(),t2.get(),t3.get(),t4.get(),t5.get()))
    con.commit()
    fetch_data()
    clear_fields()

def fetch_data():
    cursor.execute("SELECT * FROM registration")
    rows = cursor.fetchall()

    table.delete(*table.get_children())

    for row in rows:
        table.insert("",END,values=row)

def update_data():
    qry = """UPDATE registration 
             SET uname=%s,email=%s,phone=%s,password=%s,address=%s 
             WHERE uid=%s"""

    cursor.execute(qry,(t1.get(),t2.get(),t3.get(),t4.get(),t5.get(),t6.get()))
    con.commit()
    fetch_data()

def delete_data():
    qry = "DELETE FROM registration WHERE uid=%s"
    cursor.execute(qry,(t6.get(),))
    con.commit()
    fetch_data()

def clear_fields():
    t1.delete(0,END)
    t2.delete(0,END)
    t3.delete(0,END)
    t4.delete(0,END)
    t5.delete(0,END)
    t6.delete(0,END)

# ---------------- BUTTONS ----------------
Button(form_frame,text="Insert",bg="#27ae60",fg="white",
       width=10,command=insert_data).place(x=20,y=340)

Button(form_frame,text="Update",bg="#2980b9",fg="white",
       width=10,command=update_data).place(x=120,y=340)

Button(form_frame,text="Delete",bg="#c0392b",fg="white",
       width=10,command=delete_data).place(x=220,y=340)

Button(form_frame,text="Clear",bg="gray",fg="white",
       width=10,command=clear_fields).place(x=90,y=380)

# ---------------- RIGHT FRAME (TABLE) ----------------
table_frame = Frame(root,bd=2,relief=RIDGE)
table_frame.place(x=400,y=80,width=570,height=450)

scroll_y = Scrollbar(table_frame,orient=VERTICAL)

table = ttk.Treeview(table_frame,
                     columns=("id","name","email","phone","password","address"),
                     yscrollcommand=scroll_y.set)

scroll_y.pack(side=RIGHT,fill=Y)
scroll_y.config(command=table.yview)

table.heading("id",text="ID")
table.heading("name",text="Name")
table.heading("email",text="Email")
table.heading("phone",text="Phone")
table.heading("password",text="Password")
table.heading("address",text="Address")

table['show']="headings"

table.pack(fill=BOTH,expand=1)

fetch_data()

root.mainloop()