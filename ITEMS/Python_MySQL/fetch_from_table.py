import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    username="root",
    password="Ryan@6881",
    database="MyDATABASE"
)

mycursor = mydb.cursor()

# -------- SELECTING ALL ROWS FROM A TABLE ---------
# mycursor.execute("SELECT * FROM Customers")
# result = mycursor.fetchall() # fetches all rows from the last executed statement

# for x in result:
#     print(x)

# -------- SELECTING SPECIFIC COLUMS FROM A TABLE ---------
# mycursor.execute("SELECT name, address FROM Customers")
# result = mycursor.fetchall()
# for i in result:
#     print(i)

# -------- SELECTING ONE ROW FROM A TABLE ---------
mycursor.execute("SELECT * FROM Customers")

result = mycursor.fetchone() # fetchone() returms the first row of the result

print(result)