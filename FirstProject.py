import tkinter as tk
from tkinter import *
import mysql.connector
from tkinter import messagebox
import test_database_build
from datetime import datetime
from dateutil.parser import *
from dateutil.rrule import *

class studentAdd:
    
    def __init__(self):
        root = tk.Tk()
        root.geometry("450x300")
        root.title('Student Add')

        self.id_var = test_database_build.Student.set_id()
        self.first_var = tk.StringVar()
        self.last_var = tk.StringVar()
        self.age_var = tk.IntVar()
        self.grade_var = tk.IntVar()

        self.first_label = tk.Label(root, text = "First Name").place(x=40, y=80)
        self.last_label = tk.Label(root, text = "Last Name").place(x=40,y=100)
        self.age_label = tk.Label(root, text = "Age").place(x=40,y=120)
        self.grade_label = tk.Label(root, text = "Grade Level").place(x=40,y=140)

        self.first_entry = tk.Entry(root, textvariable = self.first_label, width=30).place(x=130,y=60)
        self.last_entry = tk.Entry(root, textvariable = self.last_label, width=30).place(x=130, y=80)
        self.age_entry = tk.Entry(root, textvariable = self.age_var, width=30).place(x=130,y=100)
        self.grade_entry = tk.Entry(root, textvariable = self.grade_var, width=30).place(x=130,y=120)

        self.submite_button = tk.Button(root, text='Write to Database', command=self.write).place(x=160,y=170)

        root.mainloop()

    def write(self):
        test_database_build.cursor.execute('''
        INSERT INTO student (student_ID, first_name, last_name, age, grade_level)
        VALUES (%s, %s, %s, %s, %s)
        ''', (self.id_var, self.first_var.get(), self.last_var.get(), self.age_var.get(), self.grade_var.get()))
        test_database_build.mydb.commit()

class studentModify:
    pass

class studentRemove:
    pass
        
class professorAdd:
    def __init__(self):
        root = tk.Tk()
        root.geometry("450x300")
        root.title("Add Professor")

        self.id_var = 22 #test_database_build.Professor.set_id(self)
        self.first_var = tk.StringVar()
        self.last_var = tk.StringVar()
        self.age_var = tk.IntVar()
        self.qual_var = tk.StringVar()
        self.start_var = tk.StringVar()

        self.first_label = tk.Label(root, text = "First Name").place(x=40, y=60)
        self.last_label = tk.Label(root, text = "Last Name").place(x=40, y=80)
        self.age_label = tk.Label(root, text = "Age").place(x=40, y=100)
        self.qual_label = tk.Label(root, text = "Qualifications").place(x=40, y=120)
        self.start_label = tk.Label(root, text = "Start Date").place(x=40,y=140)

        self.first_entry = tk.Entry(root, textvariable=self.first_var, width=30).place(x=130,y=60)
        self.last_entry = tk.Entry(root, textvariable=self.last_var, width=30).place(x=130,y=80)
        self.age_entry = tk.Entry(root, textvariable=self.age_var, width=30).place(x=130,y=100)
        self.qual_entry = tk.Entry(root, textvariable=self.qual_var, width=30).place(x=130,y=120)
        self.start_entry = tk.Entry(root, textvariable=self.start_var, width=30).place(x=130,y=140)

        self.submit_button = tk.Button(root, text="Submit", command=self.write).place(x=160,y=170)

        root.mainloop()

    def write(self):
        start_date = datetime.strptime(self.start_var.get(), '%Y-%m-%d').date()
        test_database_build.cursor.execute('''
        INSERT INTO professor (professor_ID, first_name, last_name, age, qualifications, start_date)
        VALUES (%s, %s, %s, %s, %s, %s)
        ''', (self.id_var, self.first_var.get(), self.last_var.get(), self.age_var.get(), self.qual_var.get(), start_date))
        test_database_build.mydb.commit()

class professorModify:
    pass
    ## Need to be able to query results of search to the screen

class professorRemove:
    pass
