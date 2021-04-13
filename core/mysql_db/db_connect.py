"""
https://mysqlclient.readthedocs.io/user_guide.html#mysqldb-mysql
"""

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","root@123","msmother_pharma" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print("Database version : %s " % data)

# disconnect from server
db.close()
