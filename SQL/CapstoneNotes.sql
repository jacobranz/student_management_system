select * from course;
insert into course values (1, "Physics 101", 4, 99);
insert into course values (2, "Math 150", 3, 99);
insert into course values (3, "English 120", 5, 99);
insert into course values (4, "Music 100", 2, 99);

select * from student;

select * from enrollment;
insert into enrollment values (24, 1);
insert into enrollment values (24, 2);
insert into enrollment values (24, 4);

select * from gradebook;
insert into gradebook values (24, 1, "Midterm 1", 80.3, 25);
insert into gradebook values (24, 1, "Midterm 2", 94.1, 25);
insert into gradebook values (24, 1, "Group Project", 86.4, 10);
insert into gradebook values (24, 1, "Final", 74.3, 40);
insert into gradebook values (24, 2, "Project 1", 78.2, 40);
insert into gradebook values (24, 2, "Project 2", 86.9, 40);
insert into gradebook values (24, 2, "Project 3", 78.9, 20);
insert into gradebook values (24, 2, "Final", 90.2, 20);
insert into gradebook values (24, 4, "Project 1", 80.3, 40);
insert into gradebook values (24, 4, "Project 2", 98.2, 40);
insert into gradebook values (24, 4, "Project 3", 86.2, 20);
insert into gradebook values (24, 4, "Final", 92.3, 20);

-- Implementation of "Find" button
-- First figure out the student ID
select student_id from student where last_name = "Ranz";
-- Use the student ID in the result set to execute the course query below:
select c.course_ID from course c, enrollment e where
	e.student_ID = 24 and e.course_ID = c.course_ID
    order by name asc;
-- For each course_id in the result set...
-- get the course name
select name from course where course_ID = 2;
-- get all the grades from this course to compute final grade
select score, weight from gradebook where student_ID = 24 and course_ID = 4
-- loop through the result set, mutliply each score by its weight and that gives you the total
-- score for the class