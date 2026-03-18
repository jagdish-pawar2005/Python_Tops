import mysql.connector as sql

con = sql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root"
)

print("Connected Successfully")