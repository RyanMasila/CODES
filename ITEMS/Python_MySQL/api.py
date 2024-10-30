from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
import json

app = Flask(__name__)
CORS(app)

mydb = mysql.connector.connect(
    host="localhost",
    username="root",
    password="Ryan@6881",
    database="MyDATABASE"
)

mycursor = mydb.cursor()


@app.route('/')
def index():
    return "Welcome to MyAPI"

@app.route('/app/api/v1.0/Customers', methods=['GET'])
def get_Customers():
    sql = "SELECT * FROM Customers"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return jsonify([customer for customer in result])


if __name__ =='__main__':
    app.run(debug=True)