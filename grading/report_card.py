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

	def gradebook(self):
		## Begin GUI
		master = tk.Tk()
		master.title("Grade Book")
		master.geometry("700x250")

		# set entry variables
		last_name = tk.StringVar()
		class1 = tk.StringVar()

		# label to enter name
		tk.Label(master, text="Student Last Name").grid(row=0, column=0)

		# labels for subject codes
		tk.Label(master, text="Subject").grid(row=1, column=0)

		tk.Label(master, text="Grade").grid(row=1, column=1)
		grade0 = tk.IntVar()
		grade1 = tk.IntVar()
		grade2 = tk.IntVar()
		grade3 = tk.IntVar()
		grades = [grade0, grade1, grade2, grade3]

		tk.Label(master, text="Weight").grid(row=1, column=2)
		weight0 = tk.IntVar()
		weight1 = tk.IntVar()
		weight2 = tk.IntVar()
		weight3 = tk.IntVar()
		weights = [weight0, weight1, weight2, weight3]

		# Name age roll entries
		e1=tk.Entry(master, textvariable=last_name)

		# organizing them in the grid
		e1.grid(row=0, column=1)

		# button to display all the calculated credit scores and sgpa
		find_button = tk.Button(master, text="Find", command=self.find_student)
		find_button.grid(row=0,column=2)
		submit_button = tk.Button(master, text="Submit", command=self.submit_grades).grid(row=13, column=0)


		master.mainloop()

	def find_student(self):

		sql = "select student_ID from student where last_name = %s"
		adr = (last_name.get(),)

		cursor.execute(sql, adr)
		for student in cursor.fetchall():
			student_ID = student[0]
		# gets all courses that student is in
		cursor.execute('''select gradebook.assignment from gradebook where
											gradebook.student_ID = %s and gradebook.course_ID = 2''', (student_ID,))
		assignment_list = cursor.fetchall()
		

		i=0
		row=6
		column=0
		for assignment in assignment_list:
			if assignment == "":
				break
			
			tk.Label(master, text=assignment[0]).grid(row=(row + i), column=column)
			#grades.append(tk.IntVar())
			#entries.append(tk.Entry(master, textvariable=grades[i], width=5).grid(row=(row + i), column=1))
			#print(grades[i])
			#for i in range(4):
				#globals()[f'grade{i}'] = tk.IntVar()
			tk.Entry(master, textvariable=eval(f'grade{i}'), width=5).grid(row=(row + i), column=1)

			i+=1

	def submit_grades(self):

		cursor.execute("select student_ID from student where last_name = %s", (last_name.get(),))
		for student in cursor.fetchall():
			student_ID = student[0]

		cursor.execute('''select gradebook.assignment from gradebook where
											gradebook.student_ID = %s and gradebook.course_ID = 2''', (student_ID,))
		assignment_list = cursor.fetchall()
		assignment0 = assignment_list[0]
		assignment1 = assignment_list[1]
		assignment2 = assignment_list[2]
		assignment3 = assignment_list[3]

		i = 0
		for grade in self.grades:
			cursor.execute('''update gradebook set score = %s where
								assignment = %s and student_ID = %s and course_ID = 2''', (grade.get(), eval(f'assignment{i}[0]'), student_ID))
			mydb.commit()
			i+=1
		mydb.close()

	entries = []

class Physics_101():
	def gradebook(self):
		## Begin GUI
		master = tk.Tk()
		master.title("Grade Book")
		master.geometry("700x250")

		# set entry variables
		last_name = tk.StringVar()
		class1 = tk.StringVar()

		# label to enter name
		tk.Label(master, text="Student Last Name").grid(row=0, column=0)

		# labels for subject codes
		tk.Label(master, text="Subject").grid(row=1, column=0)

		tk.Label(master, text="Grade").grid(row=1, column=1)
		grade0 = tk.IntVar()
		grade1 = tk.IntVar()
		grade2 = tk.IntVar()
		grade3 = tk.IntVar()
		grades = [grade0, grade1, grade2, grade3]

		tk.Label(master, text="Weight").grid(row=1, column=2)
		weight0 = tk.IntVar()
		weight1 = tk.IntVar()
		weight2 = tk.IntVar()
		weight3 = tk.IntVar()
		weights = [weight0, weight1, weight2, weight3]

		# Name age roll entries
		e1=tk.Entry(master, textvariable=last_name)

		# organizing them in the grid
		e1.grid(row=0, column=1)

		# button to display all the calculated credit scores and sgpa
		find_button = tk.Button(master, text="Find", command=self.find_student)
		find_button.grid(row=0,column=2)
		submit_button = tk.Button(master, text="Submit", command=self.submit_grades).grid(row=13, column=0)


		master.mainloop()


