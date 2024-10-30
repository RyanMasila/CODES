

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "Ryan@6881",
    database = "MyDATABASE"
)

mycursor = mydb.cursor();
# mycursor.execute("CREATE DATABASE MyDATABASE")
# mycursor.execute("SHOW TABLES")

# mycursor.execute("CREATE TABLE Customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
sql = "INSERT INTO Customers (name, address) VALUES (%s, %s)"
val = ("Ace Kariuki", "GITHURAI 45")
mycursor.execute(sql, val)
mydb.commit() # it is required to make the changes to the table
# print(mycursor.rowcount, "record inserted")
print("1 record inserted, ID: ", mycursor.lastrowid) # returns the id of the last row inserted
# print(mydb)