from types import ClassMethodDescriptorType
import mysql.connector
from numpy import append
import pandas as pd

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    #password = "1234", ## My databse currently has no password
    auth_plugin='mysql_native_password',
    database = "SCHOOL_MANAGEMENT"
)

cursor = mydb.cursor()

## Create database tables based on current use cases
cursor.execute("CREATE TABLE IF NOT EXISTS student (student_ID INT primary key auto_increment, first_name CHAR(255), last_name CHAR(255), courses VARCHAR(255), grade_level VARCHAR(255), age SMALLINT)")
cursor.execute("CREATE TABLE IF NOT EXISTS professor (professor_ID INT, first_name CHAR(255), last_name CHAR(255), classes VARCHAR(255), class_count SMALLINT, start_date DATE)")
cursor.execute("CREATE TABLE IF NOT EXISTS course (course_ID INT, name VARCHAR(255), professor_first CHAR(255), professor_last CHAR(255), student_first CHAR(255), student_last CHAR(255), grade_level CHAR(255))")
cursor.execute("CREATE TABLE IF NOT EXISTS student_course (student_ID INT references student(student_ID), course_ID INT references course(course_ID))")
cursor.execute("CREATE TABLE IF NOT EXISTS professor_course (professor_ID INT references professor(professor_ID), course_ID INT references course(course_ID))")
cursor.execute("CREATE TABLE IF NOT EXISTS student_course_grade (student_ID INT references student(student_ID), class_ID INT references class(class_ID), assignment_grade FLOAT(24), weight FLOAT(24))")
mydb.commit()

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
class Student(Person): # Inherited from Person class

    ## Button correlates to each one of these functions
    ## At the end of the class, all of the data will be entered into the database
    def __init__(self):
        self.courses = []

    def set_id(self, id): ## Implement logic to auto generate GUID
        self.id = id
        
    def set_first_name(self, first_name): ## When entering student first name in GUI, the button runs this command 
        self.first_name = first_name
    
    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_age(self, age):
        self.age = age

    def set_courses(self, courses):
        self.course = courses.strip().split(", ")
        for course in self.course:
            self.courses.append(course)
        
    def set_grade_level(self, grade_level):
        self.grade_level = grade_level

    def get_courses(self): ## Should not store course information here but rather students in course class
        for course in self.courses:
            print(course)

    def write_database(self):
        cursor.execute("""
        INSERT INTO student (student_ID, first_name, last_name, classes, grade_level, age)
        VALUES (%s,%s,%s,NULL,%s,%s)
        """, (self.id, self.first_name , self.last_name, self.grade_level, self.age))
        mydb.commit()

class Professor(Person):
    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_age(self, age):
        self.age = age

class Course:
    def __init__(self):
        pass

    def set_course_id(self):
        pass ## Implement auto generated GUID

    def set_course_name(self, name):
        self.course_name = name

    def set_course_desc(self, desc):
        self.course_desc = desc

    def set_max_students(self, max):
        self.max_students = max

    def set_student(self, student):
        self.student = student
        ## Query student to add

## Class for adding assignments to courses and assigning grades - may not be necessary
class Assignment:
    pass

    
s = Student()
s.set_id(69)
s.set_first_name("Kassie")
s.set_last_name("Estrada")
s.set_age("22")
s.set_courses("History, Math") ## Output of array does not work inputting into database yet
s.set_grade_level(16)
s.write_database()