# Write a Python program to connect to an SQLite3 database, create a table, insert data, and fetch data.
import mysql.connector as sql
con = sql.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "root",
    database = "company"
) 
# print("connected")

cursor = con.cursor()

# create tabel 
# qry = "create table school(id int, name varchar(20), email varchar(20))"
# cursor.execute(qry)
# print("table is created")


# insert data 
qry = "insert into school values(1, 'chetan' , 'chetan35@gmail.com') "
cursor.execute(qry)

con.commit()
print("data insert")

#featch the data
cursor.execute("select * from school")
data = cursor.fetchall()
print(data)
