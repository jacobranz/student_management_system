## File that includes all the code written
import tkinter as tk
import mysql.connector
from tkinter import messagebox
from tkinter import *

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "ctu1234",
    database = "grades"
)

cursor = mydb.cursor()

max_students = 20

class PageContainer(tk.Frame):

    def __init__(self, root):
        tk.Frame.__init__(self, root)

        self.container = container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frame = {}

        for F in (ClassPage, Math150, English120, Music100, Physics101):
            frame = F(container, self)
            self.frame[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(ClassPage)

    def show_frame(self, controller):
        if controller not in self.frame:
            self.frame[controller] = frame = controller(self.container, self)
            frame.grid(row=0, column=0, sticky="nsew")
        frame = self.frame[controller]
        frame.tkraise()

class ClassPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="CLASS SELECTION")
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Math 150", command= lambda: controller.show_frame(Math150))
        button2 = tk.Button(self, text="English 120", command= lambda: controller.show_frame(English120))
        button3 = tk.Button(self, text="Music 100", command= lambda: controller.show_frame(Music100))
        button4 = tk.Button(self, text="Physics 101", command= lambda: controller.show_frame(Physics101))

        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()

class Math150(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="MATH 150 ACTIONS")
        label.pack(padx=10, pady=10)

        button1 = tk.Button(self, text="Enter Grades", command= lambda: controller.show_frame(EnterGrades_Math150))
        button2 = tk.Button(self, text="Add Student", command= lambda: controller.show_frame(AddStudent_Math150))
        button3 = tk.Button(self, text="Add Professor", command= lambda: controller.show_frame(AddProfessor_Math150))
        button4 = tk.Button(self, text="Back to Main Menu", command= lambda: controller.show_frame(ClassPage))

        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()

class English120(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="ENGLISH 120 ACTIONS")
        label.pack(padx=10, pady=10)

        button1 = tk.Button(self, text="Enter Grades", command= lambda: controller.show_frame(EnterGrades_English120))
        button2 = tk.Button(self, text="Add Student", command= lambda: controller.show_frame(AddStudent_English120))
        button3 = tk.Button(self, text="Add Professor", command= lambda: controller.show_frame(AddProfessor_English120))
        button4 = tk.Button(self, text="Back to Main Menu", command= lambda: controller.show_frame(ClassPage))

        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()

class Music100(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="MUSIC 100 ACTIONS")
        label.pack(padx=10, pady=10)

        button1 = tk.Button(self, text="Enter Grades", command= lambda: controller.show_frame(EnterGrades_Music100))
        button2 = tk.Button(self, text="Add Student", command= lambda: controller.show_frame(AddStudent_Music100))
        button3 = tk.Button(self, text="Add Professor", command= lambda: controller.show_frame(AddProfessor_Music100))
        button4 = tk.Button(self, text="Back to Main Menu", command= lambda: controller.show_frame(ClassPage))

        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()

class Physics101(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="PHYSICS 101 ACTIONS")
        label.pack(padx=10, pady=10)

        button1 = tk.Button(self, text="Enter Grades", command= lambda: controller.show_frame(EnterGrades_Physics101))
        button2 = tk.Button(self, text="Add Student", command= lambda: controller.show_frame(AddStudent_Physics101))
        button3 = tk.Button(self, text="Add Professor", command= lambda: controller.show_frame(AddProfessor_Physics101))
        button4 = tk.Button(self, text="Back to Main Menu", command= lambda: controller.show_frame(ClassPage))

        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()

