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

def add_professor():
    ## get the professor ID of the last name entered
    cursor.execute("select professor_ID from professor where last_name = %s", (last_name.get(),))
    prof_last = cursor.fetchall()
    for prof in prof_last:
        prof = prof[0]
    if len(prof_last) == 0:
        messagebox.showwarning("No Entry Found", "Professor entered does not exist in the system!")
        quit()
   
    cursor.execute("select professor_ID from course where name = 'Math 150'")
    course_info = cursor.fetchall()
    print(course_info)

    if len(course_info) > 0:
        messagebox.showwarning("No Entry Found", "Math 150 already has a professor!")
    else:
        ## insert the professor id into the course
        cursor.execute("insert into course values (1, 'Math 150', 4, %s)", (prof,))
        mydb.commit()


window = tk.Tk()
window.title("Add Professor to Course")
window.geometry("500x300")

## create all tkinter variables
last_name = tk.StringVar()

## create all labels
tk.Label(window, text="Professor Last Name").grid(row=0, column=0)

## create all entries
tk.Entry(window, textvariable=last_name).grid(row=0, column=1)

## create all buttons
tk.Button(window, text="Add", command=add_professor, width=5).grid(row=2, column=0)

window.mainloop()