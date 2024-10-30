import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "Ryan@6881",
    database = "MyDATABASE"
)

mycursor = mydb.cursor();

sql = "DELETE FROM Customers WHERE address = %s"
val = ('Lowstreet 4',)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")