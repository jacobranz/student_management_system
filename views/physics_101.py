class Physics101(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(master=parent)
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