class English_120():
	def gradebook(self):
		## Begin GUI
		master = tk.Tk()
		master.title("Grade Book")
		master.geometry("700x250")

		# set entry variables
		last_name = tk.StringVar()
		class1 = tk.StringVar()

		# label to enter name
		tk.Label(master, text="Student Last Name").grid(row=0, column=0)

		# labels for subject codes
		tk.Label(master, text="Subject").grid(row=1, column=0)

		tk.Label(master, text="Grade").grid(row=1, column=1)
		grade0 = tk.IntVar()
		grade1 = tk.IntVar()
		grade2 = tk.IntVar()
		grade3 = tk.IntVar()
		grades = [grade0, grade1, grade2, grade3]

		tk.Label(master, text="Weight").grid(row=1, column=2)
		weight0 = tk.IntVar()
		weight1 = tk.IntVar()
		weight2 = tk.IntVar()
		weight3 = tk.IntVar()
		weights = [weight0, weight1, weight2, weight3]

		# Name age roll entries
		e1=tk.Entry(master, textvariable=last_name)

		# organizing them in the grid
		e1.grid(row=0, column=1)

		# button to display all the calculated credit scores and sgpa
		find_button = tk.Button(master, text="Find", command=self.find_student)
		find_button.grid(row=0,column=2)
		submit_button = tk.Button(master, text="Submit", command=self.submit_grades).grid(row=13, column=0)


		master.mainloop()


class Music_100():
	def gradebook(self):
		## Begin GUI
		master = tk.Tk()
		master.title("Grade Book")
		master.geometry("700x250")

		# set entry variables
		last_name = tk.StringVar()
		class1 = tk.StringVar()

		# label to enter name
		tk.Label(master, text="Student Last Name").grid(row=0, column=0)

		# labels for subject codes
		tk.Label(master, text="Subject").grid(row=1, column=0)

		tk.Label(master, text="Grade").grid(row=1, column=1)
		grade0 = tk.IntVar()
		grade1 = tk.IntVar()
		grade2 = tk.IntVar()
		grade3 = tk.IntVar()
		grades = [grade0, grade1, grade2, grade3]

		tk.Label(master, text="Weight").grid(row=1, column=2)
		weight0 = tk.IntVar()
		weight1 = tk.IntVar()
		weight2 = tk.IntVar()
		weight3 = tk.IntVar()
		weights = [weight0, weight1, weight2, weight3]

		# Name age roll entries
		e1=tk.Entry(master, textvariable=last_name)

		# organizing them in the grid
		e1.grid(row=0, column=1)

		# button to display all the calculated credit scores and sgpa
		find_button = tk.Button(master, text="Find", command=self.find_student)
		find_button.grid(row=0,column=2)
		submit_button = tk.Button(master, text="Submit", command=self.submit_grades).grid(row=13, column=0)


		master.mainloop()


def find_student():

	total_creds = []
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
		for grade in allgrades:
			final_grade += grade[0] * grade[1]
		
		final_grade = final_grade / 100
		tk.Label(master, text=final_grade).grid(row=(row + i), column=(column + 1))

		## get credit count for each course
		cursor.execute("select creds from course where course_ID = %s", course_ID)
		credit_count = cursor.fetchall()
		for creds in credit_count:
			tk.Label(master, text=creds).grid(row=(row + i), column=4)
			total_creds.append(creds)

		## go to button next to each class
		## ability to manage students from there
		button_command = eval(course_name[0].replace(' ','_') + '().gradebook')
		tk.Button(master, text=course_name[0], command=button_command).grid(row=(row + i), column=0)

		i+=1
	
	## get total credential count of student
	total = 0
	for cred in total_creds:
		total += cred[0]
	tk.Label(master, text=total).grid(row=11,column=4)

	## calculate student GPA
	gpa = total / len(total_creds)
	tk.Label(master, text=gpa).grid(row=12, column=4)
			


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

