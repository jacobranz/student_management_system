import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from dateutil.parser import *
from dateutil.rrule import *

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    #password = "1234", ## My databse currently has no password
    #auth_plugin='mysql_native_password',
    database = "grades"
)

cursor = mydb.cursor()

cursor.execute("create database if not exists grades")
cursor.execute("CREATE TABLE IF NOT EXISTS student (student_ID INT primary key auto_increment, first_name CHAR(255), last_name CHAR(255), age SMALLINT, grade_level VARCHAR(255))")
cursor.execute("CREATE TABLE IF NOT EXISTS professor (professor_ID INT primary key auto_increment, first_name CHAR(255), last_name CHAR(255), age SMALLINT, qualifications CHAR(255), start_date DATE)")
cursor.execute("CREATE TABLE IF NOT EXISTS course (course_ID INT primary key auto_increment, name VARCHAR(255), creds INT, professor_ID INT, FOREIGN KEY (professor_ID) REFERENCES professor(professor_ID))")
cursor.execute("CREATE TABLE IF NOT EXISTS enrollment (student_ID INT, course_ID INT, FOREIGN KEY (student_ID) REFERENCES student(student_ID), FOREIGN KEY (course_ID) REFERENCES course(course_ID))")
cursor.execute("CREATE TABLE IF NOT EXISTS gradebook (student_ID INT, course_ID INT, assignment VARCHAR(255), score FLOAT, weight INT, FOREIGN KEY (student_ID) REFERENCES student(student_ID), FOREIGN KEY (course_ID) REFERENCES course(course_ID))")

def write_student():
    cursor.execute('''
    INSERT INTO student (student_ID, first_name, last_name, age, grade_level)
    VALUES (%s, %s, %s, %s, %s)
    ''', (id_var.get(), first_var.get(), last_var.get(), age_var.get(), grade_var.get()))
    mydb.commit()



def student_gui():
    root = tk.Tk()
    root.geometry("450x300")
    root.title('Student Add')

    id_var = tk.IntVar()
    first_var = tk.StringVar()
    last_var = tk.StringVar()
    age_var = tk.IntVar()
    grade_var = tk.IntVar()

    id_label = tk.Label(root, text = "ID").place(x=40, y=60)
    first_label = tk.Label(root, text = "First Name").place(x=40, y=80)
    last_label = tk.Label(root, text = "Last Name").place(x=40,y=100)
    age_label = tk.Label(root, text = "Age").place(x=40,y=120)
    grade_label = tk.Label(root, text = "Grade Level").place(x=40,y=140)

    id_entry = tk.Entry(root, textvariable = id_var, width=30).place(x=130,y=60)
    first_entry = tk.Entry(root, textvariable = first_var, width=30).place(x=130,y=80)
    last_entry = tk.Entry(root, textvariable = last_var, width=30).place(x=130, y=100)
    age_entry = tk.Entry(root, textvariable = age_var, width=30).place(x=130,y=120)
    grade_entry = tk.Entry(root, textvariable = grade_var, width=30).place(x=130,y=140)

    submit_button = tk.Button(root, text='Write to Database', command=write_student).place(x=160,y=170)

    root.mainloop()


class Professor():

    def __init__(self):
        root = tk.Tk()
        root.geometry("450x300")
        root.title('Professor Add')

        self.id_var = tk.IntVar()
        self.first_var = tk.StringVar()
        self.last_var = tk.StringVar()
        self.age_var = tk.IntVar()
        self.qual_var = tk.StringVar()
        self.start_var = tk.StringVar()

        self.id_label = tk.Label(root, text = "ID").place(x=40, y=60)
        self.first_label = tk.Label(root, text = "First Name").place(x=40, y=80)
        self.last_label = tk.Label(root, text = "Last Name").place(x=40,y=100)
        self.age_label = tk.Label(root, text = "Age").place(x=40,y=120)
        self.qual_label = tk.Label(root, text = "Qualifications").place(x=40,y=140)
        self.start_label = tk.Label(root, text = "Start Date").place(x=40,y=160)

        self.id_entry = tk.Entry(root, textvariable = self.id_var, width=30).place(x=130,y=60)
        self.first_entry = tk.Entry(root, textvariable = self.first_var, width=30).place(x=130,y=80)
        self.last_entry = tk.Entry(root, textvariable = self.last_var, width=30).place(x=130, y=100)
        self.age_entry = tk.Entry(root, textvariable = self.age_var, width=30).place(x=130,y=120)
        self.qual_entry = tk.Entry(root, textvariable = self.qual_var, width=30).place(x=130,y=140)
        self.start_entry = tk.Entry(root, textvariable = self.start_var, width=30).place(x=130,y=160)

        submit_button = tk.Button(root, text='Write to Database', command=self.write_professor).place(x=160,y=190)

        root.mainloop()

    def write_professor(self):
        start_date = datetime.strptime(self.start_var.get(), '%Y-%m-%d').date()
        cursor.execute('''
        INSERT INTO professor (professor_ID, first_name, last_name, age, qualifications, start_date)
        VALUES (%s, %s, %s, %s, %s, %s)
        ''', (self.id_var.get(), self.first_var.get(), self.last_var.get(), self.age_var.get(), self.qual_var.get(), self.start_var.get()))
        mydb.commit()

Professor()