import customtkinter as ctk
import mysql.connector
from tkinter import messagebox

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "ctu1234",
    database = "grades"
)

cursor = mydb.cursor()

def clear():
    for label in master.grid_slaves():
        if int(label.grid_info()["row"]) > 2:
            label.grid_forget()

    last_name.set("")

    ctk.CTkButton(master, text="Submit", command=submit_grades).grid(row=13, column=0)

def find_student():

    sql = "select student_ID from student where last_name = %s"
    adr = (last_name.get(),)

    cursor.execute(sql, adr)
    students = cursor.fetchall()
    for student in students:
        student_ID = student[0]

    ## throw warning if student does not exist
    if len(students) == 0:
        messagebox.showwarning("No Entry Found", "Student entered does not exist in the system!")
        last_name.set("")

    ## get all assignments in the course
    cursor.execute('''select gradebook.assignment from gradebook where
                                        gradebook.student_ID = %s and gradebook.course_ID = 4''', (student_ID,))
    assignment_list = cursor.fetchall()
    

    i=0
    row=6
    column=0
    for assignment in assignment_list:
        if assignment == "":
            break
        
        ctk.CTkLabel(master, text=assignment[0]).grid(row=(row + i), column=column)
        ctk.CTkEntry(master, textvariable=eval(f'grade{i}'), width=5).grid(row=(row + i), column=1)

        i+=1

    ## define button for clearing all fields
    ctk.CTkButton(master, text="Clear", command=clear, width=20).grid(row=13, column=1)

def submit_grades():

    cursor.execute("select student_ID from student where last_name = %s", (last_name.get(),))
    for student in cursor.fetchall():
        student_ID = student[0]

    cursor.execute('''select gradebook.assignment from gradebook where
                                        gradebook.student_ID = %s and gradebook.course_ID = 4''', (student_ID,))
    assignment_list = cursor.fetchall()
    assignment0 = assignment_list[0]
    assignment1 = assignment_list[1]
    assignment2 = assignment_list[2]
    assignment3 = assignment_list[3]

    i = 0
    for grade in grades:
        cursor.execute('''update gradebook set score = %s where
                            assignment = %s and student_ID = %s and course_ID = 4''', (grade.get(), eval(f'assignment{i}[0]'), student_ID))
        mydb.commit()
        i+=1
    messagebox.showinfo("Success", "Student grades have been entered.")

entries = []

## Begin GUI
master = ctk.CTk()
master.title("Grade Book")
master.geometry("700x250")

# set entry variables
last_name = ctk.StringVar()
class1 = ctk.StringVar()

# label to enter name
ctk.CTkLabel(master, text="Student Last Name").grid(row=0, column=0)

# labels for subject codes
ctk.CTkLabel(master, text="Subject").grid(row=1, column=0)

ctk.CTkLabel(master, text="Grade").grid(row=1, column=1)
grade0 = ctk.IntVar()
grade1 = ctk.IntVar()
grade2 = ctk.IntVar()
grade3 = ctk.IntVar()
grades = [grade0, grade1, grade2, grade3]

ctk.CTkLabel(master, text="Weight").grid(row=1, column=2)
weight0 = ctk.IntVar()
weight1 = ctk.IntVar()
weight2 = ctk.IntVar()
weight3 = ctk.IntVar()
weights = [weight0, weight1, weight2, weight3]

# Name age roll entries
e1=ctk.CTkEntry(master, textvariable=last_name)

# organizing them in the grid
e1.grid(row=0, column=1)

# button to display all the calculated credit scores and sgpa
find_button = ctk.CTkButton(master, text="Find", command=find_student)
find_button.grid(row=0,column=2)
submit_button = ctk.CTkButton(master, text="Submit", command=submit_grades).grid(row=13, column=0)


master.mainloop()
