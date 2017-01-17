from django.test import TestCase

# Create your tests here.
#!/usr/bin/python
import MySQLdb

# Setup MySQL Connection
db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="students_db")
cursor = db.cursor()

# Insert a row into our table
cursor.execute("INSERT INTO students_mobile (mobile_number, pin_number) VALUES ('2138143752', 5)")

# Save changes to database
db.commit()