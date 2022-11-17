import tkinter as tk
import mysql.connector

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "ctu1234",
    database = "grades"
)

cursor = mydb.cursor()

def clear():
    for label in master.grid_slaves():
        if 1 < int(label.grid_info()["row"]) < 14:
            label.grid_forget()

    tk.Label(master, text="Subject").grid(row=1, column=0)
    tk.Label(master, text="Grade").grid(row=1, column=1)

    submit_button = tk.Button(master, text="Submit", command=submit_grades).grid(row=13, column=0)

def find_student():

    sql = "select student_ID from student where last_name = %s"
    adr = (last_name.get(),)

    cursor.execute(sql, adr)
    for student in cursor.fetchall():
        student_ID = student[0]
    # gets all courses that student is in
    cursor.execute('''select gradebook.assignment from gradebook where
                                        gradebook.student_ID = %s and gradebook.course_ID = 3''', (student_ID,))
    assignment_list = cursor.fetchall()
    

    i=0
    row=6
    column=0
    for assignment in assignment_list:
        if assignment == "":
            break
        
        tk.Label(master, text=assignment[0]).grid(row=(row + i), column=column)
        #grades.append(tk.IntVar())
        #entries.append(tk.Entry(master, textvariable=grades[i], width=5).grid(row=(row + i), column=1))
        #print(grades[i])
        #for i in range(4):
            #globals()[f'grade{i}'] = tk.IntVar()
        tk.Entry(master, textvariable=eval(f'grade{i}'), width=5).grid(row=(row + i), column=1)

        i+=1

def submit_grades():

    cursor.execute("select student_ID from student where last_name = %s", (last_name.get(),))
    for student in cursor.fetchall():
        student_ID = student[0]

    cursor.execute('''select gradebook.assignment from gradebook where
                                        gradebook.student_ID = %s and gradebook.course_ID = 3''', (student_ID,))
    assignment_list = cursor.fetchall()
    assignment0 = assignment_list[0]
    assignment1 = assignment_list[1]
    assignment2 = assignment_list[2]
    assignment3 = assignment_list[3]

    i = 0
    for grade in grades:
        cursor.execute('''update gradebook set score = %s where
                            assignment = %s and student_ID = %s and course_ID = 3''', (grade.get(), eval(f'assignment{i}[0]'), student_ID))
        mydb.commit()
        i+=1
    mydb.close()

entries = []

## Begin GUI
master = tk.Tk()
master.title("Grade Book")
master.geometry("700x250")

# set entry variables
last_name = tk.StringVar()
class1 = tk.StringVar()

# label to enter name
tk.Label(master, text="Student Last Name").grid(row=0, column=0)

# labels for subject codes
tk.Label(master, text="Subject").grid(row=1, column=0)

tk.Label(master, text="Grade").grid(row=1, column=1)
grade0 = tk.IntVar()
grade1 = tk.IntVar()
grade2 = tk.IntVar()
grade3 = tk.IntVar()
grades = [grade0, grade1, grade2, grade3]

# Name age roll entries
e1=tk.Entry(master, textvariable=last_name)

# organizing them in the grid
e1.grid(row=0, column=1)

# button to display all the calculated credit scores and sgpa
find_button = tk.Button(master, text="Find", command=find_student)
find_button.grid(row=0,column=2)
submit_button = tk.Button(master, text="Submit", command=submit_grades).grid(row=13, column=0)
clear_button = tk.Button(master, text="Clear", command=clear, width=20).grid(row=14, column=1)


master.mainloop()