class AddStudent_Physics101(ctk.CTkFrame):
    def __init__(self, parent, controller):
        self.max_students = 20

        super().__init__(master=parent)
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
