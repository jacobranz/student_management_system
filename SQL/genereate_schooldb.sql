/* 
Before running this script, for easiest results open 'MySQLWorkbench'.
	1. Create a connection with the same creds at the top of main.py.
    2. Create a schema called 'grades'.
    3. Double click on the 'grades' schema under the 'SCHEMAS' table and open a new tab.
    4. Either paste or open this .sql script and run it.
*/


-- Below are the commands to run to generate the necessary tables inside of the 'grades' schema.
create table professor (
	professor_ID int,
    first_name varchar(255),
    last_name varchar(255),
    age int,
    qualifications varchar(255),
    start_date date,
    primary key (professor_ID)
);

create table student (
	student_ID int,
    first_name varchar(255),
    last_name varchar(255),
    age int,
    grade_level int,
    primary key (student_ID)
);

create table course (
	course_ID int,
    name varchar(255),
    creds int,
    professor_ID int,
    primary key (course_ID),
    foreign key (professor_ID) references professor(professor_ID)
);

create table enrollment (
	student_ID int,
    course_ID int,
    foreign key (student_ID) references student(student_ID),
    foreign key (course_ID) references course(course_ID)
);

create table gradebook (
	student_ID int,
    course_ID int,
    assignment varchar(255),
    score double,
    weight int,
    foreign key (student_ID) references student(student_ID),
    foreign key (course_ID) references course(course_ID)
);