class EnterGrades_Math150(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="MATH 150")
        #label.pack(pady=10, padx=10)

        # set entry variables
        self.last_name = tk.StringVar()

        # label to enter name
        tk.Label(self, text="Student Last Name").grid(row=0, column=0)

        # labels for subject codes
        tk.Label(self, text="Subject").grid(row=1, column=0)

        tk.Label(self, text="Grade").grid(row=1, column=1)
        self.grade0 = tk.IntVar()
        self.grade1 = tk.IntVar()
        self.grade2 = tk.IntVar()
        self.grade3 = tk.IntVar()
        self.grades = [self.grade0, self.grade1, self.grade2, self.grade3]

        # Name age roll entries
        e1=tk.Entry(self , textvariable=self.last_name)

        # organizing them in the grid
        e1.grid(row=0, column=1)

        # button to display all the calculated credit scores and sgpa
        find_button = tk.Button(self, text="Find", command=self.find_student)
        find_button.grid(row=0,column=2)
        submit_button = tk.Button(self, text="Submit", command=self.submit_grades).grid(row=13, column=0)
        tk.Button(self, text="Back to Main Menu", command= lambda: controller.show_frame(ClassPage)).grid(row=14, column=1)

    def find_student(self):

        sql = "select student_ID from student where last_name = %s"
        adr = (self.last_name.get(),)

        cursor.execute(sql, adr)
        students = cursor.fetchall()
        for student in students:
            student_ID = student[0]

        ## throw warning if student does not exist
        if len(students) == 0:
            messagebox.showwarning("No Entry Found", "Student entered does not exist in the system!")
            self.last_name.set("")

        ## throw warning if student exists but is not enrolled in the class
        cursor.execute("select student_ID from enrollment where course_ID = 2 and student_ID = %s", (student_ID,))
        is_enrolled = cursor.fetchall()
        if len(is_enrolled) == 0:
            messagebox.showwarning("Not Enrolled", "Student is not enrolled in this class!")
            self.last_name.set("")

        ## get all assignments in the course
        cursor.execute('''select gradebook.assignment from gradebook where
                                            gradebook.student_ID = %s and gradebook.course_ID = 2''', (student_ID,))
        assignment_list = cursor.fetchall()
        

        i=0
        row=6
        column=0
        for assignment in assignment_list:
            if assignment == "":
                break
            
            tk.Label(self, text=assignment[0]).grid(row=(row + i), column=column)
            tk.Entry(self, textvariable=eval(f'self.grade{i}'), width=5).grid(row=(row + i), column=1)

            i+=1

        ## define button for clearing all fields
        tk.Button(self, text="Clear", command=self.clear, width=20).grid(row=13, column=1)

    def clear(self):
        for label in self.grid_slaves():
            if int(label.grid_info()["row"]) > 2:
                label.grid_forget()

        self.last_name.set("")

        tk.Button(self, text="Submit", command=self.submit_grades).grid(row=13, column=0)


    def submit_grades(self):

        cursor.execute("select student_ID from student where last_name = %s", (self.last_name.get(),))
        for student in cursor.fetchall():
            student_ID = student[0]

        cursor.execute('''select gradebook.assignment from gradebook where
                                            gradebook.student_ID = %s and gradebook.course_ID = 2''', (student_ID,))
        assignment_list = cursor.fetchall()
        assignment0 = assignment_list[0]
        assignment1 = assignment_list[1]
        assignment2 = assignment_list[2]
        assignment3 = assignment_list[3]

        i = 0
        for grade in self.grades:
            cursor.execute('''update gradebook set score = %s where
                                assignment = %s and student_ID = %s and course_ID = 2''', (grade.get(), eval(f'assignment{i}[0]'), student_ID))
            mydb.commit()
            i+=1
        messagebox.showinfo("Success", "Student grades have been entered.")

