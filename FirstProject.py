import tkinter as tk
from tkinter import *
import mysql.connector
from tkinter import messagebox
import test_database_build

class studentAdd:
    
    def __init__(self):
        root = tk.Tk()
        root.geometry("450x300")
        root.title('Student Management System')

        self.id = test_database_build.Student.set_id()
        self.first = tk.StringVar()
        self.last = tk.StringVar()
        self.grade = tk.IntVar()

        self.display = tk.Label(root, text = "First Name").place(x=40, y=60)

        self.last_name = tk.Label(root, text = "Last Name").place(x=40, y=80)

        self.button = tk.Button(root, text='Write to Database', command=self.write).place(x=75, y=130)

        first_entry = tk.Entry(root, textvariable = self.first, width=30).place(x=110,y=60)

        last_entry = tk.Entry(root, textvariable = self.last, width=30).place(x=110, y=80)

        root.mainloop()

    def write(self):
        self.first_name = self.first.get()
        self.last_name = self.last.get()
        print("First Name: " + self.first_name)
        print("Last Name: " + self.last_name)
    #    con = pymysql.connect(host="localhost", user="root", password="ctu1234", database="batman")
    #    cur = con.cursor()
    #    cur.execute("insert into students values(%s, %s)", (self.id_var.get(), self.last.get()))
    #    con.commit()
    #    con.close()
    #    messagebox.showinfo("Successfull", "Record has been inserted.")
        
class professorAdd:
    def __init__(self):
        root = tk.Tk()
        root.geometry("450x300")
        root.title("Add Professor")

        self.id_var = test_database_build.Professor.set_id(self)
        self.first_var = tk.StringVar()
        self.last_var = tk.StringVar()
        self.age_var = tk.IntVar()
        self.qual_var = tk.StringVar()

        self.first_label = tk.Label(root, text = "First Name").place(x=40, y=60)
        self.last_label = tk.Label(root, text = "Last Name").place(x=40, y=80)
        self.age_label = tk.Label(root, text = "Age").place(x=40, y=100)
        self.qual_label = tk.Label(root, text = "Qualifications").place(x=40, y=120)

        self.first_entry = tk.Entry(root, textvariable=self.first_var, width=30).place(x=130,y=60)
        self.last_entry = tk.Entry(root, textvariable=self.last_var, width=30).place(x=130,y=80)
        self.age_entry = tk.Entry(root, textvariable=self.age_var, width=30).place(x=130,y=100)
        self.qual_entry = tk.Entry(root, textvariable=self.qual_var, width=30).place(x=130,y=120)

        self.submit_button = tk.Button(root, text="Submit", command=self.write).place(x=160,y=150)

        root.mainloop()

    def write(self):
        self.first_name = self.first_var.get()
        self.last_name = self.last_var.get()
        self.age = self.age_var.get()
        self.qual = self.qual_var.get()
        print("ID: ", self.id_var)
        print("First Name: " + self.first_name)
        print("Last Name: " + self.last_name)
        print("Age: ", self.age)
        print("Qualifications: " + self.qual)

professorAdd()
