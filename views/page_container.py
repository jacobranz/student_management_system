import customtkinter as ctk

from .class_page import ClassPage
from .report_card import ReportCard
from .math_150 import Math150
from .english_120 import English120
from .physics_101 import Physics101
from .music_100 import Music100
from .example import Example
from ..enter_grades.enter_grades_english import EnterGrades_English120
from ..enter_grades.enter_grades_math import EnterGrades_Math150
from ..enter_grades.enter_grades_music import EnterGrades_Music100
from ..enter_grades.enter_grades_physics import EnterGrades_Physics101
from ..add_student.add_student_english import AddStudent_English120
from ..add_student.add_student_math import AddStudent_Math150
from ..add_student.add_student_music import AddStudent_Music100
from ..add_student.add_student_physics import AddStudent_Physics101

class PageContainer(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

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