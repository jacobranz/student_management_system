from types import ClassMethodDescriptorType
import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
	host = "127.0.0.1",
	user = "root",
	#password = "1234" --- still need to figure out how to encrypt this for authentication with password.
	database="SCHOOL_MANAGEMENT"
)

# Creating an instance of 'cursor' class
# which is used to execute the 'SQL'
# statements in 'Python'
cursor = mydb.cursor()

#cursor.execute("CREATE TABLE student (student_ID INT, first_name CHAR(255), last_name CHAR(255), classes VARCHAR(255), grade_level VARCHAR(255), age SMALLINT)")
#cursor.execute("CREATE TABLE professor (professor_ID INT, first_name CHAR(255), last_name CHAR(255), classes VARCHAR(255), class_count SMALLINT, start_date DATE)")
#cursor.execute("CREATE TABLE class (class_ID INT, name VARCHAR(255), teacher_first CHAR(255), teacher_last CHAR(255), student_first CHAR(255), student_last CHAR(255), grade_level CHAR(255))")
#cursor.execute("CREATE TABLE student_class (student_ID INT, class_ID INT)")
#cursor.execute("CREATE TABLE teacher_class (teacher_ID INT, class_ID INT)")
#cursor.execute("CREATE TABLE student_class_grade (student_ID INT, class_ID INT, assignment_grade FLOAT(24), weight FLOAT(24))")

## Insert user input into table
#stud_ID = input("Student ID: ")
#stud_first_name = input("Student First Name: ")
#stud_last_name = input("Student Last Name: ")
#stud_classes = input("Student Classes (comma separated): ")
#stud_grade_level = input("Student Grade Level: ")
#stud_age = input("Student Age: ")

## Insert Professor data into table
prof_ID = input("Professor ID: ")
prof_first_name = input("Professor First Name: ")
prof_last_name = input("Professor Last Name: ")
prof_class_count = input("Professor Class Count: ")
prof_start_date = input("Professor Start Date: ")

#cursor.execute("""
#NSERT INTO student (student_ID, first_name, last_name, classes, grade_level, age)
#VALUES (%s,%s,%s,%s,%s,%s)
#""", (stud_ID, stud_first_name, stud_last_name, stud_classes, stud_grade_level, stud_age))
#mydb.commit()

cursor.execute("SHOW TABLES")

for x in cursor:
    print(x)