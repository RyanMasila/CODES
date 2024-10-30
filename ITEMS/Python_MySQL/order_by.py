import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "Ryan@6881",
    database = "MyDATABASE"
)

mycursor = mydb.cursor();

# -------- ORDER BY ASCENDING --------
# sql = "SELECT * FROM Customers ORDER BY name"

# mycursor.execute(sql)

# result = mycursor.fetchall()

# for x in result:
#     print(x)

# --------- ORDER BY DESCENDING ---------
sql = "SELECT * FROM Customers ORDER BY name DESC"

mycursor.execute(sql)

result = mycursor.fetchall()

for x in result:
    print(x)