class EnterGrades_English120(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="English 120")
        #label.pack(pady=10, padx=10)

        # set entry variables
        self.last_name = tk.StringVar()

        # label to enter name
        tk.Label(self, text="Student Last Name").grid(row=0, column=0)

        # labels for subject codes
        tk.Label(self, text="Subject").grid(row=1, column=0)

        tk.Label(self, text="Grade").grid(row=1, column=1)
        self.grade0 = tk.IntVar()
        self.grade1 = tk.IntVar()
        self.grade2 = tk.IntVar()
        self.grade3 = tk.IntVar()
        self.grades = [self.grade0, self.grade1, self.grade2, self.grade3]

        # Name age roll entries
        e1=tk.Entry(self , textvariable=self.last_name)

        # organizing them in the grid
        e1.grid(row=0, column=1)

        # button to display all the calculated credit scores and sgpa
        find_button = tk.Button(self, text="Find", command=self.find_student)
        find_button.grid(row=0,column=2)
        submit_button = tk.Button(self, text="Submit", command=self.submit_grades).grid(row=13, column=0)
        tk.Button(self, text="Back to Main Menu", command= lambda: controller.show_frame(ClassPage)).grid(row=14, column=1)

    def find_student(self):

        sql = "select student_ID from student where last_name = %s"
        adr = (self.last_name.get(),)

        cursor.execute(sql, adr)
        students = cursor.fetchall()
        for student in students:
            student_ID = student[0]

        ## throw warning if student does not exist
        if len(students) == 0:
            messagebox.showwarning("No Entry Found", "Student entered does not exist in the system!")
            self.last_name.set("")

        ## get all assignments in the course
        cursor.execute('''select gradebook.assignment from gradebook where
                                            gradebook.student_ID = %s and gradebook.course_ID = 3''', (student_ID,))
        assignment_list = cursor.fetchall()
        

        i=0
        row=6
        column=0
        for assignment in assignment_list:
            if assignment == "":
                break
            
            tk.Label(self, text=assignment[0]).grid(row=(row + i), column=column)
            tk.Entry(self, textvariable=eval(f'self.grade{i}'), width=5).grid(row=(row + i), column=1)

            i+=1

        ## define button for clearing all fields
        tk.Button(self, text="Clear", command=self.clear, width=20).grid(row=13, column=1)

    def clear(self):
        for label in self.grid_slaves():
            if int(label.grid_info()["row"]) > 2:
                label.grid_forget()

        self.last_name.set("")

        tk.Button(self, text="Submit", command=self.submit_grades).grid(row=13, column=0)


    def submit_grades(self):

        cursor.execute("select student_ID from student where last_name = %s", (self.last_name.get(),))
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
        for grade in self.grades:
            cursor.execute('''update gradebook set score = %s where
                                assignment = %s and student_ID = %s and course_ID = 3''', (grade.get(), eval(f'assignment{i}[0]'), student_ID))
            mydb.commit()
            i+=1
        messagebox.showinfo("Success", "Student grades have been entered.")

class EnterGrades_Music100(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="MUSIC 100")
        #label.pack(pady=10, padx=10)

        # set entry variables
        self.last_name = tk.StringVar()

        # label to enter name
        tk.Label(self, text="Student Last Name").grid(row=0, column=0)

        # labels for subject codes
        tk.Label(self, text="Subject").grid(row=1, column=0)

        tk.Label(self, text="Grade").grid(row=1, column=1)
        self.grade0 = tk.IntVar()
        self.grade1 = tk.IntVar()
        self.grade2 = tk.IntVar()
        self.grade3 = tk.IntVar()
        self.grades = [self.grade0, self.grade1, self.grade2, self.grade3]

        # Name age roll entries
        e1=tk.Entry(self , textvariable=self.last_name)

        # organizing them in the grid
        e1.grid(row=0, column=1)

        # button to display all the calculated credit scores and sgpa
        find_button = tk.Button(self, text="Find", command=self.find_student)
        find_button.grid(row=0,column=2)
        submit_button = tk.Button(self, text="Submit", command=self.submit_grades).grid(row=13, column=0)
        tk.Button(self, text="Back to Main Menu", command= lambda: controller.show_frame(ClassPage)).grid(row=14, column=1)

    def find_student(self):

        sql = "select student_ID from student where last_name = %s"
        adr = (self.last_name.get(),)

        cursor.execute(sql, adr)
        students = cursor.fetchall()
        for student in students:
            student_ID = student[0]

        ## throw warning if student does not exist
        if len(students) == 0:
            messagebox.showwarning("No Entry Found", "Student entered does not exist in the system!")
            self.last_name.set("")

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
            
            tk.Label(self, text=assignment[0]).grid(row=(row + i), column=column)
            tk.Entry(self, textvariable=eval(f'self.grade{i}'), width=5).grid(row=(row + i), column=1)

            i+=1

        ## define button for clearing all fields
        tk.Button(self, text="Clear", command=self.clear, width=20).grid(row=13, column=1)

    def clear(self):
        for label in self.grid_slaves():
            if int(label.grid_info()["row"]) > 2:
                label.grid_forget()

        self.last_name.set("")

        tk.Button(self, text="Submit", command=self.submit_grades).grid(row=13, column=0)


    def submit_grades(self):

        cursor.execute("select student_ID from student where last_name = %s", (self.last_name.get(),))
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
        for grade in self.grades:
            cursor.execute('''update gradebook set score = %s where
                                assignment = %s and student_ID = %s and course_ID = 4''', (grade.get(), eval(f'assignment{i}[0]'), student_ID))
            mydb.commit()
            i+=1
        messagebox.showinfo("Success", "Student grades have been entered.")

