import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "Ryan@6881",
    database = "MyDATABASE"
)

mycursor = mydb.cursor();

# ------- WHERE -------
# sql = "SELECT * FROM Customers WHERE address = 'Park Lane 38'"
# mycursor.execute(sql)
# result = mycursor.fetchall()

# for x in result:
#     print(x)

# ------- % --------
# sql = "SELECT * FROM Customers WHERE address LIKE '%way%'"

# mycursor.execute(sql)

# result = mycursor.fetchall()

# for x in result:
#     print(x)

# -------- ESCAPING QUERY VALUES --------

sql = "SELECT * FROM Customers WHERE address = %s"
val = ("GITHURAI 45",)

mycursor.execute(sql, val)
result = mycursor.fetchall()

for x in result:
     print(x)