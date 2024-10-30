import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    username="root",
    password="Ryan@6881",
    database="MyDATABASE"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Customers (name, address) VALUES (%s, %s)"

val = [
    ("Bob Kariuki", "GITHURAI 45"),
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hannah', 'Mountain 21'),
    ('Michael', 'Valley 345'),
    ('Sandy', 'Ocean blvd 2'),
    ('Betty', 'Green Grass 1'),
    ('Richard', 'Sky st 331'),
    ('Susan', 'One way 98'),
    ('Vicky', 'Yellow Garden 2'),
    ('Ben', 'Park Lane 38'),
    ('William', 'Central st 954'),
    ('Chuck', 'Main Road 989'),
    ('Viola', 'Sideway 1633')

]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "rows inserted")