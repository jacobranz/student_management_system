import tkinter as tk
from tkinter import *
import mysql.connector
from tkinter import messagebox

class smgmt:
    
    def __init__(self):
        root = tk.Tk()
        root.geometry("450x300")
        root.title('Student Management System')

        #self.id_var = StringVar()
        #self.last = StringVar()

        self.display = tk.Label(root, text = "First Name").place(x=40, y=60)
        #self.display.pack()
        #self.display.place(relx = 0.3, rely = 0.6 ,anchor = 'center')

        self.last_name = tk.Label(root, text = "Last Name").place(x=40, y=80)
        #self.last_name.pack()
        #self.last_name.place(relx = 0.4, rely = 0.7,anchor = 'center')

        self.button = tk.Button(root, text='Write to Database', command=self.write).place(x=75, y=130)
        #self.button.pack()
        #self.button.place(relx = 0.5, rely = 0.8, anchor = 'center')

        id_entry = tk.Entry(root, width=30).place(x=110,y=60)
        #id_entry.pack()
        #id_entry.place(relx = 0.5, rely = 0.6, anchor = 'center')

        last_entry = tk.Entry(root, width=30).place(x=110, y=80)
        #last_entry.pack()
        #last_entry.place(relx = 0.5, rely = 0.7, anchor = 'center')
        
        #self.button.config(state = tk.ACTIVE)

        root.mainloop()

    def write(self):
        pass
    #    con = pymysql.connect(host="localhost", user="root", password="ctu1234", database="batman")
    #    cur = con.cursor()
    #    cur.execute("insert into students values(%s, %s)", (self.id_var.get(), self.last.get()))
    #    con.commit()
    #    con.close()
    #    messagebox.showinfo("Successfull", "Record has been inserted.")
        
smgmt()
