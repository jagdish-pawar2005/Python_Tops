# Write a Python program to insert data into an SQLite3 database and fetch it.
import mysql.connector as sql
# connect to the database
con = sql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="university"
)
cursor = con.cursor()
# create table
qry = "CREATE TABLE IF NOT EXISTS college (id INT, name VARCHAR(20), address VARCHAR(20))"
cursor.execute(qry)
print("Table created")