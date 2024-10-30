import MySQLdb
db = MySQLdb.connect(host="localhost", user="root", password="Ryan@6881", db="Institute")
cur = db.cursor()
names = ("Ryan Masila Nzyimi", "Bob Kariuki", "Ace Kariuki")
for name in names:
    cur.execute("INSERT INTO Students (StdName) VALUES (%s)", name)
    # print ("AUTO iNCREMENT ID: %s" % cur.lastrowid)