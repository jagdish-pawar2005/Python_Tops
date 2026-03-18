import sqlite3  

con = sqlite3.connect("data.db")
qry = "CREATE TABLE STUDENT (id int primary key, name varchar(20),email varchar(50))"
qry = "insert into STUDENT values(2, 'chetan','chetan32@gmail.com')"

# qry = "update STUDENT set name='chetan kumar' where id=2"

qry = "delete from STUDENT where id=2"


# qry = "insert into student values"

con.execute(qry)
con.commit()