class EnterGrades_Physics101(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="PHYSICS 101")
        #label.pack(pady=10, padx=10)

        # set entry variables
        self.last_name = tk.StringVar()

        # label to enter name
        tk.Label(self, text="Student Last Name").grid(row=0, column=0)

        # labels for subject codes
        tk.Label(self, text="Subject").grid(row=1, column=0)

        tk.Label(self, text="Grade").grid(row=1, column=1)
        self.grade0 = tk.IntVar()
        self.grade1 = tk.IntVar()
        self.grade2 = tk.IntVar()
        self.grade3 = tk.IntVar()
        self.grades = [self.grade0, self.grade1, self.grade2, self.grade3]

        # Name age roll entries
        e1=tk.Entry(self , textvariable=self.last_name)

        # organizing them in the grid
        e1.grid(row=0, column=1)

        # button to display all the calculated credit scores and sgpa
        find_button = tk.Button(self, text="Find", command=self.find_student)
        find_button.grid(row=0,column=2)
        submit_button = tk.Button(self, text="Submit", command=self.submit_grades).grid(row=13, column=0)
        tk.Button(self, text="Back to Main Menu", command= lambda: controller.show_frame(ClassPage)).grid(row=14, column=1)

    def find_student(self):

        sql = "select student_ID from student where last_name = %s"
        adr = (self.last_name.get(),)

        cursor.execute(sql, adr)
        students = cursor.fetchall()
        for student in students:
            student_ID = student[0]

        ## throw warning if student does not exist
        if len(students) == 0:
            messagebox.showwarning("No Entry Found", "Student entered does not exist in the system!")
            self.last_name.set("")

        ## get all assignments in the course
        cursor.execute('''select gradebook.assignment from gradebook where
                                            gradebook.student_ID = %s and gradebook.course_ID = 1''', (student_ID,))
        assignment_list = cursor.fetchall()
        

        i=0
        row=6
        column=0
        for assignment in assignment_list:
            if assignment == "":
                break
            
            tk.Label(self, text=assignment[0]).grid(row=(row + i), column=column)
            tk.Entry(self, textvariable=eval(f'self.grade{i}'), width=5).grid(row=(row + i), column=1)

            i+=1

        ## define button for clearing all fields
        tk.Button(self, text="Clear", command=self.clear, width=20).grid(row=13, column=1)

    def clear(self):
        for label in self.grid_slaves():
            if int(label.grid_info()["row"]) > 2:
                label.grid_forget()

        self.last_name.set("")

        tk.Button(self, text="Submit", command=self.submit_grades).grid(row=13, column=0)


    def submit_grades(self):

        cursor.execute("select student_ID from student where last_name = %s", (self.last_name.get(),))
        for student in cursor.fetchall():
            student_ID = student[0]

        cursor.execute('''select gradebook.assignment from gradebook where
                                            gradebook.student_ID = %s and gradebook.course_ID = 1''', (student_ID,))
        assignment_list = cursor.fetchall()
        assignment0 = assignment_list[0]
        assignment1 = assignment_list[1]
        assignment2 = assignment_list[2]
        assignment3 = assignment_list[3]

        i = 0
        for grade in self.grades:
            cursor.execute('''update gradebook set score = %s where
                                assignment = %s and student_ID = %s and course_ID = 1''', (grade.get(), eval(f'assignment{i}[0]'), student_ID))
            mydb.commit()
            i+=1
        messagebox.showinfo("Success", "Student grades have been entered.")

class AddStudent_Math150(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="ADD STUDENT")
        #label.pack(padx=10, pady=10)

        ## create all tkinter variables
        self.last_name = tk.StringVar()

        ## create all labels
        tk.Label(self, text="Student Last Name").grid(row=0, column=0)

        ## create all entries
        tk.Entry(self, textvariable=self.last_name).grid(row=0, column=1)

        ## create all buttons
        tk.Button(self, text="Add", command=self.add_student, width=5).grid(row=2, column=0)
        tk.Button(self, text="Back to Main Menu", command= lambda: controller.show_frame(ClassPage)).grid(row=14, column=1)

    def add_student(self):
        ## get the student ID of the last name entered
        cursor.execute("select student_ID from student where last_name = %s", (self.last_name.get(),))
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

        cursor.execute("select student_ID from enrollment where course_ID = 2")
        is_enrolled = cursor.fetchall()
        if len(is_enrolled) == 0:
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
            self.last_name.set("")
        else:
            messagebox.showwarning("Enrolled", "Student is already enrolled in this class!")
            quit()

