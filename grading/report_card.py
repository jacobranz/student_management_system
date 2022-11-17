import tkinter as tk
import mysql.connector

## Define functions
mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "ctu1234",
    database = "grades"
)

cursor = mydb.cursor()

class Math_150():
	pass

class Physics_101():
	pass


class English_120():
	pass


class Music_100():
	pass


def find_student():

	total_creds = []
	total_gpa = []
	# gets last name entered in "Name" field
	sql = "select student_ID from student where last_name = %s"
	adr = (last_name.get(),)
	
	cursor.execute(sql, adr)
	for student in cursor.fetchall():
		student_ID = student[0]

	# gets all courses that student is in
	cursor.execute('''select c.course_ID from course c, enrollment e where
							e.student_ID = %s and e.course_ID = c.course_ID
							order by name asc''', (student_ID,))
	course_list = cursor.fetchall()

	i=0
	row=6
	column=1
	for course_ID in course_list:
		if course_ID == "":
			break

		cursor.execute("select name from course where course_ID = %s", course_ID)
		course_name = cursor.fetchone()
		
		tk.Label(master, text=course_name[0]).grid(row=(row + i), column=column)

		cursor.execute('''select score, weight from gradebook 
								where student_ID = %s and course_ID = %s
								''', (student_ID, course_ID[0]))
		allgrades = cursor.fetchall()
		
		final_grade = 0
		creds_earned = 0
		for grade in allgrades:
			final_grade += grade[0] * grade[1]

		final_grade = final_grade / 100

		if final_grade >= 90:
			creds_earned += 4
		if 80 <= final_grade <= 89.9:
			creds_earned += 3
		if 70 <= final_grade <= 79.9:
			creds_earned += 2
		if 60 <= final_grade <= 69.9:
			creds_earned += 1
		else:
			creds_earned += 0

		gpa = creds_earned / len(course_list)
		total_gpa.append(gpa)

		tk.Label(master, text=final_grade).grid(row=(row + i), column=(column + 1))

		## get credit count for each course
		cursor.execute("select creds from course where course_ID = %s", course_ID)
		credit_count = cursor.fetchall()
		for creds in credit_count:
			tk.Label(master, text=creds).grid(row=(row + i), column=4)
			total_creds.append(creds)

		## go to button next to each class
		## ability to manage students from there
		button_command = eval(course_name[0].replace(' ','_'))
		tk.Button(master, text=course_name[0], command=button_command).grid(row=(row + i), column=0)

		i+=1
	
	## get amount of earned creds from student
	total = 0
	for cred in total_creds:
		total += cred[0]
		
	tk.Label(master, text=total).grid(row=11,column=4)

	## calculate student GPA
	total_student_gpa = 0
	for gpa in total_gpa:
		total_student_gpa += gpa

	tk.Label(master, text=total_student_gpa).grid(row=12, column=4)
			


## Begin GUI
master = tk.Tk()
master.title("MARKSHEET")
master.geometry("700x250")

# set entry variables
last_name = tk.StringVar()

# label to enter name
tk.Label(master, text="Name").grid(row=0, column=0)

# labels for subject codes
tk.Label(master, text="Subject").grid(row=5, column=1)

# label for grades
tk.Label(master, text="Grade").grid(row=5, column=2)

# labels for subject credits
tk.Label(master, text="Sub Credit").grid(row=5, column=4)

# label for course management
tk.Label(master, text="Manage Course").grid(row=5, column=0)

# Name age roll entries
e1=tk.Entry(master, textvariable=last_name)

# organizing them in the grid
e1.grid(row=0, column=1)

# button to display all the calculated credit scores and sgpa
find_button = tk.Button(master, text="Find", command=find_student)
find_button.grid(row=0,column=2)

tk.Label(master, text="Total credits").grid(row=11, column=3)
tk.Label(master, text="Student GPA").grid(row=12, column=3)

master.mainloop()

