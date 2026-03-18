import mysql.connector as sql
con = sql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="university"
)
# print("connect :)")
cursor = con.cursor()

# create database

# qry="create database university"           
# cursor.execute(qry)               
# print("database created successfully")

# created table
# qry = "create table college (id int, name varchar(20), address varchar(20))"  
# cursor.execute(qry)

# sending the single data into the database
# qry ="insert into college values (2,'chetan','ahmdabad')"   
# cursor.execute(qry)

# data =[ 
#     (3,'nikhil','pune'),
#     (4,'shubham','pune'),
#     (5,'umesh','west bangal')
# ]

# qry = "insert into college(id, name, address) values(%s ,%s ,%s)"
# cursor.executemany(qry,data)

# qry = "select *from college"
# cursor.execute(qry)
# data = cursor.fetchall()
# # print(data)

# for i in data:
#     print(i)

qry= "select *from college where address ='pune' "
cursor.execute(qry)
data = cursor.fetchall()
print(data)

con.commit()
# print("data inserted")


