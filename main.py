# File that includes all the code written
import mysql.connector
import customtkinter as ctk

from views.page_container import PageContainer

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "ctu1234",
    database = "grades"
)

cursor = mydb.cursor()

if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("800x300")
    root.title("STUDENT MANAGEMENT SYSTEM")
    PageContainer(root).pack(side="top", fill="both", expand=True)
    root.mainloop()