class AddStudent_English120(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="ADD STUDENT")
        #label.pack(padx=10, pady=10)

        ## create all tkinter variables
        self.last_name = tk.StringVar()

        ## create all labels
        tk.Label(self, text="Student Last Name").grid(row=0, column=0)

        ## create all entries
        tk.Entry(self, textvariable=self.last_name).grid(row=0, column=1)

        ## create all buttons
        tk.Button(self, text="Add", command=self.add_student, width=5).grid(row=2, column=0)
        tk.Button(self, text="Back to Main Menu", command= lambda: controller.show_frame(ClassPage)).grid(row=14, column=1)

    def add_student(self):
        ## get the student ID of the last name entered
        cursor.execute("select student_ID from student where last_name = %s", (self.last_name.get(),))
        student_last = cursor.fetchall()
        for student in student_last:
            student = student[0]
        if len(student_last) == 0:
            messagebox.showwarning("No Entry Found", "Student entered does not exist in the system!")
            quit()

        ## get student count and ensure it is beneath the max amount
        cursor.execute("select student_ID from gradebook where course_ID = 3")
        students = cursor.fetchall()
        if len(students) > max_students:
            messagebox.showwarning("Adding Error", "Max amount of students for this class has been reached!")
            quit()

        cursor.execute("select student_ID from enrollment where course_ID = 3")
        is_enrolled = cursor.fetchall()
        if len(is_enrolled) == 0:
            ## insert the value of student ID into the enrollment table with the appropriate class
            cursor.execute("insert into enrollment values (%s, 3)", (student,))
            mydb.commit()

            ## insert student into gradebook where assignments can be assigned to them and later graded
            sql = "insert into gradebook values (%s, 3, %s, 0, 25)"
            val = [
                (student, 'Group Project 1'),
                (student, 'Group Project 2'),
                (student, 'Group Project 3'),
                (student, 'Group Project 4')
            ]
            cursor.executemany(sql, val)
            mydb.commit()
            messagebox.showinfo("Success", "Student has been added to English 120!")

            ## clear entry field to add more students
            self.last_name.set("")
        else:
            messagebox.showwarning("Enrolled", "Student is already enrolled in this class!")
            quit()

class AddStudent_Music100(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="ADD STUDENT")
        #label.pack(padx=10, pady=10)

        ## create all tkinter variables
        self.last_name = tk.StringVar()

        ## create all labels
        tk.Label(self, text="Student Last Name").grid(row=0, column=0)

        ## create all entries
        tk.Entry(self, textvariable=self.last_name).grid(row=0, column=1)

        ## create all buttons
        tk.Button(self, text="Add", command=self.add_student, width=5).grid(row=2, column=0)
        tk.Button(self, text="Back to Main Menu", command= lambda: controller.show_frame(ClassPage)).grid(row=14, column=1)

    def add_student(self):
        ## get the student ID of the last name entered
        cursor.execute("select student_ID from student where last_name = %s", (self.last_name.get(),))
        student_last = cursor.fetchall()
        for student in student_last:
            student = student[0]
        if len(student_last) == 0:
            messagebox.showwarning("No Entry Found", "Student entered does not exist in the system!")
            quit()

        ## get student count and ensure it is beneath the max amount
        cursor.execute("select student_ID from gradebook where course_ID = 4")
        students = cursor.fetchall()
        if len(students) > max_students:
            messagebox.showwarning("Adding Error", "Max amount of students for this class has been reached!")
            quit()

        cursor.execute("select student_ID from enrollment where course_ID = 4")
        is_enrolled = cursor.fetchall()
        if len(is_enrolled) == 0:
            ## insert the value of student ID into the enrollment table with the appropriate class
            cursor.execute("insert into enrollment values (%s, 4)", (student,))
            mydb.commit()

            ## insert student into gradebook where assignments can be assigned to them and later graded
            sql = "insert into gradebook values (%s, 4, %s, 0, 25)"
            val = [
                (student, 'Project 1'),
                (student, 'Project 2'),
                (student, 'Project 3'),
                (student, 'Final')
            ]
            cursor.executemany(sql, val)
            mydb.commit()
            messagebox.showinfo("Success", "Student has been added to Music 100!")

            ## clear entry field to add more students
            self.last_name.set("")
        else:
            messagebox.showwarning("Enrolled", "Student is already enrolled in this class!")
            quit()

