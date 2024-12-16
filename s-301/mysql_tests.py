# mysql_tests.py

import pymysql

# Establish the connection
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="yourdatabase"
)

print("Connected to MySQL database!")
