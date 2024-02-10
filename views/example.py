#####################
#From FirstProject.py
#####################
class Example(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(master=parent)

        #This is the first window you see and has the 3 buttons for navigating to other windows
        b1 = ctk.CTkButton(self, text="Manage Students", command = self.studentWindow)
        b1.pack(side="left",anchor='n', padx=40, pady=10)

        b2 = ctk.CTkButton(self, text="Manage Teachers", command = self.teacherWindow)
        b2.pack(side="left",anchor='n', padx=40, pady=10)

        #lambda: controller.show_frame(ClassPage)
        b3 = ctk.CTkButton(self, text="Course Management", command = lambda: controller.show_frame(ClassPage))
        b3.pack(side="left",anchor='n', padx=40, pady=10)
        
        studenttitle = ctk.CTkLabel(self, width=30, text="School Force", fg_color="DarkBlue", font=("times new roman", 15, "bold"))
        studenttitle.pack(side="top",anchor='w', padx=40, pady=10)

        studenttitle = ctk.CTkLabel(self, width=30, text="Ranz Release 4.2.1", fg_color="black", font=("times new roman", 8, "bold"))
        studenttitle.pack(side="bottom",anchor='w', padx=40, pady=10)
        
        root.lift()
        self.splashwindow()
        
    def splashwindow(self):
        window = ctk.CTkToplevel(self)
        window.attributes("-topmost", True)
        window.geometry("%dx%d%+d%+d" % (520, 350, 10, 10))
        window.title('Loading')
        #This is the image in the students window
        img = Image.open('intro.jpg')
        self.tkimage = ImageTk.PhotoImage(img)
        ctk.CTkLabel(window,image = self.tkimage).place(x=0, y=0)
        
        window.after(5000,lambda:window.destroy())
      
    def studentWindow(self):
        window = ctk.CTkToplevel(self)
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        #Window Title
        studenttitle = ctk.CTkLabel(window, width=18, text="Manage Students", fg_color="black", font=("times new roman", 15, "bold"))
        studenttitle.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        #Creating a frame. This frame holds all the information for writing student data to the database. This frame holds buttons and entry boxes. Move this frame around and everything inside will follow
        Student_write_Frame = ctk.CTkFrame(window)
        Student_write_Frame.grid(row=0, column=2)
        
        #Setting the main window size
        window.geometry("%dx%d%+d%+d" % (1350, 550, 10, 10))
        window.grid_columnconfigure((0,1), weight=1)

        #Creating variables used in this window
        self.studentID_var = ctk.IntVar()
        self.studentFirstName_var = ctk.StringVar()
        self.studentLastName_var = ctk.StringVar()
        self.studentAge_var = ctk.IntVar()
        self.studentGradeLevel_var = ctk.IntVar()
        self.studentSearchID_var = ctk.StringVar()
        self.studentSearchName_var = ctk.StringVar()

        #This is creating labels
        #Student_Label_1 = tk.Label(Student_write_Frame, text="Student ID", bg="LightGrey", bd=5)
        #Student_Label_1.grid(row=1, column=0)
        Student_Label_2 = ctk.CTkLabel(Student_write_Frame, text="Student First Name",)
        Student_Label_2.grid(row=2, column=0)
        Student_Label_3 = ctk.CTkLabel(Student_write_Frame, text="Student Last Name")
        Student_Label_3.grid(row=3, column=0)
        Student_Label_4 = ctk.CTkLabel(Student_write_Frame, text="Age")
        Student_Label_4.grid(row=4, column=0)
        Student_Label_5 = ctk.CTkLabel(Student_write_Frame, text="Grade Level")
        Student_Label_5.grid(row=5, column=0)

        #This is creating labels and tying their input into variables
        #Student_Entry_1 = tk.Entry(Student_write_Frame, textvariable = self.studentID_var)
        #Student_Entry_1.grid(row=1, column=4)
        Student_Entry_2 = ctk.CTkEntry(Student_write_Frame, textvariable = self.studentFirstName_var)
        Student_Entry_2.grid(row=2, column=4)
        Student_Entry_3 = ctk.CTkEntry(Student_write_Frame, textvariable = self.studentLastName_var)
        Student_Entry_3.grid(row=3, column=4)
        Student_Entry_4 = ctk.CTkEntry(Student_write_Frame, textvariable = self.studentAge_var)
        Student_Entry_4.grid(row=4, column=4)
        Student_Entry_5 = ctk.CTkEntry(Student_write_Frame, textvariable = self.studentGradeLevel_var)
        Student_Entry_5.grid(row=5, column=4)

        #This is the button for writing data to a database
        buttons_student_write = ctk.CTkButton(Student_write_Frame, text="Write to Database", command= self.studentwrite)
        buttons_student_write.grid(row=1, column=40, padx=25, pady=5, sticky="w")

        #This is the image in the students window
        img = Image.open('logo.jpg')
        self.tkimage = ImageTk.PhotoImage(img)
        ctk.CTkLabel(window,image = self.tkimage).place(x=750, y=45)

        #Creating a frame. This frame holds all the information for reading student data from the database. This frame holds buttons and entry boxes. Move this frame around and everything inside will follow
        Student_read_Frame = ctk.CTkFrame(window)
        Student_read_Frame.grid(row=0, column=3)

        #These are the entries and labels for querying students
        Student_Label_6 = ctk.CTkLabel(Student_read_Frame, text="Search By ID")
        Student_Label_6.grid(row=1, column=0, padx=5, pady=5)
        Student_Entry_6 = ctk.CTkEntry(Student_read_Frame, textvariable = self.studentSearchID_var)
        Student_Entry_6.grid(row=2, column=0, padx=5, pady=5)
        Student_Label_7 = ctk.CTkLabel(Student_read_Frame, text="Search By Last Name")
        Student_Label_7.grid(row=3, column=0, padx=5, pady=5) 
        Student_Entry_7 = ctk.CTkEntry(Student_read_Frame, textvariable = self.studentSearchName_var)
        Student_Entry_7.grid(row=4, column=0, padx=5, pady=5)

        #This is the button for querying student data
        buttons_student_search = ctk.CTkButton(Student_read_Frame, command= self.readdatastudent, text="Search Database")
        buttons_student_search.grid(row=5, column=0, padx=25, pady=25)
        #Creating a frame. This frame holds the tree window. Move this frame around and everything inside will follow  
        Student_tree_Frame = ctk.CTkFrame(window)
        Student_tree_Frame.grid(row=0, column=4)
        self.studenttree = ttk.Treeview(Student_tree_Frame, columns=("ID", "FirstName","LastName","Age","Year"))
        self.studenttree.grid(row=1, column=0, padx=5, pady=5)
        self.studenttree.heading("ID", text="ID")
        self.studenttree.heading("FirstName", text="First Name")
        self.studenttree.heading("LastName", text=" Last Name")
        self.studenttree.heading("Age", text="Age")
        self.studenttree.heading("Year", text="Year")
        self.studenttree['show']='headings'
        

    def teacherWindow(self):
        window = ctk.CTkToplevel(self)
        window.geometry("%dx%d%+d%+d" % (1500, 600, 10, 10))
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        #Window Title
        teachertitle = ctk.CTkLabel(window, width=18, text="Manage Teachers", fg_color="black", font=("times new roman", 15, "bold"))
        teachertitle.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        #Creating a frame. This frame holds all the information for writing student data to the database. This frame holds buttons and entry boxes. Move this frame around and everything inside will follow
        Teacher_write_Frame = ctk.CTkFrame(window)
        Teacher_write_Frame.grid(row=1, column=2)
       

        #Creating variables used in this window
        self.teacherID_var = ctk.StringVar()
        self.teacherFirstName_var = ctk.StringVar()
        self.teacherLastName_var = ctk.StringVar()
        self.teacherAge_var = ctk.StringVar()
        self.teacherQual_var = ctk.StringVar()
        self.teacherStart_var = ctk.StringVar()
        self.teacherSearchID_var = ctk.StringVar()
        self.teacherSearchName_var = ctk.StringVar()

        #This is creating labels
        #Teacher_Label_1 = tk.Label(Teacher_write_Frame, text="Teacher ID", bg="LightGrey", bd=5)
        #Teacher_Label_1.grid(row=1, column=0)
        Teacher_Label_2 = ctk.CTkLabel(Teacher_write_Frame, text="Teacher First Name")
        Teacher_Label_2.grid(row=2, column=0)
        Teacher_Label_3 = ctk.CTkLabel(Teacher_write_Frame, text="Teacher Last Name")
        Teacher_Label_3.grid(row=3, column=0)
        Teacher_Label_4 = ctk.CTkLabel(Teacher_write_Frame, text="Age")
        Teacher_Label_4.grid(row=4, column=0)
        Teacher_Label_5 = ctk.CTkLabel(Teacher_write_Frame, text="Qualifications")
        Teacher_Label_5.grid(row=5, column=0)
        Teacher_Label_6 = ctk.CTkLabel(Teacher_write_Frame, text="Start Date")
        Teacher_Label_6.grid(row=6, column=0)

        #This is creating labels and tying their input into variables
        #Teacher_Entry_1 = tk.Entry(Teacher_write_Frame, textvariable = self.teacherID_var)
        #Teacher_Entry_1.grid(row=1, column=4)
        Teacher_Entry_2 = ctk.CTkEntry(Teacher_write_Frame, textvariable = self.teacherFirstName_var)
        Teacher_Entry_2.grid(row=2, column=4)
        Teacher_Entry_3 = ctk.CTkEntry(Teacher_write_Frame, textvariable = self.teacherLastName_var)
        Teacher_Entry_3.grid(row=3, column=4)
        Teacher_Entry_4 = ctk.CTkEntry(Teacher_write_Frame, textvariable = self.teacherAge_var)
        Teacher_Entry_4.grid(row=4, column=4)
        Teacher_Entry_5 = ctk.CTkEntry(Teacher_write_Frame, textvariable = self.teacherQual_var)
        Teacher_Entry_5.grid(row=5, column=4)
        Teacher_Entry_6 = ctk.CTkEntry(Teacher_write_Frame, textvariable = self.teacherStart_var)
        Teacher_Entry_6.grid(row=6, column=4)

        #This is the button for writing data to a database
        buttons_teacher_write = ctk.CTkButton(Teacher_write_Frame, text="Write to Database", command= self.teacherwrite)
        buttons_teacher_write.grid(row=1, column=40, padx=25, pady=5, sticky="w")

        #This is the image in the teacher window
        img = Image.open('logo.jpg')
        self.tkimage = ImageTk.PhotoImage(img)
        ctk.Label(window,image = self.tkimage).place(x=850, y=45)

        #Creating a frame. This frame holds all the information for reading student data from the database. This frame holds buttons and entry boxes. Move this frame around and everything inside will follow
        Teacher_read_Frame = ctk.CTkFrame(window)
        Teacher_read_Frame.grid(row=1, column=4)

        #These are the entries and labels for querying students
        Teacher_Label_7 = ctk.CTkLabel(Teacher_read_Frame, text="Search By ID")
        Teacher_Label_7.grid(row=1, column=0, padx=5, pady=5)
        Teacher_Entry_7 = ctk.CTkEntry(Teacher_read_Frame, textvariable = self.teacherSearchID_var)
        Teacher_Entry_7.grid(row=2, column=0, padx=5, pady=5)
        Teacher_Label_8 = ctk.CTkLabel(Teacher_read_Frame, text="Search By Last Name")
        Teacher_Label_8.grid(row=3, column=0, padx=5, pady=5) 
        Teacher_Entry_9 = ctk.CTkEntry(Teacher_read_Frame, textvariable = self.teacherSearchName_var)
        Teacher_Entry_9.grid(row=4, column=0, padx=5, pady=5)

        #This is the button for querying student data
        buttons_teacher_search = ctk.CTkButton(Teacher_read_Frame, command= self.readdatateacher, text="Search Database")
        buttons_teacher_search.grid(row=5, column=0, padx=25, pady=25)

        #Creating a frame. This frame holds the tree window. Move this frame around and everything inside will follow  
        Teacher_tree_Frame = Frame(window)
        Teacher_tree_Frame.grid(row=1, column=6)
        self.teachertree = ttk.Treeview(Teacher_tree_Frame, columns=("ID", "FirstName","LastName","Age","Qual","Start"))
        self.teachertree.grid(row=1, column=0, padx=5, pady=5)
        self.teachertree.heading("ID", text="ID")
        self.teachertree.heading("FirstName", text="First Name")
        self.teachertree.heading("LastName", text=" Last Name")
        self.teachertree.heading("Age", text="Age")
        self.teachertree.heading("Qual", text="Qualifications")
        self.teachertree.heading("Start", text="Start Date")
        self.teachertree['show']='headings'
		

        
    def sectionWindow(self, controller):
        window = ctk.CTkToplevel(self)
        window.geometry("%dx%d%+d%+d" % (1100, 550, 10, 10))
        window.grid_columnconfigure((0,1), weight=1)

        #Window Title
        sectiontitle = ctk.CTkLabel(window, width=18, text="Manage sections", fg_color="black", font=("times new roman", 15, "bold"))
        sectiontitle.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        #Creating a frame. This frame holds all the information for writing class data to the database. This frame holds buttons and entry boxes. Move this frame around and everything inside will follow
        section_write_Frame = ctk.CTkFrame(window, bd=4, relief=RIDGE, bg="LightGrey")
        section_write_Frame.place(x=50, y=45, width=450, height=150)

        #Creating variables
        self.sectionID_var = ctk.StringVar()
        self.sectionName_var = ctk.StringVar()
        self.sectionCreds_var = ctk.StringVar()
        self.sectionProf_var = ctk.StringVar()
        self.sectionSearchID_var = ctk.StringVar()
        self.sectionSearchName_var = ctk.StringVar()

        #This is creating labels
        section_Label_1 = ctk.CTkLabel(section_write_Frame, text="section ID", bg="LightGrey", bd=5)
        section_Label_1.grid(row=1, column=0)
        section_Label_2 = ctk.CTkLabel(section_write_Frame, text="Section Name", bg="LightGrey", bd=5)
        section_Label_2.grid(row=2, column=0)
        section_Label_3 = ctk.CTkLabel(section_write_Frame, text="Credits", bg="LightGrey", bd=5)
        section_Label_3.grid(row=3, column=0)
        section_Label_4 = ctk.CTkLabel(section_write_Frame, text="Professor", bg="LightGrey", bd=5)
        section_Label_4.grid(row=4, column=0)

        #This is creating labels and tying their input into variables
        section_Entry_1 = ctk.CTkEntry(section_write_Frame, textvariable = self.sectionID_var)
        section_Entry_1.grid(row=1, column=4)
        section_Entry_2 = ctk.CTkEntry(section_write_Frame, textvariable = self.sectionName_var)
        section_Entry_2.grid(row=2, column=4)
        section_Entry_3 = ctk.CTkEntry(section_write_Frame, textvariable = self.sectionCreds_var)
        section_Entry_3.grid(row=3, column=4)
        section_Entry_4 = ctk.CTkEntry(section_write_Frame, textvariable = self.sectionProf_var)
        section_Entry_4.grid(row=4, column=4)


        #This is the button for writing data to a database
        buttons_section_write = ctk.CTkButton(section_write_Frame, text="Write to Database", command= self.sectionwrite)
        buttons_section_write.grid(row=1, column=40, padx=25, pady=5, sticky="w")

        #This is the image in the section window
        img = Image.open('logo.jpg')
        self.tkimage = ImageTk.PhotoImage(img)
        ctk.CTkLabel(window,image = self.tkimage).place(x=650, y=45)

        #Creating a frame. This frame holds all the information for reading class data from the database. This frame holds buttons and entry boxes. Move this frame around and everything inside will follow
        section_read_Frame = ctk.CTkFrame(window, bd=4, relief=RIDGE, bg="LightGrey")
        section_read_Frame.place(x=900, y=250, width=150, height=200)

        #These are the entries and labels for querying classes
        section_Label_7 = ctk.CTkLabel(section_read_Frame, text="Search By ID", bg="LightGrey", bd=5)
        section_Label_7.grid(row=1, column=0, padx=5, pady=5)
        section_Entry_7 = ctk.CTkEntry(section_read_Frame, textvariable = self.sectionSearchID_var)
        section_Entry_7.grid(row=2, column=0, padx=5, pady=5)
        section_Label_8 = ctk.CTkLabel(section_read_Frame, text="Search By Name", bg="LightGrey", bd=5)
        section_Label_8.grid(row=3, column=0, padx=5, pady=5) 
        section_Entry_9 = ctk.CTkEntry(section_read_Frame, textvariable = self.sectionSearchName_var)
        section_Entry_9.grid(row=4, column=0, padx=5, pady=5)

        #This is the button for querying class data
        buttons_section_search = ctk.CTkButton(section_read_Frame, command= self.readdataclass, text="Search Database")
        buttons_section_search.grid(row=5, column=0, padx=25, pady=25)

        #Creating a frame. This frame holds the tree window. Move this frame around and everything inside will follow  
        section_tree_Frame = ctk.CTkFrame(window, bd=4, relief=RIDGE, bg="LightGrey")
        section_tree_Frame.place(x=20, y=250, width=825, height=250)
        self.sectiontree = ttk.Treeview(section_tree_Frame, columns=("ID", "Name","Creds","Prof"))
        self.sectiontree.grid(row=1, column=0, padx=5, pady=5)
        self.sectiontree.heading("ID", text="ID")
        self.sectiontree.heading("Name", text="Name")
        self.sectiontree.heading("Creds", text="Credits")
        self.sectiontree.heading("Prof", text="Professor")
        self.sectiontree['show']='headings'
        
    def sectionwrite(self):
        #con = mysql.connector.connect(host="localhost", user="root", password="ctu1234", database="grades")
        #cur = con.cursor()
        cursor.execute("insert into course values(%s, %s, %s, %s)", (self.sectionID_var.get(), self.sectionName_var.get(), self.sectionCreds_var.get(), self.sectionProf_var.get()))
        mydb.commit()
        messagebox.showinfo("Successfull", "Record has been inserted.")

    def studentwrite(self):
        #con = mysql.connector.connect(host="localhost", user="root", password="ctu1234", database="grades")
        #cur = con.cursor()
        cursor.execute("insert into student (first_name, last_name, age, grade_level) values (%s, %s, %s, %s)", (self.studentFirstName_var.get(), self.studentLastName_var.get(), self.studentAge_var.get(), self.studentGradeLevel_var.get()))
        mydb.commit()
        messagebox.showinfo("Successfull", "Record has been inserted.")
        self.studentFirstName_var.set("")
        self.studentLastName_var.set("")
        self.studentAge_var.set("")
        self.studentGradeLevel_var.set("")

    def teacherwrite(self):
        #con = mysql.connector.connect(host="localhost", user="root", password="ctu1234", database="grades")
        #cur = con.cursor()
        cursor.execute("insert into professor (first_name, last_name, age, qualifications, start_date) values(%s, %s, %s, %s, %s)", (self.teacherFirstName_var.get(), self.teacherLastName_var.get(), self.teacherAge_var.get(), self.teacherQual_var.get(), self.teacherStart_var.get()))
        mydb.commit()
        messagebox.showinfo("Successfull", "Record has been inserted.")
        self.teacherFirstName_var.set("")
        self.teacherLastName_var.set("")
        self.teacherAge_var.set("")
        self.teacherQual_var.set("")
        self.teacherStart_var.set("")

            
    def readdatastudent(self):

        if len(self.studentSearchID_var.get()) == 0:

            #con = mysql.connector.connect(host="localhost", user="root", password="ctu1234", database="grades")
            #cur = con.cursor()
         
            sql = "SELECT * FROM student WHERE last_name = %s"
            adr = self.studentSearchName_var.get()

            val = cursor.execute(sql, (adr,))

            rows = cursor.fetchall()
            if(len(rows)!=0):
                self.studenttree.delete(*self.studenttree.get_children())
                for row in rows:
                    self.studenttree.insert('', END, values=row)

                mydb.commit()
            else:
                messagebox.showinfo("No", "Student is not registered in the database!")
                self.studentSearchName_var.set("")

        elif len(self.studentSearchName_var.get()) == 0:

            #con = mysql.connector.connect(host="localhost", user="root", password="ctu1234", database="grades")
            #cur = con.cursor()
         
            sql = "SELECT * FROM student WHERE student_ID = %s"
            adr = self.studentSearchID_var.get()

            val = cursor.execute(sql, (adr,))

            rows = cursor.fetchall()
            if(len(rows)!=0):
                self.studenttree.delete(*self.studenttree.get_children())
                for row in rows:
                    self.studenttree.insert('', END, values=row)

                mydb.commit()
            else:
                messagebox.showinfo("No", "Student is not registered in the database!")
                self.studentSearchID_var.set("")
        else:
            messagebox.showinfo("Error", "Please use 1 criteria.")
            

    def readdatateacher(self):

        if len(self.teacherSearchID_var.get()) == 0:

            #con = mysql.connector.connect(host="localhost", user="root", password="ctu1234", database="grades")
            #cur = con.cursor()
         
            sql = "SELECT * FROM professor WHERE last_name = %s"
            adr = self.teacherSearchName_var.get()

            val = cursor.execute(sql, (adr,))

            rows = cursor.fetchall()
            if(len(rows)!=0):
                self.teachertree.delete(*self.teachertree.get_children())
                for row in rows:
                    self.teachertree.insert('', END, values=row)

                mydb.commit()
            else:
                messagebox.showinfo("No", "Professor is not registered in the database!")
                self.teacherSearchName_var.set("")

        elif len(self.teacherSearchName_var.get()) == 0:

            #con = mysql.connector.connect(host="localhost", user="root", password="ctu1234", database="grades")
            #cur = con.cursor()
         
            sql = "SELECT * FROM professor WHERE professor_ID = %s"
            adr = self.teacherSearchID_var.get()

            val = cursor.execute(sql, (adr,))

            rows = cursor.fetchall()
            if(len(rows)!=0):
                self.teachertree.delete(*self.teachertree.get_children())
                for row in rows:
                    self.teachertree.insert('', END, values=row)

                mydb.commit()
            else:
                messagebox.showinfo("No", "Professor is not registered in the database!")
                self.teacherSearchID_var.set("")
        else:
            messagebox.showinfo("Error", "Please use 1 criteria.")

    def readdataclass(self):
            
        if len(self.sectionSearchID_var.get()) == 0:

            con = mysql.connector.connect(host="localhost", user="root", password="ctu1234", database="grades")
            cur = con.cursor()
         
            sql = "SELECT * FROM course WHERE name = %s"
            adr = self.sectionSearchName_var.get()

            val = cur.execute(sql, adr)
            if(not val):
                messagebox.showinfo("No", "Not availabe!")

            rows = cur.fetchall()
            if(len(rows)!=0):
                self.sectiontree.delete(*self.sectiontree.get_children())
                for row in rows:
                    self.sectiontree.insert('', END, values=row)

                con.commit()
            con.close()

        elif len(self.sectionSearchName_var.get()) == 0:

            con = mysql.connector.connect(host="localhost", user="root", password="ctu1234", database="grades")
            cur = con.cursor()
         
            sql = "SELECT * FROM course WHERE course_ID = %s"
            adr = self.sectionSearchID_var.get()

            val = cur.execute(sql, adr)
            if(not val):
                messagebox.showinfo("No", "Not availabe!")

            rows = cur.fetchall()
            if(len(rows)!=0):
                self.sectiontree.delete(*self.sectiontree.get_children())
                for row in rows:
                    self.sectiontree.insert('', END, values=row)

                con.commit()
            con.close()
        else:
            messagebox.showinfo("Error", "Please use 1 criteria.")
