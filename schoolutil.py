from tkinter import ttk
import tkinter as tk
from tkinter import *
#import pymysql
import mysql.connector
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
        self.studentName_var = StringVar()
        self.studentAge_var = StringVar()
        self.studentGradeLevel_var = StringVar()
        self.studentSearchID_var = StringVar()
        self.studentSearchName_var = StringVar()
        
        Student_Label_1 = tk.Label(window, text="Student ID")
        Student_Label_2 = tk.Label(window, text="Student Name")
        Student_Label_3 = tk.Label(window, text="Age")
        Student_Label_4 = tk.Label(window, text="Grade Level")
        Student_Label_5 = tk.Label(window, text="Search By ID")
        Student_Label_6 = tk.Label(window, text="Search By Name")
        Student_Label_7 = tk.Label(window, text="_____________________________")
      
        Student_Entry_1 = tk.Entry(window, textvariable = self.studentID_var)
        Student_Entry_2 = tk.Entry(window, textvariable = self.studentName_var)
        Student_Entry_3 = tk.Entry(window, textvariable = self.studentAge_var)
        Student_Entry_4 = tk.Entry(window, textvariable = self.studentGradeLevel_var)
        Student_Entry_5 = tk.Entry(window, textvariable = self.studentSearchID_var)
        Student_Entry_6 = tk.Entry(window, textvariable = self.studentSearchName_var)
        
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
        buttons_student_write.grid(row=8, column=1)
        buttons_student_write.configure(text="Write to Database")

        Student_Label_7.grid(row=11, column=0)
        Student_Label_5.grid(row=12, column=0)
        Student_Entry_5.grid(row=12, column=1, sticky="ew")
        Student_Label_6.grid(row=13, column=0)
        Student_Entry_6.grid(row=13, column=1, sticky="ew")
        buttons_student_search.grid(row=14, column=1, sticky="ew")
        buttons_student_search.configure(text="Search Database")

        self.studenttree = ttk.Treeview(window, columns=("ID", "Name","Age","Year"))
        self.studenttree.grid(row=15, column=0)
        self.studenttree.heading("ID", text="ID")
        self.studenttree.heading("Name", text="Name")
        self.studenttree.heading("Age", text="Age")
        self.studenttree.heading("Year", text="Year")
        self.studenttree['show']='headings' # removing extra index col at begining
        

    def teacherWindow(self):
        window = tk.Toplevel(self)
        window.geometry("%dx%d%+d%+d" % (1300, 550, 10, 10))
        window.grid_columnconfigure((0,1), weight=1)

        self.teacherID_var = StringVar()
        self.teacherName_var = StringVar()
        self.teacherSubject_var = StringVar()
        self.teacherContact_var = StringVar()
        self.teacherSearchID_var = StringVar()
        self.teacherSearchName_var = StringVar()

        Teacher_Label_1 = tk.Label(window, text="Teacher ID")
        Teacher_Label_2 = tk.Label(window, text="Teacher Name")
        Teacher_Label_3 = tk.Label(window, text="Teacher Subject")
        Teacher_Label_4 = tk.Label(window, text="Teacher Contact")
        Teacher_Label_5 = tk.Label(window, text="Search By ID")
        Teacher_Label_6 = tk.Label(window, text="Search By Name")
        Teacher_Label_7 = tk.Label(window, text="_____________________________")
  
        
        Teacher_Entry_1 = tk.Entry(window, textvariable = self.teacherID_var)
        Teacher_Entry_2 = tk.Entry(window, textvariable = self.teacherName_var)
        Teacher_Entry_3 = tk.Entry(window, textvariable = self.teacherSubject_var)
        Teacher_Entry_4 = tk.Entry(window, textvariable = self.teacherContact_var)
        Teacher_Entry_5 = tk.Entry(window, textvariable = self.teacherSearchID_var)
        Teacher_Entry_6 = tk.Entry(window, textvariable = self.teacherContact_var)
        
        buttons_Teacher_write = tk.Button(window, command= self.teacherwrite)
        buttons_Teacher_search = tk.Button(window, command= self.teacherwrite)

        Teacher_Label_1.grid(row=3, column=0)
        Teacher_Entry_1.grid(row=3, column=1, sticky="ew")
        Teacher_Label_2.grid(row=4, column=0)
        Teacher_Entry_2.grid(row=4, column=1, sticky="ew")
        Teacher_Label_3.grid(row=5, column=0)
        Teacher_Entry_3.grid(row=5, column=1, sticky="ew")
        Teacher_Label_4.grid(row=6, column=0)
        Teacher_Entry_4.grid(row=6, column=1, sticky="ew")
        buttons_Teacher_write.grid(row=8, column=1)
        buttons_Teacher_write.configure(text="Write to Database")

        Teacher_Label_7.grid(row=11, column=0)
        Teacher_Label_5.grid(row=12, column=0)
        Teacher_Entry_5.grid(row=12, column=1, sticky="ew")
        Teacher_Label_6.grid(row=13, column=0)
        Teacher_Entry_6.grid(row=13, column=1, sticky="ew")
        buttons_Teacher_search.grid(row=14, column=1)
        buttons_Teacher_search.configure(text="Search Database")

        self.teachertree = ttk.Treeview(window, columns=("ID", "Name","Age","Year"))
        self.teachertree.grid(row=15, column=0)
        self.teachertree.heading("ID", text="ID")
        self.teachertree.heading("Name", text="Name")
        self.teachertree.heading("Age", text="Age")
        self.teachertree.heading("Year", text="Year")
        self.teachertree['show']='headings' # removing extra index col at begining
      
    def sectionWindow(self):
        window = tk.Toplevel(self)
        window.geometry("%dx%d%+d%+d" % (1300, 550, 10, 10))
        window.grid_columnconfigure((0,1), weight=1)

        self.sectionID_var = StringVar()
        self.sectionName_var = StringVar()
        self.sectionDescription_var = StringVar()
        self.sectionSubject_var = StringVar()
        self.sectionSearchID_var = StringVar()
        self.sectionSearchName_var = StringVar()

        Section_Label_1 = tk.Label(window, text="Section ID")
        Section_Label_2 = tk.Label(window, text="Section Name")
        Section_Label_3 = tk.Label(window, text="Section Description")
        Section_Label_4 = tk.Label(window, text="Section Subject")
        Section_Label_5 = tk.Label(window, text="Search By ID")
        Section_Label_6 = tk.Label(window, text="Search By Name")
        Section_Label_7 = tk.Label(window, text="_____________________________")
                      
        Section_Entry_1 = tk.Entry(window, textvariable = self.sectionID_var)
        Section_Entry_2 = tk.Entry(window, textvariable = self.sectionName_var)
        Section_Entry_3 = tk.Entry(window, textvariable = self.sectionDescription_var)
        Section_Entry_4 = tk.Entry(window, textvariable = self.sectionSubject_var)
        Section_Entry_5 = tk.Entry(window, textvariable = self.sectionSearchID_var)
        Section_Entry_6 = tk.Entry(window, textvariable = self.sectionSearchName_var)
        
        buttons_Section_write = tk.Button(window, command= self.sectionwrite)
        buttons_Section_search = tk.Button(window, command= self.sectionwrite)

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

        self.sectiontree = ttk.Treeview(window, columns=("ID", "Name","Age","Year"))
        self.sectiontree.grid(row=15, column=0)
        self.sectiontree.heading("ID", text="ID")
        self.sectiontree.heading("Name", text="Name")
        self.sectiontree.heading("Age", text="Age")
        self.sectiontree.heading("Year", text="Year")
        self.sectiontree['show']='headings' # removing extra index col at begining

    def sectionwrite(self):
        con = pymysql.connect(host="localhost", user="root", password="ctu1234", database="sections")
        cur = con.cursor()
        cur.execute("insert into sections values(%s, %s, %s, %s)", (self.sectionID_var.get(), self.sectionName_var.get(), self.sectionDescription_var.get(), self.sectionSubject_var.get()))
        con.commit()
        con.close()
        messagebox.showinfo("Successfull", "Record has been inserted.")

    def studentwrite(self):
        con = pymysql.connect(host="localhost", user="root", password="ctu1234", database="sections")
        cur = con.cursor()
        cur.execute("insert into students values(%s, %s, %s, %s)", (self.studentID_var.get(), self.studentName_var.get(), self.studentAge_var.get(), self.studentGradeLevel_var.get()))
        con.commit()
        con.close()
        messagebox.showinfo("Successfull", "Record has been inserted.")

    def teacherwrite(self):
        con = pymysql.connect(host="localhost", user="root", password="ctu1234", database="sections")
        cur = con.cursor()
        cur.execute("insert into teacher values(%s, %s, %s, %s)", (self.teacherID_var.get(), self.teacherName_var.get(), self.teacherSubject_var.get(), self.teacherContact_var.get()))
        con.commit()
        con.close()
        messagebox.showinfo("Successfull", "Record has been inserted.")

            
    def readdatastudent(self):

        con = pymysql.connect(host="localhost", user="root", password="ctu1234", database="sections")
        cur = con.cursor()
     
        sql = "SELECT * FROM students WHERE idstudents = %s"
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
            

        pass
        #copy, paste and repeat code from readdatastudent()

    def readdataclass(self):
            

        pass
        #copy, paste and repeat code from readdatastudent()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x200")
    root.title('Student Management System')
    Example(root).pack(side="top", fill="both", expand=True)
    root.mainloop()