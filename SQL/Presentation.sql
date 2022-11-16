select student_ID from student where last_name = 'Smith';

select * from gradebook;
select * from enrollment;
select * from student;
select * from course;

insert into gradebook (student_ID, course_ID, assignment, weight) values (23, 1, "Midterm 1", 25);
insert into gradebook (student_ID, course_ID, assignment, weight) values (23, 1, "Midterm 2", 25);
insert into gradebook (student_ID, course_ID, assignment, weight) values (23, 1, "Group Project", 25);
insert into gradebook (student_ID, course_ID, assignment, weight) values (23, 1, "Final", 25);
insert into gradebook (student_ID, course_ID, assignment, weight) values (23, 2, "Project 1", 25);
insert into gradebook (student_ID, course_ID, assignment, weight) values (23, 2, "Project 2", 25);
insert into gradebook (student_ID, course_ID, assignment, weight) values (23, 2, "Project 3", 25);
insert into gradebook (student_ID, course_ID, assignment, weight) values (23, 2, "Final", 25);
insert into gradebook (student_ID, course_ID, assignment, weight) values (23, 4, "Final", 25);
insert into gradebook (student_ID, course_ID, assignment, weight) values (23, 4, "Final", 25);
insert into gradebook (student_ID, course_ID, assignment, weight) values (23, 4, "Final", 25);
insert into gradebook (student_ID, course_ID, assignment, weight) values (23, 4, "Final", 25);


update gradebook set score = 66 where
	assignment = 'Midterm 1' and student_ID = 23;
    
update gradebook set score = 0;