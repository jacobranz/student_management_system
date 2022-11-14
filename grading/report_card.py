import tkinter as tk
import school_manage_home ## Importing file with database connection configuration

## Define functions
def Math_150():
	pass

def Physics_101():
	pass

def English_120():
	pass

def Music_100():
	pass

def find_student():

	total_creds = []
	# gets last name entered in "Name" field
	sql = "select student_ID from student where last_name = %s"
	adr = (last_name.get(),)
	
	school_manage_home.cursor.execute(sql, adr)
	for student in school_manage_home.cursor.fetchall():
		student_ID = student[0]

	# gets all courses that student is in
	school_manage_home.cursor.execute('''select c.course_ID from course c, enrollment e where
							e.student_ID = %s and e.course_ID = c.course_ID
							order by name asc''', (student_ID,))
	course_list = school_manage_home.cursor.fetchall()


	i=0
	row=6
	column=1
	for course_ID in course_list:
		if course_ID == "":
			break

		school_manage_home.cursor.execute("select name from course where course_ID = %s", course_ID)
		course_name = school_manage_home.cursor.fetchone()
		
		tk.Label(master, text=course_name[0]).grid(row=(row + i), column=column)

		school_manage_home.cursor.execute('''select score, weight from gradebook 
								where student_ID = %s and course_ID = %s
								''', (student_ID, course_ID[0]))
		allgrades = school_manage_home.cursor.fetchall()
		
		final_grade = 0
		for grade in allgrades:
			final_grade += grade[0] * grade[1]
		
		final_grade = final_grade / 100
		tk.Label(master, text=final_grade).grid(row=(row + i), column=(column + 1))

		## get credit count for each course
		school_manage_home.cursor.execute("select creds from course where course_ID = %s", course_ID)
		credit_count = school_manage_home.cursor.fetchall()
		for creds in credit_count:
			tk.Label(master, text=creds).grid(row=(row + i), column=4)
			total_creds.append(creds)

		## go to button next to each class
		## ability to manage students from there
		button_command = eval(course_name[0].replace(' ','_'))
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
class1 = tk.StringVar()

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

