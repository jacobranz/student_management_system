import customtkinter as ctk

from .math_150 import Math150
from .english_120 import English120
from .music_100 import Music100
from .example import Example
from .report_card import ReportCard
from .physics_101 import Physics101

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
