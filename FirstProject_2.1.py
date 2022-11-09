from tkinter import ttk
import tkinter as tk
from tkinter import *
import pymysql
from tkinter import messagebox

class Example(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        b1 = tk.Button(self, text="Student", command = self.studentWindow)
        b1.pack(side="left",anchor='n', padx=40, pady=10)

        b2 = tk.Button(self, text="Teacher", command = self.teacherWindow)
        b2.pack(side="left",anchor='n', padx=40, pady=10)

        b3 = tk.Button(self, text="Class", command = self.sectionWindow)
        b3.pack(side="left",anchor='n', padx=40, pady=10)
      
    def studentWindow(self):
        window = tk.Toplevel(self)
        window.geometry("%dx%d%+d%+d" % (1300, 550, 10, 10))
        window.grid_columnconfigure((0,1), weight=1)

        self.studentID_var = StringVar()
        self.studentFirstName_var = StringVar()
        self.studentLastName_var = StringVar()
        self.studentAge_var = StringVar()
        self.studentGradeLevel_var = StringVar()
        self.studentSearchID_var = StringVar()
        self.studentSearchName_var = StringVar()
        
        Student_Label_1 = tk.Label(window, text="Student ID")
        Student_Label_2 = tk.Label(window, text="Student First Name")
        Student_Label_3 = tk.Label(window, text="Student Last Name")
        Student_Label_4 = tk.Label(window, text="Age")
        Student_Label_5 = tk.Label(window, text="Grade Level")
        Student_Label_6 = tk.Label(window, text="Search By ID")
        Student_Label_7 = tk.Label(window, text="Search By Name")
        Student_Label_8 = tk.Label(window, text="_____________________________")
      
        Student_Entry_1 = tk.Entry(window, textvariable = self.studentID_var)
        Student_Entry_2 = tk.Entry(window, textvariable = self.studentFirstName_var)
        Student_Entry_3 = tk.Entry(window, textvariable = self.studentLastName_var)
        Student_Entry_4 = tk.Entry(window, textvariable = self.studentAge_var)
        Student_Entry_5 = tk.Entry(window, textvariable = self.studentGradeLevel_var)
        Student_Entry_6 = tk.Entry(window, textvariable = self.studentSearchID_var)
        Student_Entry_7 = tk.Entry(window, textvariable = self.studentSearchName_var)
        
        buttons_student_write = tk.Button(window, command= self.studentwrite)
        buttons_student_search = tk.Button(window, command= self.readdatastudent)

        Student_Label_1.grid(row=3, column=0)
        Student_Entry_1.grid(row=3, column=1, sticky="ew")
        Student_Label_2.grid(row=4, column=0)
        Student_Entry_2.grid(row=4, column=1, sticky="ew")
        Student_Label_3.grid(row=5, column=0)
        Student_Entry_3.grid(row=5, column=1, sticky="ew")
        Student_Label_4.grid(row=6, column=0)
        Student_Entry_4.grid(row=6, column=1, sticky="ew")
        Student_Label_5.grid(row=7, column=0)
        Student_Entry_5.grid(row=7, column=1, sticky="ew")
        buttons_student_write.grid(row=8, column=1)
        buttons_student_write.configure(text="Write to Database")

        Student_Label_8.grid(row=11, column=0)

        Student_Label_6.grid(row=13, column=0)
        Student_Entry_6.grid(row=13, column=1, sticky="ew")
        Student_Label_7.grid(row=14, column=0)
        Student_Entry_7.grid(row=14, column=1, sticky="ew")        
        buttons_student_search.grid(row=15, column=1, sticky="ew")
        buttons_student_search.configure(text="Search Database")

        self.studenttree = ttk.Treeview(window, columns=("ID", "FirstName","LastName","Age","Year"))
        self.studenttree.grid(row=15, column=0)
        self.studenttree.heading("ID", text="ID")
        self.studenttree.heading("FirstName", text="First Name")
        self.studenttree.heading("LastName", text=" Last Name")
        self.studenttree.heading("Age", text="Age")
        self.studenttree.heading("Year", text="Year")
        self.studenttree['show']='headings' # removing extra index col at begining
        

    def teacherWindow(self):
        window = tk.Toplevel(self)
        window.geometry("%dx%d%+d%+d" % (1500, 550, 10, 10))
        window.grid_columnconfigure((0,1), weight=1)

        self.teacherID_var = StringVar()
        self.teacherFirstName_var = StringVar()
        self.teacherLastName_var = StringVar()
        self.teacherAge_var = StringVar()
        self.teacherQual_var = StringVar()
        self.teacherStart_var = StringVar()
        self.teacherSearchID_var = StringVar()
        self.teacherSearchName_var = StringVar()

        Teacher_Label_1 = tk.Label(window, text="Teacher ID")
        Teacher_Label_2 = tk.Label(window, text="Teacher First Name")
        Teacher_Label_3 = tk.Label(window, text="Teacher Last Name")
        Teacher_Label_4 = tk.Label(window, text="Teacher Age")
        Teacher_Label_5 = tk.Label(window, text="Teacher Qualifications")
        Teacher_Label_6 = tk.Label(window, text="Teacher Start Date")
        Teacher_Label_7 = tk.Label(window, text="Search By ID")
        Teacher_Label_8 = tk.Label(window, text="Search By Name")
        Teacher_Label_9 = tk.Label(window, text="_____________________________")
  
        
        Teacher_Entry_1 = tk.Entry(window, textvariable = self.teacherID_var)
        Teacher_Entry_2 = tk.Entry(window, textvariable = self.teacherFirstName_var)
        Teacher_Entry_3 = tk.Entry(window, textvariable = self.teacherLastName_var)
        Teacher_Entry_4 = tk.Entry(window, textvariable = self.teacherAge_var)
        Teacher_Entry_5 = tk.Entry(window, textvariable = self.teacherQual_var)
        Teacher_Entry_6 = tk.Entry(window, textvariable = self.teacherStart_var)
        Teacher_Entry_7 = tk.Entry(window, textvariable = self.teacherSearchID_var)
        Teacher_Entry_8 = tk.Entry(window, textvariable = self.teacherSearchName_var)
        
        buttons_Teacher_write = tk.Button(window, command= self.teacherwrite)
        buttons_Teacher_search = tk.Button(window, command= self.readdatateacher)

        Teacher_Label_1.grid(row=3, column=0)
        Teacher_Entry_1.grid(row=3, column=1, sticky="ew")
        Teacher_Label_2.grid(row=4, column=0)
        Teacher_Entry_2.grid(row=4, column=1, sticky="ew")
        Teacher_Label_3.grid(row=5, column=0)
        Teacher_Entry_3.grid(row=5, column=1, sticky="ew")
        Teacher_Label_4.grid(row=6, column=0)
        Teacher_Entry_4.grid(row=6, column=1, sticky="ew")
        Teacher_Label_5.grid(row=7, column=0)
        Teacher_Entry_5.grid(row=7, column=1, sticky="ew")
        Teacher_Label_6.grid(row=8, column=0)
        Teacher_Entry_6.grid(row=8, column=1, sticky="ew")
        buttons_Teacher_write.grid(row=9, column=1)
        buttons_Teacher_write.configure(text="Write to Database")

        Teacher_Label_9.grid(row=11, column=0)
        Teacher_Label_7.grid(row=12, column=0)
        Teacher_Entry_7.grid(row=12, column=1, sticky="ew")
        Teacher_Label_8.grid(row=13, column=0)
        Teacher_Entry_8.grid(row=13, column=1, sticky="ew")
        buttons_Teacher_search.grid(row=14, column=1)
        buttons_Teacher_search.configure(text="Search Database")

        self.teachertree = ttk.Treeview(window, columns=("ID", "FirstName","LastName", "Age", "Qualifications", "StartDate"))
        self.teachertree.grid(row=15, column=0)
        self.teachertree.heading("ID", text="ID")
        self.teachertree.heading("FirstName", text="First Name")
        self.teachertree.heading("LastName", text="Last Name")
        self.teachertree.heading("Age", text="Age")
        self.teachertree.heading("Qualifications", text="Qualifications")
        self.teachertree.heading("StartDate", text="Start Date")
        self.teachertree['show']='headings' # removing extra index col at begining
      
    def sectionWindow(self):
        window = tk.Toplevel(self)
        window.geometry("%dx%d%+d%+d" % (1300, 550, 10, 10))
        window.grid_columnconfigure((0,1), weight=1)

        self.sectionID_var = StringVar()
        self.sectionName_var = StringVar()
        self.sectionCreds_var = StringVar()
        self.sectionProf_var = StringVar()
        self.sectionSearchID_var = StringVar()
        self.sectionSearchName_var = StringVar()

        Section_Label_1 = tk.Label(window, text="Section ID")
        Section_Label_2 = tk.Label(window, text="Section Name")
        Section_Label_3 = tk.Label(window, text="Section Creds")
        Section_Label_4 = tk.Label(window, text="Section Professor")
        Section_Label_5 = tk.Label(window, text="Search By ID")
        Section_Label_6 = tk.Label(window, text="Search By Name")
        Section_Label_7 = tk.Label(window, text="_____________________________")
                      
        Section_Entry_1 = tk.Entry(window, textvariable = self.sectionID_var)
        Section_Entry_2 = tk.Entry(window, textvariable = self.sectionName_var)
        Section_Entry_3 = tk.Entry(window, textvariable = self.sectionCreds_var)
        Section_Entry_4 = tk.Entry(window, textvariable = self.sectionProf_var)
        Section_Entry_5 = tk.Entry(window, textvariable = self.sectionSearchID_var)
        Section_Entry_6 = tk.Entry(window, textvariable = self.sectionSearchName_var)
        
        buttons_Section_write = tk.Button(window, command= self.sectionwrite)
        buttons_Section_search = tk.Button(window, command= self.readdataclass)

        Section_Label_1.grid(row=3, column=0)
        Section_Entry_1.grid(row=3, column=1, sticky="ew")
        Section_Label_2.grid(row=4, column=0)
        Section_Entry_2.grid(row=4, column=1, sticky="ew")
        Section_Label_3.grid(row=5, column=0)
        Section_Entry_3.grid(row=5, column=1, sticky="ew")
        Section_Label_4.grid(row=6, column=0)
        Section_Entry_4.grid(row=6, column=1, sticky="ew")
        buttons_Section_write.grid(row=8, column=1)
        buttons_Section_write.configure(text="Write to Database")

        Section_Label_7.grid(row=11, column=0)
        Section_Label_5.grid(row=12, column=0)
        Section_Entry_5.grid(row=12, column=1, sticky="ew")
        Section_Label_6.grid(row=13, column=0)
        Section_Entry_6.grid(row=13, column=1, sticky="ew")
        buttons_Section_search.grid(row=14, column=1)
        buttons_Section_search.configure(text="Search Database")

        self.sectiontree = ttk.Treeview(window, columns=("ID", "Name","Creds","Prof"))
        self.sectiontree.grid(row=15, column=0)
        self.sectiontree.heading("ID", text="ID")
        self.sectiontree.heading("Name", text="Name")
        self.sectiontree.heading("Creds", text="Creds")
        self.sectiontree.heading("Prof", text="Professor")
        self.sectiontree['show']='headings' # removing extra index col at begining

    def sectionwrite(self):
        con = pymysql.connect(host="localhost", user="root", password="ctu1234", database="grades")
        cur = con.cursor()
        cur.execute("insert into course values(%s, %s, %s, %s)", (self.sectionID_var.get(), self.sectionName_var.get(), self.sectionCreds_var.get(), self.sectionProf_var.get()))
        con.commit()
        con.close()
        messagebox.showinfo("Successfull", "Record has been inserted.")

    def studentwrite(self):
        con = pymysql.connect(host="localhost", user="root", password="ctu1234", database="grades")
        cur = con.cursor()
        cur.execute("insert into student values(%s, %s, %s, %s, %s)", (self.studentID_var.get(), self.studentFirstName_var.get(), self.studentLastName_var.get(), self.studentAge_var.get(), self.studentGradeLevel_var.get()))
        con.commit()
        con.close()
        messagebox.showinfo("Successfull", "Record has been inserted.")

    def teacherwrite(self):
        con = pymysql.connect(host="localhost", user="root", password="ctu1234", database="grades")
        cur = con.cursor()
        cur.execute("insert into professor values(%s, %s, %s, %s, %s, %s)", (self.teacherID_var.get(), self.teacherFirstName_var.get(), self.teacherLastName_var.get(), self.teacherAge_var.get(), self.teacherQual_var.get(), self.teacherStart_var.get()))
        con.commit()
        con.close()
        messagebox.showinfo("Successfull", "Record has been inserted.")

            
    def readdatastudent(self):

        con = pymysql.connect(host="localhost", user="root", password="ctu1234", database="grades")
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

    def readdatateacher(self):
            
        con = pymysql.connect(host="localhost", user="root", password="ctu1234", database="grades")
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

    def readdataclass(self):
            
        con = pymysql.connect(host="localhost", user="root", password="ctu1234", database="grades")
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

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x200")
    root.title('Student Management System')
    Example(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
