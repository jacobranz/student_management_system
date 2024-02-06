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

def add_student():
    ## get the student ID of the last name entered
    cursor.execute("select professor_ID from professor where last_name = %s", (last_name.get(),))
    prof_last = cursor.fetchall()
    for prof in prof_last:
        prof = prof[0]
   
    course_info = cursor.execute("select professor_ID from course where name = 'English 120'")
    cursor.fetchall()
    print(course_info)

    if len(course_info) > 0:
        messagebox.showwarning("English 120 already has a professor!")
    else:
        ## insert the professor id into the course
        cursor.execute("insert into course values (1, 'English 120', 4, %s)", (prof,))
        mydb.commit()


window = ctk.CTk()
window.title("Add Professor to Course")
window.geometry("500x300")

## create all tkinter variables
last_name = ctk.StringVar()

## create all labels
ctk.CTkLabel(window, text="Professor Last Name").grid(row=0, column=0)

## create all entries
ctk.CTkEntry(window, textvariable=last_name).grid(row=0, column=1)

## create all buttons
ctk.CTkButton(window, text="Add", command=add_student, width=5).grid(row=2, column=0)

window.mainloop()