class AddStudent_Physics101(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="ADD STUDENT")
        #label.pack(padx=10, pady=10)

        ## create all tkinter variables
        self.last_name = tk.StringVar()

        ## create all labels
        tk.Label(self, text="Student Last Name").grid(row=0, column=0)

        ## create all entries
        tk.Entry(self, textvariable=self.last_name).grid(row=0, column=1)

        ## create all buttons
        tk.Button(self, text="Add", command=self.add_student, width=5).grid(row=2, column=0)
        tk.Button(self, text="Back to Main Menu", command= lambda: controller.show_frame(ClassPage)).grid(row=14, column=1)

    def add_student(self):
        ## get the student ID of the last name entered
        cursor.execute("select student_ID from student where last_name = %s", (self.last_name.get(),))
        student_last = cursor.fetchall()
        for student in student_last:
            student = student[0]
        if len(student_last) == 0:
            messagebox.showwarning("No Entry Found", "Student entered does not exist in the system!")
            quit()

        ## get student count and ensure it is beneath the max amount
        cursor.execute("select student_ID from gradebook where course_ID = 1")
        students = cursor.fetchall()
        if len(students) > max_students:
            messagebox.showwarning("Adding Error", "Max amount of students for this class has been reached!")
            quit()

        cursor.execute("select student_ID from enrollment where course_ID = 1")
        is_enrolled = cursor.fetchall()
        if len(is_enrolled) == 0:
            ## insert the value of student ID into the enrollment table with the appropriate class
            cursor.execute("insert into enrollment values (%s, 1)", (student,))
            mydb.commit()

            ## insert student into gradebook where assignments can be assigned to them and later graded
            sql = "insert into gradebook values (%s, 1, %s, 0, 25)"
            val = [
                (student, 'Project 1'),
                (student, 'Project 2'),
                (student, 'Project 3'),
                (student, 'Final')
            ]
            cursor.executemany(sql, val)
            mydb.commit()
            messagebox.showinfo("Success", "Student has been added to Physics 101!")

            ## clear entry field to add more students
            self.last_name.set("")
        else:
            messagebox.showwarning("Enrolled", "Student is already enrolled in this class!")
            quit()

class AddProfessor_Math150(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="ADD PROFESSOR")
        #label.pack(padx=10, pady=10)

        ## create all tkinter variables
        self.last_name = tk.StringVar()

        ## create all labels
        tk.Label(self, text="Professor Last Name").grid(row=0, column=0)

        ## create all entries
        tk.Entry(self, textvariable=self.last_name).grid(row=0, column=1)

        ## create all buttons
        tk.Button(self, text="Add", command=self.add_professor, width=5).grid(row=2, column=0)
        tk.Button(self, text="Back to Main Menu", command= lambda: controller.show_frame(ClassPage)).grid(row=14, column=1)

    def add_professor(self):
        ## get the professor ID of the last name entered
        cursor.execute("select professor_ID from professor where last_name = %s", (self.last_name.get(),))
        prof_last = cursor.fetchall()
        for prof in prof_last:
            prof = prof[0]
        if len(prof_last) == 0:
            messagebox.showwarning("No Entry Found", "Professor entered does not exist in the system!")
            self.last_name.set("")
    
        cursor.execute("select professor_ID from course where name = 'Math 150'")
        course_info = cursor.fetchall()
        print(course_info)

        if len(course_info) > 0:
            messagebox.showwarning("No Entry Found", "Math 150 already has a professor!")
            self.last_name.set("")
        else:
            ## insert the professor id into the course
            cursor.execute("insert into course values (2, 'Math 150', 4, %s)", (prof,))
            mydb.commit()
            messagebox.showinfo("Success", "Professor has been added to Math 150!")

