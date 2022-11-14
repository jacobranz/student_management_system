import tkinter as tk
import school_manage_home

def find_student():

    sql = "select student_ID from student where last_name = %s"
    adr = (last_name.get(),)

    school_manage_home.cursor.execute(sql, adr)
    for student in school_manage_home.cursor.fetchall():
        student_ID = student[0]
    # gets all courses that student is in
    school_manage_home.cursor.execute('''select gradebook.assignment from gradebook where
                                        gradebook.student_ID = %s and gradebook.course_ID = 1''', (student_ID,))
    assignment_list = school_manage_home.cursor.fetchall()
    

    i=0
    row=6
    column=0
    for assignment in assignment_list:
        if assignment == "":
            break
        
        tk.Label(master, text=assignment[0]).grid(row=(row + i), column=column)
        #grades.append(tk.IntVar())
        grades[i] = tk.IntVar()
        entries.append(tk.Entry(master, textvariable=grades[i], width=5).grid(row=(row + i), column=1))

        i+=1
    
def submit_grades():
    for entry in entries:
        print(entry)
    for grade in grades:
        print(grade)

entries = []
grade1 = 0
grade2 = 0
grade3 = 0
grade4 = 0
grades = [grade1, grade2, grade3, grade4]

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

# Name age roll entries
e1=tk.Entry(master, textvariable=last_name)

# organizing them in the grid
e1.grid(row=0, column=1)

# button to display all the calculated credit scores and sgpa
find_button = tk.Button(master, text="Find", command=find_student)
find_button.grid(row=0,column=2)
submit_button = tk.Button(master, text="Submit", command=submit_grades).grid(row=13, column=0)


master.mainloop()