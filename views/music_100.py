import customtkinter as ctk

#from .class_page import ClassPage
from ..enter_grades.enter_grades_music import EnterGrades_Music100
from ..add_professor.add_professor_music import AddProfessor_Music100
from ..add_student.add_student_music import AddStudent_Music100

class Music100(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(master=parent)
        label = ctk.CTkLabel(self, text="MUSIC 100 ACTIONS")
        label.pack(padx=10, pady=10)

        button1 = ctk.CTkButton(self, text="Enter Grades", command= lambda: controller.show_frame(EnterGrades_Music100))
        button2 = ctk.CTkButton(self, text="Add Student", command= lambda: controller.show_frame(AddStudent_Music100))
        button3 = ctk.CTkButton(self, text="Add Professor", command= lambda: controller.show_frame(AddProfessor_Music100))
        #button4 = ctk.CTkButton(self, text="Back to Class Selection", command= lambda: controller.show_frame(ClassPage))

        button1.pack()
        button2.pack()
        button3.pack()
        #button4.pack()