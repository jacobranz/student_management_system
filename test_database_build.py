from types import ClassMethodDescriptorType
import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "1234",
    auth_plugin='mysql_native_password',
    database = "test"
)

cursor = mydb.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS student (student_ID INT primary key auto_increment, first_name CHAR(255), last_name CHAR(255), courses VARCHAR(255), grade_level VARCHAR(255), age SMALLINT)")
cursor.execute("CREATE TABLE IF NOT EXISTS professor (professor_ID INT, first_name CHAR(255), last_name CHAR(255), classes VARCHAR(255), class_count SMALLINT, start_date DATE)")
cursor.execute("CREATE TABLE IF NOT EXISTS course (course_ID INT, name VARCHAR(255), professor_first CHAR(255), professor_last CHAR(255), student_first CHAR(255), student_last CHAR(255), grade_level CHAR(255))")
cursor.execute("CREATE TABLE IF NOT EXISTS student_course (student_ID INT references student(student_ID), course_ID INT references course(course_ID))")
cursor.execute("CREATE TABLE IF NOT EXISTS professor_course (professor_ID INT references professor(professor_ID), course_ID INT references course(course_ID))")
cursor.execute("CREATE TABLE IF NOT EXISTS student_course_grade (student_ID INT references student(student_ID), class_ID INT references class(class_ID), assignment_grade FLOAT(24), weight FLOAT(24))")
cursor.execute("INSERT INTO student (grade_level) VALUES (13)")
mydb.commit()

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
class Student(Person):
    def __init__(self):
        pass
        
    def set_first_name(self, student_ID, first_name, last_name, courses, grade_level, age):
        self.student_ID = student_ID
        self.first_name = first_name
        self.last_name = last_name
        self.courses = courses
        self.grade_level = grade_level
        self.age = age
        cursor.execute("""
                       INSERT INTO student (first_name, last_name, courses, grade_level, age) 
                       VALUES (%s,%s,%s,%s,%s)
                       """, (self.first_name, self.last_name, self.courses, self.grade_level, self.age))
        mydb.commit()
        
    def set_grade_level(self, grade_level):
        self.grade_level = grade_level
        #cursor.execute("INSERT INTO student grade_level VALUES (%s)", self.grade_level)
    
    def get_grade_level(self):
        cursor.execute("SELECT grade_level FROM student WHERE student_ID = 1")
        for x in cursor.fetchall():
            print(x)
    
    
s = Student()
s.set_first_name(4, "Jacob", "Ranz", "History", 13, 18)