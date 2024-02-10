from tkinter import messagebox
import customtkinter as ctk

from ..views.class_page import ClassPage

class EnterGrades_Physics101(ctk.CTkFrame):
    def __init__(self, parent, controller, mydb, cursor):
        super().__init__(master=parent)
        label = ctk.CTkLabel(self, text="PHYSICS 101")
        #label.pack(pady=10, padx=10)

        self.mydb = mydb
        self.cursor = cursor

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

        self.cursor.execute(sql, adr)
        students = self.cursor.fetchall()
        for student in students:
            student_ID = student[0]

        ## throw warning if student does not exist
        if len(students) == 0:
            messagebox.showwarning("No Entry Found", "Student entered does not exist in the system!")
            self.last_name.set("")

        ## throw warning if student exists but is not enrolled in the class
        self.cursor.execute("select student_ID from enrollment where course_ID = 1 and student_ID = %s", (student_ID,))
        is_enrolled = self.cursor.fetchall()
        if len(is_enrolled) == 0:
            messagebox.showwarning("Not Enrolled", "Student is not enrolled in this class!")
            self.last_name.set("")
            ctk.CTkButton(self, text="Add Student to Course Here").grid(row=15, column=1)

        ## get all assignments in the course
        self.cursor.execute('''select gradebook.assignment from gradebook where
                                            gradebook.student_ID = %s and gradebook.course_ID = 1''', (student_ID,))
        assignment_list = self.cursor.fetchall()
        

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

        self.cursor.execute("select student_ID from student where last_name = %s", (self.last_name.get(),))
        for student in self.cursor.fetchall():
            student_ID = student[0]

        self.cursor.execute('''select gradebook.assignment from gradebook where
                                            gradebook.student_ID = %s and gradebook.course_ID = 1''', (student_ID,))
        assignment_list = self.cursor.fetchall()
        assignment0 = assignment_list[0]
        assignment1 = assignment_list[1]
        assignment2 = assignment_list[2]
        assignment3 = assignment_list[3]

        i = 0
        for grade in self.grades:
            self.cursor.execute('''update gradebook set score = %s where
                                assignment = %s and student_ID = %s and course_ID = 1''', (grade.get(), eval(f'assignment{i}[0]'), student_ID))
            self.mydb.commit()
            i+=1
        messagebox.showinfo("Success", "Student grades have been entered.")