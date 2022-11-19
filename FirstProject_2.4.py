from tkinter import ttk
import tkinter as tk
from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import ImageTk, Image

class Example(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)

        #This is the first window you see and has the 3 buttons for navigating to other windows
        b1 = tk.Button(self, text="Student", command = self.studentWindow)
        b1.pack(side="left",anchor='n', padx=40, pady=10)

        b2 = tk.Button(self, text="Teacher", command = self.teacherWindow)
        b2.pack(side="left",anchor='n', padx=40, pady=10)

        b3 = tk.Button(self, text="Class", command = self.show_classes)
        b3.pack(side="left",anchor='n', padx=40, pady=10)
      
    def studentWindow(self):
        window = tk.Toplevel(self)

        #Window Title
        studenttitle = Label(window, width=18, text="Manage Students", fg="black", font=("times new roman", 15, "bold"))
        studenttitle.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        #Creating a frame. This frame holds all the information for writing student data to the database. This frame holds buttons and entry boxes. Move this frame around and everything inside will follow
        Student_write_Frame = Frame(window, bd=4, relief=RIDGE, bg="LightBlue")
        Student_write_Frame.place(x=50, y=45, width=450, height=175)
        
        #Setting the main window size
        window.geometry("%dx%d%+d%+d" % (1250, 550, 10, 10))
        window.grid_columnconfigure((0,1), weight=1)

        #Creating variables used in this window
        self.studentID_var = StringVar()
        self.studentFirstName_var = StringVar()
        self.studentLastName_var = StringVar()
        self.studentAge_var = StringVar()
        self.studentGradeLevel_var = StringVar()
        self.studentSearchID_var = StringVar()
        self.studentSearchName_var = StringVar()

        #This is creating labels
        Student_Label_1 = tk.Label(Student_write_Frame, text="Student ID", bg="LightBlue", bd=5)
        Student_Label_1.grid(row=1, column=0)
        Student_Label_2 = tk.Label(Student_write_Frame, text="Student First Name", bg="LightBlue", bd=5)
        Student_Label_2.grid(row=2, column=0)
        Student_Label_3 = tk.Label(Student_write_Frame, text="Student Last Name", bg="LightBlue", bd=5)
        Student_Label_3.grid(row=3, column=0)
        Student_Label_4 = tk.Label(Student_write_Frame, text="Age", bg="LightBlue", bd=5)
        Student_Label_4.grid(row=4, column=0)
        Student_Label_5 = tk.Label(Student_write_Frame, text="Grade Level", bg="LightBlue", bd=5)
        Student_Label_5.grid(row=5, column=0)

        #This is creating labels and tying their input into variables
        Student_Entry_1 = tk.Entry(Student_write_Frame, textvariable = self.studentID_var)
        Student_Entry_1.grid(row=1, column=4)
        Student_Entry_2 = tk.Entry(Student_write_Frame, textvariable = self.studentFirstName_var)
        Student_Entry_2.grid(row=2, column=4)
        Student_Entry_3 = tk.Entry(Student_write_Frame, textvariable = self.studentLastName_var)
        Student_Entry_3.grid(row=3, column=4)
        Student_Entry_4 = tk.Entry(Student_write_Frame, textvariable = self.studentAge_var)
        Student_Entry_4.grid(row=4, column=4)
        Student_Entry_5 = tk.Entry(Student_write_Frame, textvariable = self.studentGradeLevel_var)
        Student_Entry_5.grid(row=5, column=4)

        #This is the button for writing data to a database
        buttons_student_write = tk.Button(Student_write_Frame, text="Write to Database", command= self.studentwrite)
        buttons_student_write.grid(row=1, column=40, padx=25, pady=5, sticky="w")

        buttons_student_write = tk.Button(window, text="Manage Grades", command= self.display)
        buttons_student_write.grid(row=1, column=2, padx=2, pady=2, sticky="w")

        #This is the image in the students window
        img = Image.open('logo.jpg')
        self.tkimage = ImageTk.PhotoImage(img)
        Label(window,image = self.tkimage).place(x=750, y=45)

        #Creating a frame. This frame holds all the information for reading student data from the database. This frame holds buttons and entry boxes. Move this frame around and everything inside will follow
        Student_read_Frame = Frame(window, bd=4, relief=RIDGE, bg="LightBlue")
        Student_read_Frame.place(x=1075, y=250, width=150, height=200)

        #These are the entries and labels for querying students
        Student_Label_6 = tk.Label(Student_read_Frame, text="Search By ID", bg="LightBlue", bd=5)
        Student_Label_6.grid(row=1, column=0, padx=5, pady=5)
        Student_Entry_6 = tk.Entry(Student_read_Frame, textvariable = self.studentSearchID_var)
        Student_Entry_6.grid(row=2, column=0, padx=5, pady=5)
        Student_Label_7 = tk.Label(Student_read_Frame, text="Search By Last Name", bg="LightBlue", bd=5)
        Student_Label_7.grid(row=3, column=0, padx=5, pady=5) 
        Student_Entry_7 = tk.Entry(Student_read_Frame, textvariable = self.studentSearchName_var)
        Student_Entry_7.grid(row=4, column=0, padx=5, pady=5)

        #This is the button for querying student data
        buttons_student_search = tk.Button(Student_read_Frame, command= self.readdatastudent, text="Search Database")
        buttons_student_search.grid(row=5, column=0, padx=25, pady=25)

        #Creating a frame. This frame holds the tree window. Move this frame around and everything inside will follow  
        Student_tree_Frame = Frame(window, bd=4, relief=RIDGE, bg="LightBlue")
        Student_tree_Frame.place(x=20, y=250, width=1025, height=250)
        self.studenttree = ttk.Treeview(Student_tree_Frame, columns=("ID", "FirstName","LastName","Age","Year"))
        self.studenttree.grid(row=1, column=0, padx=5, pady=5)
        self.studenttree.heading("ID", text="ID")
        self.studenttree.heading("FirstName", text="First Name")
        self.studenttree.heading("LastName", text=" Last Name")
        self.studenttree.heading("Age", text="Age")
        self.studenttree.heading("Year", text="Year")
        self.studenttree['show']='headings'
        

    def teacherWindow(self):
        window = tk.Toplevel(self)
        window.geometry("%dx%d%+d%+d" % (1500, 600, 10, 10))
        window.grid_columnconfigure((0,1), weight=1)

        #Window Title
        teachertitle = Label(window, width=18, text="Manage Teachers", fg="black", font=("times new roman", 15, "bold"))
        teachertitle.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        #Creating a frame. This frame holds all the information for writing student data to the database. This frame holds buttons and entry boxes. Move this frame around and everything inside will follow
        Teacher_write_Frame = Frame(window, bd=4, relief=RIDGE, bg="LightBlue")
        Teacher_write_Frame.place(x=50, y=45, width=450, height=200)
       

        #Creating variables used in this window
        self.teacherID_var = StringVar()
        self.teacherFirstName_var = StringVar()
        self.teacherLastName_var = StringVar()
        self.teacherAge_var = StringVar()
        self.teacherQual_var = StringVar()
        self.teacherStart_var = StringVar()
        self.teacherSearchID_var = StringVar()
        self.teacherSearchName_var = StringVar()

        #This is creating labels
        Teacher_Label_1 = tk.Label(Teacher_write_Frame, text="Teacher ID", bg="LightBlue", bd=5)
        Teacher_Label_1.grid(row=1, column=0)
        Teacher_Label_2 = tk.Label(Teacher_write_Frame, text="Teacher First Name", bg="LightBlue", bd=5)
        Teacher_Label_2.grid(row=2, column=0)
        Teacher_Label_3 = tk.Label(Teacher_write_Frame, text="Teacher Last Name", bg="LightBlue", bd=5)
        Teacher_Label_3.grid(row=3, column=0)
        Teacher_Label_4 = tk.Label(Teacher_write_Frame, text="Age", bg="LightBlue", bd=5)
        Teacher_Label_4.grid(row=4, column=0)
        Teacher_Label_5 = tk.Label(Teacher_write_Frame, text="Qualifications", bg="LightBlue", bd=5)
        Teacher_Label_5.grid(row=5, column=0)
        Teacher_Label_6 = tk.Label(Teacher_write_Frame, text="Start Date", bg="LightBlue", bd=5)
        Teacher_Label_6.grid(row=6, column=0)

        #This is creating labels and tying their input into variables
        Teacher_Entry_1 = tk.Entry(Teacher_write_Frame, textvariable = self.teacherID_var)
        Teacher_Entry_1.grid(row=1, column=4)
        Teacher_Entry_2 = tk.Entry(Teacher_write_Frame, textvariable = self.teacherFirstName_var)
        Teacher_Entry_2.grid(row=2, column=4)
        Teacher_Entry_3 = tk.Entry(Teacher_write_Frame, textvariable = self.teacherLastName_var)
        Teacher_Entry_3.grid(row=3, column=4)
        Teacher_Entry_4 = tk.Entry(Teacher_write_Frame, textvariable = self.teacherAge_var)
        Teacher_Entry_4.grid(row=4, column=4)
        Teacher_Entry_5 = tk.Entry(Teacher_write_Frame, textvariable = self.teacherQual_var)
        Teacher_Entry_5.grid(row=5, column=4)
        Teacher_Entry_6 = tk.Entry(Teacher_write_Frame, textvariable = self.teacherStart_var)
        Teacher_Entry_6.grid(row=6, column=4)

        #This is the button for writing data to a database
        buttons_teacher_write = tk.Button(Teacher_write_Frame, text="Write to Database", command= self.teacherwrite)
        buttons_teacher_write.grid(row=1, column=40, padx=25, pady=5, sticky="w")

        #This is the image in the teacher window
        img = Image.open('logo.jpg')
        self.tkimage = ImageTk.PhotoImage(img)
        Label(window,image = self.tkimage).place(x=850, y=45)

        #Creating a frame. This frame holds all the information for reading student data from the database. This frame holds buttons and entry boxes. Move this frame around and everything inside will follow
        Teacher_read_Frame = Frame(window, bd=4, relief=RIDGE, bg="LightBlue")
        Teacher_read_Frame.place(x=1275, y=300, width=150, height=200)

        #These are the entries and labels for querying students
        Teacher_Label_7 = tk.Label(Teacher_read_Frame, text="Search By ID", bg="LightBlue", bd=5)
        Teacher_Label_7.grid(row=1, column=0, padx=5, pady=5)
        Teacher_Entry_7 = tk.Entry(Teacher_read_Frame, textvariable = self.teacherSearchID_var)
        Teacher_Entry_7.grid(row=2, column=0, padx=5, pady=5)
        Teacher_Label_8 = tk.Label(Teacher_read_Frame, text="Search By Last Name", bg="LightBlue", bd=5)
        Teacher_Label_8.grid(row=3, column=0, padx=5, pady=5) 
        Teacher_Entry_9 = tk.Entry(Teacher_read_Frame, textvariable = self.teacherSearchName_var)
        Teacher_Entry_9.grid(row=4, column=0, padx=5, pady=5)

        #This is the button for querying student data
        buttons_teacher_search = tk.Button(Teacher_read_Frame, command= self.readdatateacher, text="Search Database")
        buttons_teacher_search.grid(row=5, column=0, padx=25, pady=25)

        #Creating a frame. This frame holds the tree window. Move this frame around and everything inside will follow  
        Teacher_tree_Frame = Frame(window, bd=4, relief=RIDGE, bg="LightBlue")
        Teacher_tree_Frame.place(x=20, y=300, width=1225, height=250)
        self.teachertree = ttk.Treeview(Teacher_tree_Frame, columns=("ID", "FirstName","LastName","Age","Qual","Start"))
        self.teachertree.grid(row=1, column=0, padx=5, pady=5)
        self.teachertree.heading("ID", text="ID")
        self.teachertree.heading("FirstName", text="First Name")
        self.teachertree.heading("LastName", text=" Last Name")
        self.teachertree.heading("Age", text="Age")
        self.teachertree.heading("Qual", text="Qualifications")
        self.teachertree.heading("Start", text="Start Date")
        self.teachertree['show']='headings'
		

        
    def sectionWindow(self):
        window = tk.Toplevel(self)
        window.geometry("%dx%d%+d%+d" % (1100, 550, 10, 10))
        window.grid_columnconfigure((0,1), weight=1)

        #Window Title
        sectiontitle = Label(window, width=18, text="Manage sections", fg="black", font=("times new roman", 15, "bold"))
        sectiontitle.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        #Creating a frame. This frame holds all the information for writing class data to the database. This frame holds buttons and entry boxes. Move this frame around and everything inside will follow
        section_write_Frame = Frame(window, bd=4, relief=RIDGE, bg="LightBlue")
        section_write_Frame.place(x=50, y=45, width=450, height=150)

        #Creating variables
        self.sectionID_var = StringVar()
        self.sectionName_var = StringVar()
        self.sectionCreds_var = StringVar()
        self.sectionProf_var = StringVar()
        self.sectionSearchID_var = StringVar()
        self.sectionSearchName_var = StringVar()

        #This is creating labels
        section_Label_1 = tk.Label(section_write_Frame, text="section ID", bg="LightBlue", bd=5)
        section_Label_1.grid(row=1, column=0)
        section_Label_2 = tk.Label(section_write_Frame, text="Section Name", bg="LightBlue", bd=5)
        section_Label_2.grid(row=2, column=0)
        section_Label_3 = tk.Label(section_write_Frame, text="Credits", bg="LightBlue", bd=5)
        section_Label_3.grid(row=3, column=0)
        section_Label_4 = tk.Label(section_write_Frame, text="Professor", bg="LightBlue", bd=5)
        section_Label_4.grid(row=4, column=0)

        #This is creating labels and tying their input into variables
        section_Entry_1 = tk.Entry(section_write_Frame, textvariable = self.sectionID_var)
        section_Entry_1.grid(row=1, column=4)
        section_Entry_2 = tk.Entry(section_write_Frame, textvariable = self.sectionName_var)
        section_Entry_2.grid(row=2, column=4)
        section_Entry_3 = tk.Entry(section_write_Frame, textvariable = self.sectionCreds_var)
        section_Entry_3.grid(row=3, column=4)
        section_Entry_4 = tk.Entry(section_write_Frame, textvariable = self.sectionProf_var)
        section_Entry_4.grid(row=4, column=4)


        #This is the button for writing data to a database
        buttons_section_write = tk.Button(section_write_Frame, text="Write to Database", command= self.sectionwrite)
        buttons_section_write.grid(row=1, column=40, padx=25, pady=5, sticky="w")

        #This is the image in the section window
        img = Image.open('logo.jpg')
        self.tkimage = ImageTk.PhotoImage(img)
        Label(window,image = self.tkimage).place(x=650, y=45)

        #Creating a frame. This frame holds all the information for reading class data from the database. This frame holds buttons and entry boxes. Move this frame around and everything inside will follow
        section_read_Frame = Frame(window, bd=4, relief=RIDGE, bg="LightBlue")
        section_read_Frame.place(x=900, y=250, width=150, height=200)

        #These are the entries and labels for querying classes
        section_Label_7 = tk.Label(section_read_Frame, text="Search By ID", bg="LightBlue", bd=5)
        section_Label_7.grid(row=1, column=0, padx=5, pady=5)
        section_Entry_7 = tk.Entry(section_read_Frame, textvariable = self.sectionSearchID_var)
        section_Entry_7.grid(row=2, column=0, padx=5, pady=5)
        section_Label_8 = tk.Label(section_read_Frame, text="Search By Name", bg="LightBlue", bd=5)
        section_Label_8.grid(row=3, column=0, padx=5, pady=5) 
        section_Entry_9 = tk.Entry(section_read_Frame, textvariable = self.sectionSearchName_var)
        section_Entry_9.grid(row=4, column=0, padx=5, pady=5)

        #This is the button for querying class data
        buttons_section_search = tk.Button(section_read_Frame, command= self.readdataclass, text="Search Database")
        buttons_section_search.grid(row=5, column=0, padx=25, pady=25)

        #Creating a frame. This frame holds the tree window. Move this frame around and everything inside will follow  
        section_tree_Frame = Frame(window, bd=4, relief=RIDGE, bg="LightBlue")
        section_tree_Frame.place(x=20, y=250, width=825, height=250)
        self.sectiontree = ttk.Treeview(section_tree_Frame, columns=("ID", "Name","Creds","Prof"))
        self.sectiontree.grid(row=1, column=0, padx=5, pady=5)
        self.sectiontree.heading("ID", text="ID")
        self.sectiontree.heading("Name", text="Name")
        self.sectiontree.heading("Creds", text="Credits")
        self.sectiontree.heading("Prof", text="Professor")
        self.sectiontree['show']='headings'
        
    def sectionwrite(self):
        con = mysql.connector.connect(host="localhost", user="root", password="ctu1234", database="grades")
        cur = con.cursor()
        cur.execute("insert into course values(%s, %s, %s, %s)", (self.sectionID_var.get(), self.sectionName_var.get(), self.sectionCreds_var.get(), self.sectionProf_var.get()))
        con.commit()
        con.close()
        messagebox.showinfo("Successfull", "Record has been inserted.")

    def studentwrite(self):
        con = mysql.connector.connect(host="localhost", user="root", password="ctu1234", database="grades")
        cur = con.cursor()
        cur.execute("insert into student values(%s, %s, %s, %s, %s)", (self.studentID_var.get(), self.studentFirstName_var.get(), self.studentLastName_var.get(), self.studentAge_var.get(), self.studentGradeLevel_var.get()))
        con.commit()
        con.close()
        messagebox.showinfo("Successfull", "Record has been inserted.")

    def teacherwrite(self):
        con = mysql.connector.connect(host="localhost", user="root", password="ctu1234", database="grades")
        cur = con.cursor()
        cur.execute("insert into professor values(%s, %s, %s, %s, %s, %s)", (self.teacherID_var.get(), self.teacherFirstName_var.get(), self.teacherLastName_var.get(), self.teacherAge_var.get(), self.teacherQual_var.get(), self.teacherStart_var.get()))
        con.commit()
        con.close()
        messagebox.showinfo("Successfull", "Record has been inserted.")

            
    def readdatastudent(self):

        if len(self.studentSearchID_var.get()) == 0:

            con = mysql.connector.connect(host="localhost", user="root", password="ctu1234", database="grades")
            cur = con.cursor()
         
            sql = "SELECT * FROM student WHERE last_name = %s"
            adr = self.studentSearchName_var.get()

            val = cur.execute(sql, adr)
            if(not val):
                messagebox.showinfo("No", "Not availabe!")

            rows = cur.fetchall()
            if(len(rows)!=0):
                self.studenttree.delete(*self.studenttree.get_children())
                for row in rows:
                    self.studenttree.insert('', END, values=row)

                con.commit()
            con.close()

        elif len(self.studentSearchName_var.get()) == 0:

            con = mysql.connector.connect(host="localhost", user="root", password="ctu1234", database="grades")
            cur = con.cursor()
         
            sql = "SELECT * FROM student WHERE student_ID = %s"
            adr = self.studentSearchID_var.get()

            val = cur.execute(sql, adr)
            if(not val):
                messagebox.showinfo("No", "Not availabe!")

            rows = cur.fetchall()
            if(len(rows)!=0):
                self.studenttree.delete(*self.studenttree.get_children())
                for row in rows:
                    self.studenttree.insert('', END, values=row)

                con.commit()
            con.close()
        else:
            messagebox.showinfo("Error", "Please use 1 criteria.")
            

    def readdatateacher(self):

        if len(self.teacherSearchID_var.get()) == 0:

            con = mysql.connector.connect(host="localhost", user="root", password="ctu1234", database="grades")
            cur = con.cursor()
         
            sql = "SELECT * FROM professor WHERE last_name = %s"
            adr = self.teacherSearchName_var.get()

            val = cur.execute(sql, adr)
            if(not val):
                messagebox.showinfo("No", "Not availabe!")

            rows = cur.fetchall()
            if(len(rows)!=0):
                self.teachertree.delete(*self.teachertree.get_children())
                for row in rows:
                    self.teachertree.insert('', END, values=row)

                con.commit()
            con.close()

        elif len(self.teacherSearchName_var.get()) == 0:

            con = mysql.connector.connect(host="localhost", user="root", password="ctu1234", database="grades")
            cur = con.cursor()
         
            sql = "SELECT * FROM professor WHERE professor_ID = %s"
            adr = self.teacherSearchID_var.get()

            val = cur.execute(sql, adr)
            if(not val):
                messagebox.showinfo("No", "Not availabe!")

            rows = cur.fetchall()
            if(len(rows)!=0):
                self.teachertree.delete(*self.teachertree.get_children())
                for row in rows:
                    self.teachertree.insert('', END, values=row)

                con.commit()
            con.close()
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
            
    def find_student(self):
        window = tk.Toplevel(self)
                                    # gets last name entered in "Name" field
        
        con = mysql.connector.connect(host="localhost", user="root", password="ctu1234", database="grades")
        cur = con.cursor()
        cur.execute("select student_ID from student where last_name = %s", ('Ranz',) )
        for student in cur.fetchall():
            student_ID = student[0]

        # gets all courses that student is in
        cur.execute('''select c.course_ID from course c, enrollment e where
                                e.student_ID = %s and e.course_ID = c.course_ID
                                order by name asc''', (student_ID,))
        course_list = cur.fetchall()

        #for course in course_list:
        #	print(*course)

        i=0
        row=6
        column=1
        for course_ID in course_list:
            if course_ID == "":
                break

            cur.execute("select name from course where course_ID = %s", course_ID)
            course_name = cur.fetchone()
            
            tk.Label(window, text=course_name[0]).grid(row=(row + i), column=column)

            i+=1

            cur.execute('''select score, weight from gradebook 
                                    where student_ID = %s and course_ID = %s
                                    ''', (student_ID, course_ID[0]))
            allgrades = cur.fetchall()
            
            final_grade = 0
            for grade in allgrades:
                final_grade += grade[0] * grade[1]
                #for x in grade:
                #### grade[i] prints as a tuple not an int
            
            
            final_grade = final_grade / 100
            tk.Label(window, text=final_grade).grid(row=(row + 1), column=(column + 1))
            
    def display(self):
        window = tk.Toplevel(self)
        window.title("MARKSHEET")
        window.geometry("700x250")
    
        # set entry variables
        last_name = tk.StringVar()
        class1 = tk.StringVar()

        e1 = tk.Entry(window)
        e2 = tk.Entry(window)
        e3 = tk.Entry(window)
        #e4 = tk.Entry(window, textvariable=class1)
        e5 = tk.Entry(window)
        e6 = tk.Entry(window)
        e7 = tk.Entry(window)
        e8 = tk.Entry(window)
        # Variable to store total marks
        tot=0

        tk.Label(window, text=str(tot)).grid(row=9, column=4)
        tk.Label(window, text=str(tot/5)).grid(row=10, column=4)


        # label to enter name
        tk.Label(window, text="Name").grid(row=0, column=0)
        # label for registration number
        tk.Label(window, text="Reg.No").grid(row=0, column=3)
        # label for roll Number
        tk.Label(window, text="Roll.No").grid(row=1, column=0)


        # labels for subject codes
        tk.Label(window, text="Subject").grid(row=5, column=1)
        #tk.Label(window, text="Statistics").grid(row=3, column=1)
        #tk.Label(window, text="Biology").grid(row=4, column=1)
        #tk.Label(window, text="Physics").grid(row=5, column=1)
        #tk.Label(window, text="History").grid(row=6, column=1)
        #tk.Label(window, text="English").grid(row=7, column=1)

        # label for grades
        tk.Label(window, text="Grade").grid(row=5, column=2)
        #e4.grid(row=6, column=2)
        #e5.grid(row=7, column=2)
        #e6.grid(row=8, column=2)
        #e7.grid(row=9, column=2)
        #e8.grid(row=10, column=2)

        # labels for subject credits
        tk.Label(window, text="Sub Credit").grid(row=5, column=4)
        #tk.Label(window, text="4").grid(row=3, column=3)
        #tk.Label(window, text="4").grid(row=4, column=3)
        #tk.Label(window, text="3").grid(row=5, column=3)
        #tk.Label(window, text="4").grid(row=6, column=3)
        #tk.Label(window, text="4").grid(row=7, column=3)

        # Name age roll entries
        e1=tk.Entry(window, textvariable=last_name.get())
        e2=tk.Entry(window)
        e3=tk.Entry(window)

        # organizing them in the grid
        e1.grid(row=0, column=1)
        e2.grid(row=0, column=4)
        e3.grid(row=1, column=1)

        # button to display all the calculated credit scores and sgpa
        button1=tk.Button(window, text="submit", bg="green", command=self.display)
        button1.grid(row=16, column=1)
        button2 = tk.Button(window, text="Find", command=self.find_student)
        button2.grid(row=0,column=2)

        tk.Label(window, text="Total credits").grid(row=11, column=3)
        tk.Label(window, text="Student GPA").grid(row=12, column=3)
        
    def show_classes(self):
        window = tk.Toplevel(self)
        window.title("Class Selection")
        window.geometry("300x250")
        
        tk.Button(window, text="Math 150", command=grading.math_gradebook.main, width=10).place(x=115, y=10)
        tk.Button(window, text="Physics 110", width=10).place(x=115, y=40)
        tk.Button(window, text="Biology 103", width=10).place(x=115, y=70)
        tk.Button(window, text="History 101",width=10).place(x=115, y=100)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x200")
    root.title('Student Management System')
    Example(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
