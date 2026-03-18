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

# insert data
qry = "INSERT INTO college VALUES (2, 'chetan', 'Ahmedabad')"
cursor.execute(qry)

con.commit()
print("Data inserted")

# fetch data
cursor.execute("SELECT * FROM college")
data = cursor.fetchall()

print("Records:")
for row in data:
    print(row)

con.close()