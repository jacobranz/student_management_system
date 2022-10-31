import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
	host = "127.0.0.1",
	user = "root",
	#password = "1234" --- still need to figure out how to encrypt this for authentication with password.
)

# Set all possible databases
databases = ["STUDENT", "TEACHER", "CLASS"]

# Creating an instance of 'cursor' class
# which is used to execute the 'SQL'
# statements in 'Python'
cursor = mydb.cursor()

# Show database
cursor.execute("SHOW DATABASES")

for x in cursor:
    print(x)