class AddProfessor_English120(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="ADD PROFESSOR")
        #label.pack(padx=10, pady=10)

        ## create all tkinter variables
        self.last_name = tk.StringVar()

        ## create all labels
        tk.Label(self, text="Professor Last Name").grid(row=0, column=0)

        ## create all entries
        tk.Entry(self, textvariable=self.last_name).grid(row=0, column=1)

        ## create all buttons
        tk.Button(self, text="Add", command=self.add_professor, width=5).grid(row=2, column=0)
        tk.Button(self, text="Back to Main Menu", command= lambda: controller.show_frame(ClassPage)).grid(row=14, column=1)

    def add_professor(self):
        ## get the professor ID of the last name entered
        cursor.execute("select professor_ID from professor where last_name = %s", (self.last_name.get(),))
        prof_last = cursor.fetchall()
        for prof in prof_last:
            prof = prof[0]
        if len(prof_last) == 0:
            messagebox.showwarning("No Entry Found", "Professor entered does not exist in the system!")
            self.last_name.set("")
    
        cursor.execute("select professor_ID from course where name = 'English 120'")
        course_info = cursor.fetchall()
        print(course_info)

        if len(course_info) > 0:
            messagebox.showwarning("No Entry Found", "English 120 already has a professor!")
            self.last_name.set("")
        else:
            ## insert the professor id into the course
            cursor.execute("insert into course values (3, 'English 120', 4, %s)", (prof,))
            mydb.commit()
            messagebox.showinfo("Success", "Professor has been added to English 120!")

class AddProfessor_Music100(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="ADD PROFESSOR")
        #label.pack(padx=10, pady=10)

        ## create all tkinter variables
        self.last_name = tk.StringVar()

        ## create all labels
        tk.Label(self, text="Professor Last Name").grid(row=0, column=0)

        ## create all entries
        tk.Entry(self, textvariable=self.last_name).grid(row=0, column=1)

        ## create all buttons
        tk.Button(self, text="Add", command=self.add_professor, width=5).grid(row=2, column=0)
        tk.Button(self, text="Back to Main Menu", command= lambda: controller.show_frame(ClassPage)).grid(row=14, column=1)

    def add_professor(self):
        ## get the professor ID of the last name entered
        cursor.execute("select professor_ID from professor where last_name = %s", (self.last_name.get(),))
        prof_last = cursor.fetchall()
        for prof in prof_last:
            prof = prof[0]
        if len(prof_last) == 0:
            messagebox.showwarning("No Entry Found", "Professor entered does not exist in the system!")
            self.last_name.set("")
    
        cursor.execute("select professor_ID from course where name = 'Music 100'")
        course_info = cursor.fetchall()
        print(course_info)

        if len(course_info) > 0:
            messagebox.showwarning("No Entry Found", "Music 100 already has a professor!")
            self.last_name.set("")
        else:
            ## insert the professor id into the course
            cursor.execute("insert into course values (4, 'Music 100', 4, %s)", (prof,))
            mydb.commit()
            messagebox.showinfo("Success", "Professor has been added to Music 100!")

class AddProfessor_Physics101(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="ADD PROFESSOR")
        #label.pack(padx=10, pady=10)

        ## create all tkinter variables
        self.last_name = tk.StringVar()

        ## create all labels
        tk.Label(self, text="Professor Last Name").grid(row=0, column=0)

        ## create all entries
        tk.Entry(self, textvariable=self.last_name).grid(row=0, column=1)

        ## create all buttons
        tk.Button(self, text="Add", command=self.add_professor, width=5).grid(row=2, column=0)
        tk.Button(self, text="Back to Main Menu", command= lambda: controller.show_frame(ClassPage)).grid(row=14, column=1)

    def add_professor(self):
        ## get the professor ID of the last name entered
        cursor.execute("select professor_ID from professor where last_name = %s", (self.last_name.get(),))
        prof_last = cursor.fetchall()
        for prof in prof_last:
            prof = prof[0]
        if len(prof_last) == 0:
            messagebox.showwarning("No Entry Found", "Professor entered does not exist in the system!")
            self.last_name.set("")
    
        cursor.execute("select professor_ID from course where name = 'Physics 101'")
        course_info = cursor.fetchall()
        print(course_info)

        if len(course_info) > 0:
            messagebox.showwarning("No Entry Found", "Physics 101 already has a professor!")
            self.last_name.set("")
        else:
            ## insert the professor id into the course
            cursor.execute("insert into course values (1, 'Physics 101', 4, %s)", (prof,))
            mydb.commit()
            messagebox.showinfo("Success", "Professor has been added to Physics 101!")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x300")
    root.title('CLASS MANAGEMENT')
    PageContainer(root).pack(side="top", fill="both", expand=True)
    root.mainloop()