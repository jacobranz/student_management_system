from tkinter import messagebox
import customtkinter as ctk

from .class_page import ClassPage

class ReportCard(ctk.CTkFrame):
    def __init__(self, parent, controller, cursor):
        super().__init__(master=parent)
        
        self.cursor = cursor
        
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
        
        self.cursor.execute(sql, adr)
        students = self.cursor.fetchall()
        for student in students:
            student_ID = student[0]

        if len(students) == 0:
            messagebox.showwarning("No Entry Found", "Student entered does not exist in the system!")
            self.last_name.set("")

        # gets all courses that student is in
        self.cursor.execute('''select c.course_ID from course c, enrollment e where
                                e.student_ID = %s and e.course_ID = c.course_ID
                                order by name asc''', (student_ID,))
        course_list = self.cursor.fetchall()

        i=0
        row=6
        column=1
        for course_ID in course_list:
            if course_ID == "":
                break

            self.cursor.execute("select name from course where course_ID = %s", course_ID)
            course_name = self.cursor.fetchone()
            
            ctk.CTkLabel(self, text=course_name[0]).grid(row=(row + i), column=column)

            self.cursor.execute('''select score, weight from gradebook 
                                    where student_ID = %s and course_ID = %s
                                    ''', (student_ID, course_ID[0]))
            allgrades = self.cursor.fetchall()
            
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
            self.cursor.execute("select creds from course where course_ID = %s", course_ID)
            credit_count = self.cursor.fetchall()
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
