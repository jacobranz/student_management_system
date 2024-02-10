class AddProfessor_English120(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(master=parent)
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
