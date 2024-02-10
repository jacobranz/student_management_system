from tkinter import messagebox
import customtkinter as ctk

from ..views.class_page import ClassPage

class AddProfessor_Math150(ctk.CTkFrame):
    def __init__(self, parent, controller, mydb, cursor):
        super().__init__(master=parent)
        label = ctk.CTkLabel(self, text="ADD PROFESSOR")
        #label.pack(padx=10, pady=10)

        self.mydb = mydb
        self.cursor = cursor

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
        self.cursor.execute("select professor_ID from professor where last_name = %s", (self.last_name.get(),))
        prof_last = self.cursor.fetchall()
        for prof in prof_last:
            prof = prof[0]
        if len(prof_last) == 0:
            messagebox.showwarning("No Entry Found", "Professor entered does not exist in the system!")
            self.last_name.set("")
    
        self.cursor.execute("select professor_ID from course where name = 'Math 150'")
        course_info = self.cursor.fetchall()

        if len(course_info) > 0:
            messagebox.showwarning("No Entry Found", "Math 150 already has a professor!")
            self.last_name.set("")
        else:
            ## insert the professor id into the course
            #self.cursor.execute("insert into course values (2, 'Math 150', 4, %s)", (prof,))
            self.cursor.execute("update course set professor_ID = %s where course_ID = 2", (prof,))
            self.mydb.commit()
            messagebox.showinfo("Success", "Professor has been added to Math 150!")
            self.last_name.set("")