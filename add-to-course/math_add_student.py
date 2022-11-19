import tkinter as tk
import mysql.connector
from tkinter import messagebox

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "ctu1234",
    database = "grades"
)

cursor = mydb.cursor()

max_students = 20

def add_student():
    ## get the student ID of the last name entered
    cursor.execute("select student_ID from student where last_name = %s", (last_name.get(),))
    student_last = cursor.fetchall()
    for student in student_last:
        student = student[0]
    if len(student_last) == 0:
        messagebox.showwarning("No Entry Found", "Student entered does not exist in the system!")
        quit()

    ## get student count and ensure it is beneath the max amount
    cursor.execute("select student_ID from gradebook where course_ID = 2")
    students = cursor.fetchall()
    if len(students) > max_students:
        messagebox.showwarning("Adding Error", "Max amount of students for this class has been reached!")
        quit()
   
    ## insert the value of student ID into the enrollment table with the appropriate class
    cursor.execute("insert into enrollment values (%s, 2)", (student,))
    mydb.commit()
    
    ## insert student into gradebook where assignments can be assigned to them and later graded
    sql = "insert into gradebook values (%s, 2, %s, 0, 25)"
    val = [
        (student, 'Project 1'),
        (student, 'Project 2'),
        (student, 'Project 3'),
        (student, 'Final')
    ]
    cursor.executemany(sql, val)
    mydb.commit()
    messagebox.showinfo("Success", "Student has been added to Math 150!")

    ## clear entry field to add more students
    last_name.set("")

window = tk.Tk()
window.title("Add Student to Course")
window.geometry("500x300")

## create all tkinter variables
last_name = tk.StringVar()

## create all labels
tk.Label(window, text="Student Last Name").grid(row=0, column=0)

## create all entries
tk.Entry(window, textvariable=last_name).grid(row=0, column=1)

## create all buttons
tk.Button(window, text="Add", command=add_student, width=5).grid(row=2, column=0)

window.mainloop()