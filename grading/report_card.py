import tkinter as tk
import school_manage_home ## Importing file with database connection configuration

## Define functions
def find_student():
	# gets last name entered in "Name" field
	school_manage_home.cursor.execute("select student_ID from student where last_name = %s", ('Ranz',) )
	for student in school_manage_home.cursor.fetchall():
		student_ID = student[0]

	# gets all courses that student is in
	school_manage_home.cursor.execute('''select c.course_ID from course c, enrollment e where
							e.student_ID = %s and e.course_ID = c.course_ID
							order by name asc''', (student_ID,))
	course_list = school_manage_home.cursor.fetchall()

	#for course in course_list:
	#	print(*course)

	i=0
	row=6
	column=1
	for course_ID in course_list:
		if course_ID == "":
			break

		school_manage_home.cursor.execute("select name from course where course_ID = %s", course_ID)
		course_name = school_manage_home.cursor.fetchone()
		
		tk.Label(master, text=course_name[0]).grid(row=(row + i), column=column)

		i+=1

		school_manage_home.cursor.execute('''select score, weight from gradebook 
								where student_ID = %s and course_ID = %s
								''', (student_ID, course_ID[0]))
		allgrades = school_manage_home.cursor.fetchall()
		
		final_grade = 0
		for grade in allgrades:
			final_grade += grade[0] * grade[1]
			#for x in grade:
			#### grade[i] prints as a tuple not an int
		
		
		final_grade = final_grade / 100
		tk.Label(master, text=final_grade).grid(row=(row + 1), column=(column + 1))

			


## Begin GUI
master = tk.Tk()
master.title("MARKSHEET")
master.geometry("700x250")

# set entry variables
last_name = tk.StringVar()
class1 = tk.StringVar()

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
#e4 = tk.Entry(master, textvariable=class1)
e5 = tk.Entry(master)
e6 = tk.Entry(master)
e7 = tk.Entry(master)
e8 = tk.Entry(master)

def display():
	# Variable to store total marks
	tot=0

	'''
	if e4.get() == "A":
		tot += 4
	if e4.get() == "B":
		tot += 3
	if e4.get() == "C":
		tot += 2
	if e4.get() == "D":
		tot += 1
	if e4.get() == "F":
		tot += 0


	if e5.get() == "A":
		tot += 4
	if e5.get() == "B":
		tot += 3
	if e5.get() == "C":
		tot += 2
	if e5.get() == "D":
		tot += 1
	if e5.get() == "F":
		tot += 0
	
	
	if e6.get() == "A":
		tk.Label(master)
		tot += 4
	if e6.get() == "B":
		tot += 3
	if e6.get() == "C":
		tot += 2
	if e6.get() == "D":
		tot += 1
	if e6.get() == "F":
		tot += 0


	if e7.get() == "A":
		tot += 4
	if e7.get() == "B":
		tot += 3
	if e7.get() == "C":
		tot += 2
	if e7.get() == "D":
		tot += 1
	if e7.get() == "F":
		tot += 0


	if e8.get() == "A":
		tot += 4
	if e8.get() == "B":
		tot += 3
	if e8.get() == "C":
		tot += 2
	if e8.get() == "D":
		tot += 1
	if e8.get() == "F":
		tot += 0
	'''

	tk.Label(master, text=str(tot)).grid(row=9, column=4)
	tk.Label(master, text=str(tot/5)).grid(row=10, column=4)


# label to enter name
tk.Label(master, text="Name").grid(row=0, column=0)
# label for registration number
tk.Label(master, text="Reg.No").grid(row=0, column=3)
# label for roll Number
tk.Label(master, text="Roll.No").grid(row=1, column=0)


# labels for subject codes
tk.Label(master, text="Subject").grid(row=5, column=1)
#tk.Label(master, text="Statistics").grid(row=3, column=1)
#tk.Label(master, text="Biology").grid(row=4, column=1)
#tk.Label(master, text="Physics").grid(row=5, column=1)
#tk.Label(master, text="History").grid(row=6, column=1)
#tk.Label(master, text="English").grid(row=7, column=1)

# label for grades
tk.Label(master, text="Grade").grid(row=5, column=2)
#e4.grid(row=6, column=2)
#e5.grid(row=7, column=2)
#e6.grid(row=8, column=2)
#e7.grid(row=9, column=2)
#e8.grid(row=10, column=2)

# labels for subject credits
tk.Label(master, text="Sub Credit").grid(row=5, column=4)
#tk.Label(master, text="4").grid(row=3, column=3)
#tk.Label(master, text="4").grid(row=4, column=3)
#tk.Label(master, text="3").grid(row=5, column=3)
#tk.Label(master, text="4").grid(row=6, column=3)
#tk.Label(master, text="4").grid(row=7, column=3)

# Name age roll entries
e1=tk.Entry(master, textvariable=last_name.get())
e2=tk.Entry(master)
e3=tk.Entry(master)

# organizing them in the grid
e1.grid(row=0, column=1)
e2.grid(row=0, column=4)
e3.grid(row=1, column=1)

# button to display all the calculated credit scores and sgpa
button1=tk.Button(master, text="submit", bg="green", command=display)
button1.grid(row=16, column=1)
button2 = tk.Button(master, text="Find", command=find_student)
button2.grid(row=0,column=2)

tk.Label(master, text="Total credits").grid(row=11, column=3)
tk.Label(master, text="Student GPA").grid(row=12, column=3)

master.mainloop()

