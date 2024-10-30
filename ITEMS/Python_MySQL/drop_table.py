import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "Ryan@6881",
    database = "MyDATABASE"
)

mycursor = mydb.cursor();

sql = "DROP TABLE IF EXISTS Customers"

mycursor.execute(sql)