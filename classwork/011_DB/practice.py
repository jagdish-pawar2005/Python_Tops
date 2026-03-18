import mysql.connector as sql 
con = sql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="company"
)
# print("connect")

cursor = con.cursor()

# qry = "create database company"
# cursor.execute(qry)
# print("database createdd")

# qry ="create table employe (id int, name varchar(20), email varchar(20), phone int)"
# cursor.execute(qry)
# print("table created")

# qry = "insert into employe values(1 ,'chetan','chetan21@gmail.com',24578981)"
# cursor.execute(qry)
# print("data inserted")

# data = [
#     (2,'nikhil','nikhil@gmail.com',2457892582),
#     (3,'sonu','sonu@gmail.com',2457892583),
#     (4,'shubham','shubham@gmail.com',2457892584)
# ]

# qry =" insert into employe(id, name, email, phone) values (%s,%s,%s,%s)"
# cursor.executemany(qry,data)
# print("data added")
# con.commit()

# qry = "select *from employe"
# cursor.execute(qry)
# data=cursor.fetchall()
# # print(data)

# for i in data : 
#     print(i)

# 1️⃣ Show Only Employee Names
qry = "select name from employe"
cursor.execute(qry)
data = cursor.fetchall()
print(data)