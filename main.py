## File that includes all the code written
import tkinter as tk
import mysql.connector
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import customtkinter as ctk
import time

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "ctu1234",
    database = "grades"
)

cursor = mydb.cursor()

class PageContainer(ctk.CTkFrame):

    def __init__(self, root):
        super().__init__(self, root)

        self.container = container = ctk.CTkFrame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frame = {}

        for F in (Example, ReportCard, Math150, English120, Music100, Physics101, ClassPage, EnterGrades_English120, EnterGrades_Math150, EnterGrades_Music100, EnterGrades_Physics101, AddStudent_English120, AddStudent_Math150, AddStudent_Music100, AddStudent_Physics101):
            frame = F(container, self)
            self.frame[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(Example)

    def show_frame(self, controller):
        if controller not in self.frame:
            self.frame[controller] = frame = controller(self.container, self)
            frame.grid(row=0, column=0, sticky="nsew")
        frame = self.frame[controller]
        frame.tkraise()

    def get_page(self, page_class):
        return self.frame[page_class]

class ClassPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        label = ctk.CTkLabel(self, text="CLASS SELECTION")
        label.pack(pady=10, padx=10)

        button1 = ctk.CTkButton(self, text="Math 150", command= lambda: controller.show_frame(Math150))
        button2 = ctk.CTkButton(self, text="English 120", command= lambda: controller.show_frame(English120))
        button3 = ctk.CTkButton(self, text="Music 100", command= lambda: controller.show_frame(Music100))
        button4 = ctk.CTkButton(self, text="Physics 101", command= lambda: controller.show_frame(Physics101))
        button5 = ctk.CTkButton(self, text="Report Cards", command= lambda: controller.show_frame(ReportCard))
        button6 = ctk.CTkButton(self, text="Main Menu", command= lambda: controller.show_frame(Example))

        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()
        button5.pack()
        button6.pack()

class Math150(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(self, parent)
        label = ctk.CTkLabel(self, text="MATH 150 ACTIONS")
        label.pack(padx=10, pady=10)

        button1 = ctk.CTkButton(self, text="Enter Grades", command= lambda: controller.show_frame(EnterGrades_Math150))
        button2 = ctk.CTkButton(self, text="Add Student", command= lambda: controller.show_frame(AddStudent_Math150))
        button3 = ctk.CTkButton(self, text="Add Professor", command= lambda: controller.show_frame(AddProfessor_Math150))
        button4 = ctk.CTkButton(self, text="Back to Class Selection", command= lambda: controller.show_frame(ClassPage))

        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()

class English120(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(self, parent)
        label = ctk.CTkLabel(self, text="ENGLISH 120 ACTIONS")
        label.pack(padx=10, pady=10)

        button1 = ctk.CTkButton(self, text="Enter Grades", command= lambda: controller.show_frame(EnterGrades_English120))
        button2 = ctk.CTkButton(self, text="Add Student", command= lambda: controller.show_frame(AddStudent_English120))
        button3 = ctk.CTkButton(self, text="Add Professor", command= lambda: controller.show_frame(AddProfessor_English120))
        button4 = ctk.CTkButton(self, text="Back to Class Selection", command= lambda: controller.show_frame(ClassPage))

        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()

class Music100(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(self, parent)
        label = ctk.CTkLabel(self, text="MUSIC 100 ACTIONS")
        label.pack(padx=10, pady=10)

        button1 = ctk.CTkButton(self, text="Enter Grades", command= lambda: controller.show_frame(EnterGrades_Music100))
        button2 = ctk.CTkButton(self, text="Add Student", command= lambda: controller.show_frame(AddStudent_Music100))
        button3 = ctk.CTkButton(self, text="Add Professor", command= lambda: controller.show_frame(AddProfessor_Music100))
        button4 = ctk.CTkButton(self, text="Back to Class Selection", command= lambda: controller.show_frame(ClassPage))

        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()

class Physics101(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(self, parent)
        label = ctk.CTkLabel(self, text="PHYSICS 101 ACTIONS")
        label.pack(padx=10, pady=10)

        button1 = ctk.CTkButton(self, text="Enter Grades", command= lambda: controller.show_frame(EnterGrades_Physics101))
        button2 = ctk.CTkButton(self, text="Add Student", command= lambda: controller.show_frame(AddStudent_Physics101))
        button3 = ctk.CTkButton(self, text="Add Professor", command= lambda: controller.show_frame(AddProfessor_Physics101))
        button4 = ctk.CTkButton(self, text="Back to Class Selection", command= lambda: controller.show_frame(ClassPage))

        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()

class EnterGrades_Math150(ctk.CTkFrame):
    def __init__(self, parent, controller):
        self.controller = controller
        super().__init__(self, parent)
        label = ctk.CTkLabel(self, text="MATH 150")
        #label.pack(pady=10, padx=10)

        # set entry variables
        self.last_name = ctk.StringVar()

        # label to enter name
        ctk.CTkLabel(self, text="Student Last Name").grid(row=0, column=0)

        # labels for subject codes
        ctk.CTkLabel(self, text="Subject").grid(row=1, column=0)

        ctk.CTkLabel(self, text="Grade").grid(row=1, column=1)
        self.grade0 = ctk.IntVar()
        self.grade1 = ctk.IntVar()
        self.grade2 = ctk.IntVar()
        self.grade3 = ctk.IntVar()
        self.grades = [self.grade0, self.grade1, self.grade2, self.grade3]

        # Name age roll entries
        e1 = ctk.CTkEntry(self , textvariable=self.last_name)

        # organizing them in the grid
        e1.grid(row=0, column=1)

        # button to display all the calculated credit scores and sgpa
        find_button = ctk.CTkButton(self, text="Find", command=self.find_student)
        find_button.grid(row=0,column=2)
        submit_button = ctk.CTkButton(self, text="Submit", command=self.submit_grades).grid(row=13, column=0)
        ctk.CTkButton(self, text="Back to Class Selection", command= lambda: controller.show_frame(ClassPage)).grid(row=14, column=1)

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
            tk.Button(self, text="Add Student to Course Here").grid(row=15, column=1)
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
            
            ctk.CTkLabel(self, text=assignment[0]).grid(row=(row + i), column=column)
            ctk.CTkEntry(self, textvariable=eval(f'self.grade{i}'), width=5).grid(row=(row + i), column=1)

            i+=1

        ## define button for clearing all fields
        ctk.CTkButton(self, text="Clear", command=self.clear, width=20).grid(row=13, column=1)

    def clear(self):
        for label in self.grid_slaves():
            if 2 < int(label.grid_info()["row"]) < 13:
                label.grid_forget()

        self.last_name.set("")

        #tk.Button(self, text="Submit", command=self.submit_grades).grid(row=13, column=0)


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

class EnterGrades_English120(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(self, parent)
        label = ctk.CTkLabel(self, text="English 120")
        #label.pack(pady=10, padx=10)

        # set entry variables
        self.last_name = tk.StringVar()

        # label to enter name
        ctk.CTkLabel(self, text="Student Last Name").grid(row=0, column=0)

        # labels for subject codes
        ctk.CTkLabel(self, text="Subject").grid(row=1, column=0)

        tk.Label(self, text="Grade").grid(row=1, column=1)
        self.grade0 = ctk.IntVar()
        self.grade1 = ctk.IntVar()
        self.grade2 = ctk.IntVar()
        self.grade3 = ctk.IntVar()
        self.grades = [self.grade0, self.grade1, self.grade2, self.grade3]

        # Name age roll entries
        e1=ctk.CTkEntry(self , textvariable=self.last_name)

        # organizing them in the grid
        e1.grid(row=0, column=1)

        # button to display all the calculated credit scores and sgpa
        find_button = ctk.CTkButton(self, text="Find", command=self.find_student)
        find_button.grid(row=0,column=2)
        submit_button = ctk.CTkButton(self, text="Submit", command=self.submit_grades).grid(row=13, column=0)
        ctk.CTkButton(self, text="Back to Class Selection", command= lambda: controller.show_frame(ClassPage)).grid(row=14, column=1)

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
        cursor.execute("select student_ID from enrollment where course_ID = 3 and student_ID = %s", (student_ID,))
        is_enrolled = cursor.fetchall()
        if len(is_enrolled) == 0:
            messagebox.showwarning("Not Enrolled", "Student is not enrolled in this class!")
            self.last_name.set("")
            tk.Button(self, text="Add Student to Course Here").grid(row=15, column=1)

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
            
            ctk.CTkLabel(self, text=assignment[0]).grid(row=(row + i), column=column)
            ctk.CTkEntry(self, textvariable=eval(f'self.grade{i}'), width=5).grid(row=(row + i), column=1)

            i+=1

        ## define button for clearing all fields
        ctk.CTkButton(self, text="Clear", command=self.clear, width=20).grid(row=13, column=1)

    def clear(self):
        for label in self.grid_slaves():
            if 2 < int(label.grid_info()["row"]) < 13:
                label.grid_forget()

        self.last_name.set("")

        #ctk.CTkButton(self, text="Submit", command=self.submit_grades).grid(row=13, column=0)


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

class EnterGrades_Music100(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(self, parent)
        label = ctk.CTkLabel(self, text="MUSIC 100")
        #label.pack(pady=10, padx=10)

        # set entry variables
        self.last_name = ctk.StringVar()

        # label to enter name
        ctk.CTkLabel(self, text="Student Last Name").grid(row=0, column=0)

        # labels for subject codes
        ctk.CTkLabel(self, text="Subject").grid(row=1, column=0)

        ctk.CTkLabel(self, text="Grade").grid(row=1, column=1)
        self.grade0 = ctk.IntVar()
        self.grade1 = ctk.IntVar()
        self.grade2 = ctk.IntVar()
        self.grade3 = ctk.IntVar()
        self.grades = [self.grade0, self.grade1, self.grade2, self.grade3]

        # Name age roll entries
        e1=ctk.CTkEntry(self , textvariable=self.last_name)

        # organizing them in the grid
        e1.grid(row=0, column=1)

        # button to display all the calculated credit scores and sgpa
        find_button = ctk.CTkButton(self, text="Find", command=self.find_student)
        find_button.grid(row=0,column=2)
        submit_button = ctk.CTkButton(self, text="Submit", command=self.submit_grades).grid(row=13, column=0)
        ctk.CTkButton(self, text="Back to Class Selection", command= lambda: controller.show_frame(ClassPage)).grid(row=14, column=1)

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
        cursor.execute("select student_ID from enrollment where course_ID = 4 and student_ID = %s", (student_ID,))
        is_enrolled = cursor.fetchall()
        if len(is_enrolled) == 0:
            messagebox.showwarning("Not Enrolled", "Student is not enrolled in this class!")
            self.last_name.set("")
            ctk.CTkButton(self, text="Add Student to Course Here").grid(row=15, column=1)

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
            
            ctk.CTkLabel(self, text=assignment[0]).grid(row=(row + i), column=column)
            ctk.CTkEntry(self, textvariable=eval(f'self.grade{i}'), width=5).grid(row=(row + i), column=1)

            i+=1

        ## define button for clearing all fields
        ctk.CTkButton(self, text="Clear", command=self.clear, width=20).grid(row=13, column=1)

    def clear(self):
        for label in self.grid_slaves():
            if 2 < int(label.grid_info()["row"]) < 13:
                label.grid_forget()

        self.last_name.set("")

        #tk.Button(self, text="Submit", command=self.submit_grades).grid(row=13, column=0)


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

class EnterGrades_Physics101(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(self, parent)
        label = ctk.CTkLabel(self, text="PHYSICS 101")
        #label.pack(pady=10, padx=10)

        # set entry variables
        self.last_name = ctk.StringVar()

        # label to enter name
        ctk.CTkLabel(self, text="Student Last Name").grid(row=0, column=0)

        # labels for subject codes
        ctk.CTkLabel(self, text="Subject").grid(row=1, column=0)

        ctk.CTkLabel(self, text="Grade").grid(row=1, column=1)
        self.grade0 = ctk.IntVar()
        self.grade1 = ctk.IntVar()
        self.grade2 = ctk.IntVar()
        self.grade3 = ctk.IntVar()
        self.grades = [self.grade0, self.grade1, self.grade2, self.grade3]

        # Name age roll entries
        e1=ctk.CTkEntry(self , textvariable=self.last_name)

        # organizing them in the grid
        e1.grid(row=0, column=1)

        # button to display all the calculated credit scores and sgpa
        find_button = ctk.CTkButton(self, text="Find", command=self.find_student)
        find_button.grid(row=0,column=2)
        submit_button = ctk.CTkButton(self, text="Submit", command=self.submit_grades).grid(row=13, column=0)
        ctk.CTkButton(self, text="Back to Class Selection", command= lambda: controller.show_frame(ClassPage)).grid(row=14, column=1)

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
        cursor.execute("select student_ID from enrollment where course_ID = 1 and student_ID = %s", (student_ID,))
        is_enrolled = cursor.fetchall()
        if len(is_enrolled) == 0:
            messagebox.showwarning("Not Enrolled", "Student is not enrolled in this class!")
            self.last_name.set("")
            tk.Button(self, text="Add Student to Course Here").grid(row=15, column=1)

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
            
            ctk.CTkLabel(self, text=assignment[0]).grid(row=(row + i), column=column)
            ctk.CTkEntry(self, textvariable=eval(f'self.grade{i}'), width=5).grid(row=(row + i), column=1)

            i+=1

        ## define button for clearing all fields
        ctk.CTkButton(self, text="Clear", command=self.clear, width=20).grid(row=13, column=1)

    def clear(self):
        for label in self.grid_slaves():
            if 2 < int(label.grid_info()["row"]) < 13:
                label.grid_forget()

        self.last_name.set("")

        #tk.Button(self, text="Submit", command=self.submit_grades).grid(row=13, column=0)


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

class AddStudent_Math150(ctk.CTkFrame):
    def __init__(self, parent, controller):
        self.max_students = 1

        super().__init__(self, parent)
        label = ctk.CTkLabel(self, text="ADD STUDENT")
        #label.pack(padx=10, pady=10)

        ## create all tkinter variables
        self.last_name = ctk.StringVar()

        ## create all labels
        ctk.CTkLabel(self, text="Student Last Name").grid(row=0, column=0)

        ## create all entries
        ctk.CTkEntry(self, textvariable=self.last_name).grid(row=0, column=1)

        ## create all buttons
        ctk.CTkButton(self, text="Add", command=self.add_student, width=5).grid(row=2, column=0)
        ctk.CTkButton(self, text="Back to Class Selection", command= lambda: controller.show_frame(ClassPage)).grid(row=14, column=1)

    def add_student(self):
        ## get the student ID of the last name entered
        cursor.execute("select student_ID from student where last_name = %s", (self.last_name.get(),))
        student_last = cursor.fetchall()
        for student in student_last:
            student = student[0]
        if len(student_last) == 0:
            messagebox.showwarning("No Entry Found", "Student entered does not exist in the system!")
            self.last_name.set("")

        cursor.execute("select student_ID from enrollment where course_ID = 2 and student_ID = %s", (student,))
        is_enrolled = cursor.fetchall()
        if len(is_enrolled) == 0:
            ## get student count and ensure it is beneath the max amount
            cursor.execute("select student_ID from gradebook where course_ID = 2")
            students = cursor.fetchall()
            if len(students) > self.max_students:
                messagebox.showwarning("Adding Error", "Max amount of students for this class has been reached!")
                self.last_name.set("")
            else:
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
            self.last_name.set("")

class AddStudent_English120(ctk.CTkFrame):
    def __init__(self, parent, controller):
        self.max_students = 20

        super().__init__(self, parent)
        label = ctk.CTkLabel(self, text="ADD STUDENT")
        #label.pack(padx=10, pady=10)

        ## create all tkinter variables
        self.last_name = ctk.StringVar()

        ## create all labels
        ctk.CTkLabel(self, text="Student Last Name").grid(row=0, column=0)

        ## create all entries
        ctk.CTkEntry(self, textvariable=self.last_name).grid(row=0, column=1)

        ## create all buttons
        ctk.CTkButton(self, text="Add", command=self.add_student, width=5).grid(row=2, column=0)
        ctk.CTkButton(self, text="Back to Class Selection", command= lambda: controller.show_frame(ClassPage)).grid(row=14, column=1)

    def add_student(self):
        ## get the student ID of the last name entered
        cursor.execute("select student_ID from student where last_name = %s", (self.last_name.get(),))
        student_last = cursor.fetchall()
        for student in student_last:
            student = student[0]
        if len(student_last) == 0:
            messagebox.showwarning("No Entry Found", "Student entered does not exist in the system!")
            self.last_name.set("")

        cursor.execute("select student_ID from enrollment where course_ID = 3 and student_ID = %s", (student,))
        is_enrolled = cursor.fetchall()
        if len(is_enrolled) == 0:
            ## get student count and ensure it is beneath the max amount
            cursor.execute("select student_ID from gradebook where course_ID = 3")
            students = cursor.fetchall()
            if len(students) > self.max_students:
                messagebox.showwarning("Adding Error", "Max amount of students for this class has been reached!")
                self.last_name.set("")
            else:
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
            self.last_name.set("")

class AddStudent_Music100(ctk.CTkFrame):
    def __init__(self, parent, controller):
        self.max_students = 20

        super().__init__(self, parent)
        label = ctk.CTkLabel(self, text="ADD STUDENT")
        #label.pack(padx=10, pady=10)

        ## create all tkinter variables
        self.last_name = ctk.StringVar()

        ## create all labels
        ctk.CTkLabel(self, text="Student Last Name").grid(row=0, column=0)

        ## create all entries
        ctk.CTkEntry(self, textvariable=self.last_name).grid(row=0, column=1)

        ## create all buttons
        ctk.CTkButton(self, text="Add", command=self.add_student, width=5).grid(row=2, column=0)
        ctk.CTkButton(self, text="Back to Class Selection", command= lambda: controller.show_frame(ClassPage)).grid(row=14, column=1)

    def add_student(self):
        ## get the student ID of the last name entered
        cursor.execute("select student_ID from student where last_name = %s", (self.last_name.get(),))
        student_last = cursor.fetchall()
        for student in student_last:
            student = student[0]
        if len(student_last) == 0:
            messagebox.showwarning("No Entry Found", "Student entered does not exist in the system!")
            self.last_name.set("")

        cursor.execute("select student_ID from enrollment where course_ID = 4 and student_ID = %s", (student,))
        is_enrolled = cursor.fetchall()
        if len(is_enrolled) == 0:
            ## get student count and ensure it is beneath the max amount
            cursor.execute("select student_ID from gradebook where course_ID = 4")
            students = cursor.fetchall()
            if len(students) > self.max_students:
                messagebox.showwarning("Adding Error", "Max amount of students for this class has been reached!")
                self.last_name.set("")
            else:
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
            self.last_name.set("")

class AddStudent_Physics101(ctk.CTkFrame):
    def __init__(self, parent, controller):
        self.max_students = 20

        super().__init__(self, parent)
        label = ctk.CTkLabel(self, text="ADD STUDENT")
        #label.pack(padx=10, pady=10)

        ## create all tkinter variables
        self.last_name = ctk.StringVar()

        ## create all labels
        ctk.CTkLabel(self, text="Student Last Name").grid(row=0, column=0)

        ## create all entries
        ctk.CTkEntry(self, textvariable=self.last_name).grid(row=0, column=1)

        ## create all buttons
        ctk.CTkButton(self, text="Add", command=self.add_student, width=5).grid(row=2, column=0)
        ctk.CTkButton(self, text="Back to Class Selection", command= lambda: controller.show_frame(ClassPage)).grid(row=14, column=1)

    def add_student(self):
        ## get the student ID of the last name entered
        cursor.execute("select student_ID from student where last_name = %s", (self.last_name.get(),))
        student_last = cursor.fetchall()
        for student in student_last:
            student = student[0]
        if len(student_last) == 0:
            messagebox.showwarning("No Entry Found", "Student entered does not exist in the system!")
            self.last_name.set("")

        cursor.execute("select student_ID from enrollment where course_ID = 1 and student_ID = %s", (student,))
        is_enrolled = cursor.fetchall()
        if len(is_enrolled) == 0:
            ## get student count and ensure it is beneath the max amount
            cursor.execute("select student_ID from gradebook where course_ID = 1")
            students = cursor.fetchall()
            if len(students) > self.max_students:
                messagebox.showwarning("Adding Error", "Max amount of students for this class has been reached!")
                self.last_name.set("")
            else:
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
            self.last_name.set("")

class AddProfessor_Math150(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(self, parent)
        label = tk.Label(self, text="ADD PROFESSOR")
        #label.pack(padx=10, pady=10)

        ## create all tkinter variables
        self.last_name = ctk.StringVar()

        ## create all labels
        ctk.CTkLabel(self, text="Professor Last Name").grid(row=0, column=0)

        ## create all entries
        ctk.CTkEntry(self, textvariable=self.last_name).grid(row=0, column=1)

        ## create all buttons
        ctk.CTkButton(self, text="Add", command=self.add_professor, width=5).grid(row=2, column=0)
        ctk.CTkButton(self, text="Back to Class Selection", command= lambda: controller.show_frame(ClassPage)).grid(row=14, column=1)

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

        if len(course_info) > 0:
            messagebox.showwarning("No Entry Found", "Math 150 already has a professor!")
            self.last_name.set("")
        else:
            ## insert the professor id into the course
            #cursor.execute("insert into course values (2, 'Math 150', 4, %s)", (prof,))
            cursor.execute("update course set professor_ID = %s where course_ID = 2", (prof,))
            mydb.commit()
            messagebox.showinfo("Success", "Professor has been added to Math 150!")
            self.last_name.set("")

class AddProfessor_English120(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(self, parent)
        label = ctk.CTkLabel(self, text="ADD PROFESSOR")
        #label.pack(padx=10, pady=10)

        ## create all tkinter variables
        self.last_name = ctk.StringVar()

        ## create all labels
        ctk.CTkLabel(self, text="Professor Last Name").grid(row=0, column=0)

        ## create all entries
        ctk.CTkEntry(self, textvariable=self.last_name).grid(row=0, column=1)

        ## create all buttons
        ctk.CTkButton(self, text="Add", command=self.add_professor, width=5).grid(row=2, column=0)
        ctk.CTkButton(self, text="Back to Class Selection", command= lambda: controller.show_frame(ClassPage)).grid(row=14, column=1)

    def add_professor(self):
        ## get the professor ID of the last name entered
        cursor.execute("select professor_ID from professor where last_name = %s", (self.last_name.get(),))
        prof_last = cursor.fetchall()
        for prof in prof_last:
            prof = prof[0]
        if len(prof_last) == 0:
            messagebox.showwarning("No Entry Found", "Professor entered does not exist in the system!")
            self.last_name.set("")
    
        cursor.execute("select professor_ID from course where name = 'English 120' and professor_ID != NULL")
        course_info = cursor.fetchall()

        if len(course_info) > 0:
            messagebox.showwarning("No Entry Found", "English 120 already has a professor!")
            self.last_name.set("")
        else:
            ## insert the professor id into the course
            #cursor.execute("insert into course values (3, 'English 120', 4, %s)", (prof,))
            cursor.execute("update course set professor_ID = %s where course_ID = 3", (prof,))
            mydb.commit()
            messagebox.showinfo("Success", "Professor has been added to English 120!")
            self.last_name.set("")

class AddProfessor_Music100(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(self, parent)
        label = ctk.CTkLabel(self, text="ADD PROFESSOR")
        #label.pack(padx=10, pady=10)

        ## create all tkinter variables
        self.last_name = ctk.StringVar()

        ## create all labels
        ctk.CTkLabel(self, text="Professor Last Name").grid(row=0, column=0)

        ## create all entries
        ctk.CTkEntry(self, textvariable=self.last_name).grid(row=0, column=1)

        ## create all buttons
        ctk.CTkButton(self, text="Add", command=self.add_professor, width=5).grid(row=2, column=0)
        ctk.CTkButton(self, text="Back to Class Selection", command= lambda: controller.show_frame(ClassPage)).grid(row=14, column=1)

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

        if len(course_info) > 0:
            messagebox.showwarning("No Entry Found", "Music 100 already has a professor!")
            self.last_name.set("")
        else:
            ## insert the professor id into the course
            #cursor.execute("insert into course values (4, 'Music 100', 4, %s)", (prof,))
            cursor.execute("update course set professor_ID = %s where course_ID = 4", (prof,))
            mydb.commit()
            messagebox.showinfo("Success", "Professor has been added to Music 100!")
            self.last_name.set("")

class AddProfessor_Physics101(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(self, parent)
        label = tk.Label(self, text="ADD PROFESSOR")
        #label.pack(padx=10, pady=10)

        ## create all tkinter variables
        self.last_name = ctk.StringVar()

        ## create all labels
        ctk.CTkLabel(self, text="Professor Last Name").grid(row=0, column=0)

        ## create all entries
        ctk.CTkEntry(self, textvariable=self.last_name).grid(row=0, column=1)

        ## create all buttons
        ctk.CTkButton(self, text="Add", command=self.add_professor, width=5).grid(row=2, column=0)
        ctk.CTkButton(self, text="Back to Class Selection", command= lambda: controller.show_frame(ClassPage)).grid(row=14, column=1)

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

        if len(course_info) > 0:
            messagebox.showwarning("No Entry Found", "Physics 101 already has a professor!")
            self.last_name.set("")
        else:
            ## insert the professor id into the course
            #cursor.execute("insert into course values (1, 'Physics 101', 4, %s)", (prof,))
            cursor.execute("update course set professor_ID = %s where course_ID = 1", (prof,))
            mydb.commit()
            messagebox.showinfo("Success", "Professor has been added to Physics 101!")
            self.last_name.set("")

class ReportCard(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(self, parent, controller)
        # set entry variables
        self.last_name = ctk.StringVar()
        # label to enter name
        ctk.CTkLabel(self, text="Name").grid(row=0, column=0)
        # labels for subject codes
        ctk.CTkLabel(self, text="Subject").grid(row=5, column=1)
        # label for grades
        ctk.CTkLabel(self, text="Grade").grid(row=5, column=2)
        # labels for subject credits
        ctk.CTkLabel(self, text="Sub Credit").grid(row=5, column=4)
        # label for course management
        ctk.CTkLabel(self, text="Manage Course").grid(row=5, column=0)
        # Name age roll entries
        e1=ctk.CTkEntry(self, textvariable=self.last_name)
        # organizing them in the grid
        e1.grid(row=0, column=1)
        # button to display all the calculated credit scores and sgpa
        find_button = ctk.CTkButton(self, text="Find", command=self.find_student)
        find_button.grid(row=0,column=2)
        ctk.CTkButton(self, text="Back to Class Selection", command= lambda: controller.show_frame(ClassPage)).grid(row=13, column=3)

        ctk.CTkLabel(self, text="Total credits").grid(row=11, column=3)
        ctk.CTkLabel(self, text="Student GPA").grid(row=12, column=3)

    def find_student(self):

        total_creds = []
        total_gpa = []
        # gets last name entered in "Name" field
        sql = "select student_ID from student where last_name = %s"
        adr = (self.last_name.get(),)
        
        cursor.execute(sql, adr)
        students = cursor.fetchall()
        for student in students:
            student_ID = student[0]

        if len(students) == 0:
            messagebox.showwarning("No Entry Found", "Student entered does not exist in the system!")
            self.last_name.set("")

        # gets all courses that student is in
        cursor.execute('''select c.course_ID from course c, enrollment e where
                                e.student_ID = %s and e.course_ID = c.course_ID
                                order by name asc''', (student_ID,))
        course_list = cursor.fetchall()

        i=0
        row=6
        column=1
        for course_ID in course_list:
            if course_ID == "":
                break

            cursor.execute("select name from course where course_ID = %s", course_ID)
            course_name = cursor.fetchone()
            
            ctk.CTkLabel(self, text=course_name[0]).grid(row=(row + i), column=column)

            cursor.execute('''select score, weight from gradebook 
                                    where student_ID = %s and course_ID = %s
                                    ''', (student_ID, course_ID[0]))
            allgrades = cursor.fetchall()
            
            final_grade = 0
            creds_earned = 0
            for grade in allgrades:
                final_grade += grade[0] * grade[1]

            final_grade = final_grade / 100

            if final_grade >= 90:
                creds_earned += 4
            if 80 <= final_grade <= 89.9:
                creds_earned += 3
            if 70 <= final_grade <= 79.9:
                creds_earned += 2
            if 60 <= final_grade <= 69.9:
                creds_earned += 1
            else:
                creds_earned += 0

            gpa = creds_earned / len(course_list)
            total_gpa.append(gpa)

            ctk.CTkLabel(self, text=final_grade).grid(row=(row + i), column=(column + 1))

            ## get credit count for each course
            cursor.execute("select creds from course where course_ID = %s", course_ID)
            credit_count = cursor.fetchall()
            for creds in credit_count:
                ctk.CTkLabel(self, text=creds).grid(row=(row + i), column=4)
                total_creds.append(creds)

            ## go to button next to each class
            ## ability to manage students from there
            button_command = eval(course_name[0].replace(' ',''))
            ctk.CTkButton(self, text=course_name[0], command=button_command).grid(row=(row + i), column=0)

            i+=1
        
        ## get amount of earned creds from student
        total = 0
        for cred in total_creds:
            total += cred[0]
            
        ctk.CTkLabel(self, text=total).grid(row=11,column=4)

        ## calculate student GPA
        total_student_gpa = 0
        for gpa in total_gpa:
            total_student_gpa += gpa

        ctk.CTkLabel(self, text=total_student_gpa).grid(row=12, column=4)
    
        ## define button for clearing all fields
        ctk.CTkButton(self, text="Clear", command=self.clear, width=20).grid(row=13, column=1)


    def clear(self):
        for label in self.grid_slaves():
            if 3 < int(label.grid_info()["row"]) < 13:
                label.grid_forget()
        self.last_name.set("")        

        # label to enter name
        ctk.CTkLabel(self, text="Name").grid(row=0, column=0)

        # labels for subject codes
        ctk.CTkLabel(self, text="Subject").grid(row=5, column=1)

        # label for grades
        ctk.CTkLabel(self, text="Grade").grid(row=5, column=2)

        # labels for subject credits
        ctk.CTkLabel(self, text="Sub Credit").grid(row=5, column=4)

        # label for course management
        ctk.CTkLabel(self, text="Manage Course").grid(row=5, column=0)
    
        ctk.CTkLabel(self, text="Total credits").grid(row=11, column=3)
        ctk.CTkLabel(self, text="Student GPA").grid(row=12, column=3)                
                
#####################
#From FirstProject.py
#####################
class Example(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(self, parent, controller)

        #This is the first window you see and has the 3 buttons for navigating to other windows
        b1 = ctk.CTkButton(self, text="Manage Students", command = self.studentWindow)
        b1.pack(side="left",anchor='n', padx=40, pady=10)

        b2 = ctk.CTkButton(self, text="Manage Teachers", command = self.teacherWindow)
        b2.pack(side="left",anchor='n', padx=40, pady=10)

        #lambda: controller.show_frame(ClassPage)
        b3 = ctk.CTkButton(self, text="Course Management", command = lambda: controller.show_frame(ClassPage))
        b3.pack(side="left",anchor='n', padx=40, pady=10)
        
        studenttitle = ctk.CTkLabel(self, width=30, text="School Force", fg="DarkBlue", font=("times new roman", 15, "bold"))
        studenttitle.pack(side="top",anchor='w', padx=40, pady=10)

        studenttitle = ctk.CTkLabel(self, width=30, text="Ranz Release 4.2.1", fg="black", font=("times new roman", 8, "bold"))
        studenttitle.pack(side="bottom",anchor='w', padx=40, pady=10)
        
        root.lift()
        self.splashwindow()
        
    def splashwindow(self):
        window = ctk.CTkToplevel(self)
        window.attributes("-topmost", True)
        window.geometry("%dx%d%+d%+d" % (520, 350, 10, 10))
        window.title('Loading')
        #This is the image in the students window
        img = Image.open('intro.jpg')
        self.tkimage = ImageTk.PhotoImage(img)
        ctk.CTkLabel(window,image = self.tkimage).place(x=0, y=0)
        
        window.after(5000,lambda:window.destroy())
      
    def studentWindow(self):
        window = ctk.CTkToplevel(self)

        #Window Title
        studenttitle = ctk.CTkLabel(window, width=18, text="Manage Students", fg="black", font=("times new roman", 15, "bold"))
        studenttitle.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        #Creating a frame. This frame holds all the information for writing student data to the database. This frame holds buttons and entry boxes. Move this frame around and everything inside will follow
        Student_write_Frame = ctk.CTkFrame(window, bd=4, relief=RIDGE, bg="LightGrey")
        Student_write_Frame.place(x=50, y=45, width=550, height=200)
        
        #Setting the main window size
        window.geometry("%dx%d%+d%+d" % (1350, 550, 10, 10))
        window.grid_columnconfigure((0,1), weight=1)

        #Creating variables used in this window
        self.studentID_var = ctk.IntVar()
        self.studentFirstName_var = ctk.StringVar()
        self.studentLastName_var = ctk.StringVar()
        self.studentAge_var = ctk.IntVar()
        self.studentGradeLevel_var = ctk.IntVar()
        self.studentSearchID_var = ctk.StringVar()
        self.studentSearchName_var = ctk.StringVar()

        #This is creating labels
        #Student_Label_1 = tk.Label(Student_write_Frame, text="Student ID", bg="LightGrey", bd=5)
        #Student_Label_1.grid(row=1, column=0)
        Student_Label_2 = ctk.CTkLabel(Student_write_Frame, text="Student First Name", bg="LightGrey", bd=5)
        Student_Label_2.grid(row=2, column=0)
        Student_Label_3 = ctk.CTkLabel(Student_write_Frame, text="Student Last Name", bg="LightGrey", bd=5)
        Student_Label_3.grid(row=3, column=0)
        Student_Label_4 = ctk.CTkLabel(Student_write_Frame, text="Age", bg="LightGrey", bd=5)
        Student_Label_4.grid(row=4, column=0)
        Student_Label_5 = ctk.CTkLabel(Student_write_Frame, text="Grade Level", bg="LightGrey", bd=5)
        Student_Label_5.grid(row=5, column=0)

        #This is creating labels and tying their input into variables
        #Student_Entry_1 = tk.Entry(Student_write_Frame, textvariable = self.studentID_var)
        #Student_Entry_1.grid(row=1, column=4)
        Student_Entry_2 = ctk.CTkEntry(Student_write_Frame, textvariable = self.studentFirstName_var)
        Student_Entry_2.grid(row=2, column=4)
        Student_Entry_3 = ctk.CTkEntry(Student_write_Frame, textvariable = self.studentLastName_var)
        Student_Entry_3.grid(row=3, column=4)
        Student_Entry_4 = ctk.CTkEntry(Student_write_Frame, textvariable = self.studentAge_var)
        Student_Entry_4.grid(row=4, column=4)
        Student_Entry_5 = ctk.CTkEntry(Student_write_Frame, textvariable = self.studentGradeLevel_var)
        Student_Entry_5.grid(row=5, column=4)

        #This is the button for writing data to a database
        buttons_student_write = ctk.CTkButton(Student_write_Frame, text="Write to Database", command= self.studentwrite)
        buttons_student_write.grid(row=1, column=40, padx=25, pady=5, sticky="w")

        #This is the image in the students window
        img = Image.open('logo.jpg')
        self.tkimage = ImageTk.PhotoImage(img)
        ctk.CTkLabel(window,image = self.tkimage).place(x=750, y=45)

        #Creating a frame. This frame holds all the information for reading student data from the database. This frame holds buttons and entry boxes. Move this frame around and everything inside will follow
        Student_read_Frame = ctk.CTkFrame(window, bd=4, relief=RIDGE, bg="LightGrey")
        Student_read_Frame.place(x=1075, y=250, width=210, height=250)

        #These are the entries and labels for querying students
        Student_Label_6 = ctk.CTkLabel(Student_read_Frame, text="Search By ID", bg="LightGrey", bd=5)
        Student_Label_6.grid(row=1, column=0, padx=5, pady=5)
        Student_Entry_6 = ctk.CTkEntry(Student_read_Frame, textvariable = self.studentSearchID_var)
        Student_Entry_6.grid(row=2, column=0, padx=5, pady=5)
        Student_Label_7 = ctk.CTkLabel(Student_read_Frame, text="Search By Last Name", bg="LightGrey", bd=5)
        Student_Label_7.grid(row=3, column=0, padx=5, pady=5) 
        Student_Entry_7 = ctk.CTkEntry(Student_read_Frame, textvariable = self.studentSearchName_var)
        Student_Entry_7.grid(row=4, column=0, padx=5, pady=5)

        #This is the button for querying student data
        buttons_student_search = ctk.CTkButton(Student_read_Frame, command= self.readdatastudent, text="Search Database")
        buttons_student_search.grid(row=5, column=0, padx=25, pady=25)
        #Creating a frame. This frame holds the tree window. Move this frame around and everything inside will follow  
        Student_tree_Frame = ctk.CTkFrame(window, bd=4, relief=RIDGE, bg="LightGrey")
        Student_tree_Frame.place(x=20, y=250, width=1025, height=250)
        self.studenttree = ttk.Treeview(Student_tree_Frame, columns=("ID", "FirstName","LastName","Age","Year"))
        self.studenttree.grid(row=1, column=0, padx=5, pady=5)
        self.studenttree.heading("ID", text="ID")
        self.studenttree.heading("FirstName", text="First Name")
        self.studenttree.heading("LastName", text=" Last Name")
        self.studenttree.heading("Age", text="Age")
        self.studenttree.heading("Year", text="Year")
        self.studenttree['show']='headings'
        

    def teacherWindow(self):
        window = ctk.CTkToplevel(self)
        window.geometry("%dx%d%+d%+d" % (1500, 600, 10, 10))
        window.grid_columnconfigure((0,1), weight=1)

        #Window Title
        teachertitle = ctk.CTkLabel(window, width=18, text="Manage Teachers", fg="black", font=("times new roman", 15, "bold"))
        teachertitle.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        #Creating a frame. This frame holds all the information for writing student data to the database. This frame holds buttons and entry boxes. Move this frame around and everything inside will follow
        Teacher_write_Frame = ctk.CTkFrame(window, bd=4, relief=RIDGE, bg="LightGrey")
        Teacher_write_Frame.place(x=50, y=45, width=550, height=230)
       

        #Creating variables used in this window
        self.teacherID_var = ctk.StringVar()
        self.teacherFirstName_var = ctk.StringVar()
        self.teacherLastName_var = ctk.StringVar()
        self.teacherAge_var = ctk.StringVar()
        self.teacherQual_var = ctk.StringVar()
        self.teacherStart_var = ctk.StringVar()
        self.teacherSearchID_var = ctk.StringVar()
        self.teacherSearchName_var = ctk.StringVar()

        #This is creating labels
        #Teacher_Label_1 = tk.Label(Teacher_write_Frame, text="Teacher ID", bg="LightGrey", bd=5)
        #Teacher_Label_1.grid(row=1, column=0)
        Teacher_Label_2 = ctk.CTkLabel(Teacher_write_Frame, text="Teacher First Name", bg="LightGrey", bd=5)
        Teacher_Label_2.grid(row=2, column=0)
        Teacher_Label_3 = ctk.CTkLabel(Teacher_write_Frame, text="Teacher Last Name", bg="LightGrey", bd=5)
        Teacher_Label_3.grid(row=3, column=0)
        Teacher_Label_4 = ctk.CTkLabel(Teacher_write_Frame, text="Age", bg="LightGrey", bd=5)
        Teacher_Label_4.grid(row=4, column=0)
        Teacher_Label_5 = ctk.CTkLabel(Teacher_write_Frame, text="Qualifications", bg="LightGrey", bd=5)
        Teacher_Label_5.grid(row=5, column=0)
        Teacher_Label_6 = ctk.CTkLabel(Teacher_write_Frame, text="Start Date", bg="LightGrey", bd=5)
        Teacher_Label_6.grid(row=6, column=0)

        #This is creating labels and tying their input into variables
        #Teacher_Entry_1 = tk.Entry(Teacher_write_Frame, textvariable = self.teacherID_var)
        #Teacher_Entry_1.grid(row=1, column=4)
        Teacher_Entry_2 = ctk.CTkEntry(Teacher_write_Frame, textvariable = self.teacherFirstName_var)
        Teacher_Entry_2.grid(row=2, column=4)
        Teacher_Entry_3 = ctk.CTkEntry(Teacher_write_Frame, textvariable = self.teacherLastName_var)
        Teacher_Entry_3.grid(row=3, column=4)
        Teacher_Entry_4 = ctk.CTkEntry(Teacher_write_Frame, textvariable = self.teacherAge_var)
        Teacher_Entry_4.grid(row=4, column=4)
        Teacher_Entry_5 = ctk.CTkEntry(Teacher_write_Frame, textvariable = self.teacherQual_var)
        Teacher_Entry_5.grid(row=5, column=4)
        Teacher_Entry_6 = ctk.CTkEntry(Teacher_write_Frame, textvariable = self.teacherStart_var)
        Teacher_Entry_6.grid(row=6, column=4)

        #This is the button for writing data to a database
        buttons_teacher_write = ctk.CTkButton(Teacher_write_Frame, text="Write to Database", command= self.teacherwrite)
        buttons_teacher_write.grid(row=1, column=40, padx=25, pady=5, sticky="w")

        #This is the image in the teacher window
        img = Image.open('logo.jpg')
        self.tkimage = ImageTk.PhotoImage(img)
        ctk.Label(window,image = self.tkimage).place(x=850, y=45)

        #Creating a frame. This frame holds all the information for reading student data from the database. This frame holds buttons and entry boxes. Move this frame around and everything inside will follow
        Teacher_read_Frame = ctk.CTkFrame(window, bd=4, relief=RIDGE, bg="LightGrey")
        Teacher_read_Frame.place(x=1275, y=300, width=210, height=250)

        #These are the entries and labels for querying students
        Teacher_Label_7 = ctk.CTkLabel(Teacher_read_Frame, text="Search By ID", bg="LightGrey", bd=5)
        Teacher_Label_7.grid(row=1, column=0, padx=5, pady=5)
        Teacher_Entry_7 = ctk.CTkEntry(Teacher_read_Frame, textvariable = self.teacherSearchID_var)
        Teacher_Entry_7.grid(row=2, column=0, padx=5, pady=5)
        Teacher_Label_8 = ctk.CTkLabel(Teacher_read_Frame, text="Search By Last Name", bg="LightGrey", bd=5)
        Teacher_Label_8.grid(row=3, column=0, padx=5, pady=5) 
        Teacher_Entry_9 = ctk.CTkEntry(Teacher_read_Frame, textvariable = self.teacherSearchName_var)
        Teacher_Entry_9.grid(row=4, column=0, padx=5, pady=5)

        #This is the button for querying student data
        buttons_teacher_search = ctk.CTkButton(Teacher_read_Frame, command= self.readdatateacher, text="Search Database")
        buttons_teacher_search.grid(row=5, column=0, padx=25, pady=25)

        #Creating a frame. This frame holds the tree window. Move this frame around and everything inside will follow  
        Teacher_tree_Frame = Frame(window, bd=4, relief=RIDGE, bg="LightGrey")
        Teacher_tree_Frame.place(x=20, y=300, width=1225, height=250)
        self.teachertree = ttk.Treeview(Teacher_tree_Frame, columns=("ID", "FirstName","LastName","Age","Qual","Start"))
        self.teachertree.grid(row=1, column=0, padx=5, pady=5)
        self.teachertree.heading("ID", text="ID")
        self.teachertree.heading("FirstName", text="First Name")
        self.teachertree.heading("LastName", text=" Last Name")
        self.teachertree.heading("Age", text="Age")
        self.teachertree.heading("Qual", text="Qualifications")
        self.teachertree.heading("Start", text="Start Date")
        self.teachertree['show']='headings'
		

        
    def sectionWindow(self, controller):
        window = ctk.CTkToplevel(self)
        window.geometry("%dx%d%+d%+d" % (1100, 550, 10, 10))
        window.grid_columnconfigure((0,1), weight=1)

        #Window Title
        sectiontitle = ctk.CTkLabel(window, width=18, text="Manage sections", fg="black", font=("times new roman", 15, "bold"))
        sectiontitle.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        #Creating a frame. This frame holds all the information for writing class data to the database. This frame holds buttons and entry boxes. Move this frame around and everything inside will follow
        section_write_Frame = ctk.CTkFrame(window, bd=4, relief=RIDGE, bg="LightGrey")
        section_write_Frame.place(x=50, y=45, width=450, height=150)

        #Creating variables
        self.sectionID_var = ctk.StringVar()
        self.sectionName_var = ctk.StringVar()
        self.sectionCreds_var = ctk.StringVar()
        self.sectionProf_var = ctk.StringVar()
        self.sectionSearchID_var = ctk.StringVar()
        self.sectionSearchName_var = ctk.StringVar()

        #This is creating labels
        section_Label_1 = ctk.CTkLabel(section_write_Frame, text="section ID", bg="LightGrey", bd=5)
        section_Label_1.grid(row=1, column=0)
        section_Label_2 = ctk.CTkLabel(section_write_Frame, text="Section Name", bg="LightGrey", bd=5)
        section_Label_2.grid(row=2, column=0)
        section_Label_3 = ctk.CTkLabel(section_write_Frame, text="Credits", bg="LightGrey", bd=5)
        section_Label_3.grid(row=3, column=0)
        section_Label_4 = ctk.CTkLabel(section_write_Frame, text="Professor", bg="LightGrey", bd=5)
        section_Label_4.grid(row=4, column=0)

        #This is creating labels and tying their input into variables
        section_Entry_1 = ctk.CTkEntry(section_write_Frame, textvariable = self.sectionID_var)
        section_Entry_1.grid(row=1, column=4)
        section_Entry_2 = ctk.CTkEntry(section_write_Frame, textvariable = self.sectionName_var)
        section_Entry_2.grid(row=2, column=4)
        section_Entry_3 = ctk.CTkEntry(section_write_Frame, textvariable = self.sectionCreds_var)
        section_Entry_3.grid(row=3, column=4)
        section_Entry_4 = ctk.CTkEntry(section_write_Frame, textvariable = self.sectionProf_var)
        section_Entry_4.grid(row=4, column=4)


        #This is the button for writing data to a database
        buttons_section_write = ctk.CTkButton(section_write_Frame, text="Write to Database", command= self.sectionwrite)
        buttons_section_write.grid(row=1, column=40, padx=25, pady=5, sticky="w")

        #This is the image in the section window
        img = Image.open('logo.jpg')
        self.tkimage = ImageTk.PhotoImage(img)
        ctk.CTkLabel(window,image = self.tkimage).place(x=650, y=45)

        #Creating a frame. This frame holds all the information for reading class data from the database. This frame holds buttons and entry boxes. Move this frame around and everything inside will follow
        section_read_Frame = ctk.CTkFrame(window, bd=4, relief=RIDGE, bg="LightGrey")
        section_read_Frame.place(x=900, y=250, width=150, height=200)

        #These are the entries and labels for querying classes
        section_Label_7 = ctk.CTkLabel(section_read_Frame, text="Search By ID", bg="LightGrey", bd=5)
        section_Label_7.grid(row=1, column=0, padx=5, pady=5)
        section_Entry_7 = ctk.CTkEntry(section_read_Frame, textvariable = self.sectionSearchID_var)
        section_Entry_7.grid(row=2, column=0, padx=5, pady=5)
        section_Label_8 = ctk.CTkLabel(section_read_Frame, text="Search By Name", bg="LightGrey", bd=5)
        section_Label_8.grid(row=3, column=0, padx=5, pady=5) 
        section_Entry_9 = ctk.CTkEntry(section_read_Frame, textvariable = self.sectionSearchName_var)
        section_Entry_9.grid(row=4, column=0, padx=5, pady=5)

        #This is the button for querying class data
        buttons_section_search = ctk.CTkButton(section_read_Frame, command= self.readdataclass, text="Search Database")
        buttons_section_search.grid(row=5, column=0, padx=25, pady=25)

        #Creating a frame. This frame holds the tree window. Move this frame around and everything inside will follow  
        section_tree_Frame = ctk.CTkFrame(window, bd=4, relief=RIDGE, bg="LightGrey")
        section_tree_Frame.place(x=20, y=250, width=825, height=250)
        self.sectiontree = ttk.Treeview(section_tree_Frame, columns=("ID", "Name","Creds","Prof"))
        self.sectiontree.grid(row=1, column=0, padx=5, pady=5)
        self.sectiontree.heading("ID", text="ID")
        self.sectiontree.heading("Name", text="Name")
        self.sectiontree.heading("Creds", text="Credits")
        self.sectiontree.heading("Prof", text="Professor")
        self.sectiontree['show']='headings'
        
    def sectionwrite(self):
        #con = mysql.connector.connect(host="localhost", user="root", password="ctu1234", database="grades")
        #cur = con.cursor()
        cursor.execute("insert into course values(%s, %s, %s, %s)", (self.sectionID_var.get(), self.sectionName_var.get(), self.sectionCreds_var.get(), self.sectionProf_var.get()))
        mydb.commit()
        messagebox.showinfo("Successfull", "Record has been inserted.")

    def studentwrite(self):
        #con = mysql.connector.connect(host="localhost", user="root", password="ctu1234", database="grades")
        #cur = con.cursor()
        cursor.execute("insert into student (first_name, last_name, age, grade_level) values (%s, %s, %s, %s)", (self.studentFirstName_var.get(), self.studentLastName_var.get(), self.studentAge_var.get(), self.studentGradeLevel_var.get()))
        mydb.commit()
        messagebox.showinfo("Successfull", "Record has been inserted.")
        self.studentFirstName_var.set("")
        self.studentLastName_var.set("")
        self.studentAge_var.set("")
        self.studentGradeLevel_var.set("")

    def teacherwrite(self):
        #con = mysql.connector.connect(host="localhost", user="root", password="ctu1234", database="grades")
        #cur = con.cursor()
        cursor.execute("insert into professor (first_name, last_name, age, qualifications, start_date) values(%s, %s, %s, %s, %s)", (self.teacherFirstName_var.get(), self.teacherLastName_var.get(), self.teacherAge_var.get(), self.teacherQual_var.get(), self.teacherStart_var.get()))
        mydb.commit()
        messagebox.showinfo("Successfull", "Record has been inserted.")
        self.teacherFirstName_var.set("")
        self.teacherLastName_var.set("")
        self.teacherAge_var.set("")
        self.teacherQual_var.set("")
        self.teacherStart_var.set("")

            
    def readdatastudent(self):

        if len(self.studentSearchID_var.get()) == 0:

            #con = mysql.connector.connect(host="localhost", user="root", password="ctu1234", database="grades")
            #cur = con.cursor()
         
            sql = "SELECT * FROM student WHERE last_name = %s"
            adr = self.studentSearchName_var.get()

            val = cursor.execute(sql, (adr,))

            rows = cursor.fetchall()
            if(len(rows)!=0):
                self.studenttree.delete(*self.studenttree.get_children())
                for row in rows:
                    self.studenttree.insert('', END, values=row)

                mydb.commit()
            else:
                messagebox.showinfo("No", "Student is not registered in the database!")
                self.studentSearchName_var.set("")

        elif len(self.studentSearchName_var.get()) == 0:

            #con = mysql.connector.connect(host="localhost", user="root", password="ctu1234", database="grades")
            #cur = con.cursor()
         
            sql = "SELECT * FROM student WHERE student_ID = %s"
            adr = self.studentSearchID_var.get()

            val = cursor.execute(sql, (adr,))

            rows = cursor.fetchall()
            if(len(rows)!=0):
                self.studenttree.delete(*self.studenttree.get_children())
                for row in rows:
                    self.studenttree.insert('', END, values=row)

                mydb.commit()
            else:
                messagebox.showinfo("No", "Student is not registered in the database!")
                self.studentSearchID_var.set("")
        else:
            messagebox.showinfo("Error", "Please use 1 criteria.")
            

    def readdatateacher(self):

        if len(self.teacherSearchID_var.get()) == 0:

            #con = mysql.connector.connect(host="localhost", user="root", password="ctu1234", database="grades")
            #cur = con.cursor()
         
            sql = "SELECT * FROM professor WHERE last_name = %s"
            adr = self.teacherSearchName_var.get()

            val = cursor.execute(sql, (adr,))

            rows = cursor.fetchall()
            if(len(rows)!=0):
                self.teachertree.delete(*self.teachertree.get_children())
                for row in rows:
                    self.teachertree.insert('', END, values=row)

                mydb.commit()
            else:
                messagebox.showinfo("No", "Professor is not registered in the database!")
                self.teacherSearchName_var.set("")

        elif len(self.teacherSearchName_var.get()) == 0:

            #con = mysql.connector.connect(host="localhost", user="root", password="ctu1234", database="grades")
            #cur = con.cursor()
         
            sql = "SELECT * FROM professor WHERE professor_ID = %s"
            adr = self.teacherSearchID_var.get()

            val = cursor.execute(sql, (adr,))

            rows = cursor.fetchall()
            if(len(rows)!=0):
                self.teachertree.delete(*self.teachertree.get_children())
                for row in rows:
                    self.teachertree.insert('', END, values=row)

                mydb.commit()
            else:
                messagebox.showinfo("No", "Professor is not registered in the database!")
                self.teacherSearchID_var.set("")
        else:
            messagebox.showinfo("Error", "Please use 1 criteria.")

    def readdataclass(self):
            
        if len(self.sectionSearchID_var.get()) == 0:

            con = mysql.connector.connect(host="localhost", user="root", password="ctu1234", database="grades")
            cur = con.cursor()
         
            sql = "SELECT * FROM course WHERE name = %s"
            adr = self.sectionSearchName_var.get()

            val = cur.execute(sql, adr)
            if(not val):
                messagebox.showinfo("No", "Not availabe!")

            rows = cur.fetchall()
            if(len(rows)!=0):
                self.sectiontree.delete(*self.sectiontree.get_children())
                for row in rows:
                    self.sectiontree.insert('', END, values=row)

                con.commit()
            con.close()

        elif len(self.sectionSearchName_var.get()) == 0:

            con = mysql.connector.connect(host="localhost", user="root", password="ctu1234", database="grades")
            cur = con.cursor()
         
            sql = "SELECT * FROM course WHERE course_ID = %s"
            adr = self.sectionSearchID_var.get()

            val = cur.execute(sql, adr)
            if(not val):
                messagebox.showinfo("No", "Not availabe!")

            rows = cur.fetchall()
            if(len(rows)!=0):
                self.sectiontree.delete(*self.sectiontree.get_children())
                for row in rows:
                    self.sectiontree.insert('', END, values=row)

                con.commit()
            con.close()
        else:
            messagebox.showinfo("Error", "Please use 1 criteria.")

if __name__ == "__main__":
    root = ctk.CTkTk()
    root.geometry("800x300")
    root.title('STUDENT MANAGEMENT SYSTEM')
    PageContainer(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
