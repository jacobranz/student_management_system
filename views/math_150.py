import customtkinter as ctk

from .class_page import ClassPage
from ..add_professor.add_professor_math import AddProfessor_Math150
from ..add_student.add_student_math import AddStudent_Math150
from ..enter_grades.enter_grades_math import EnterGrades_Math150

class Math150(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(master=parent)
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
