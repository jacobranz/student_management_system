/*
	***** Student Notes *****
    Student 'Zach Miller' is added to all classes with grades in each one to show report card
    Student 'Samantha Testerman' is added to Math 150 to show max students rule is effective
    
    **** Professor Notes *****
    Two professors have been created to query if desired
    
    ***** Course Notes *****
    Course 'English 120' has been create with no professor to add one in the demo
*/

-- insert test professors for demonstration
insert into professor values (1, "Josh", "Allen", 48, "Masters", "2022-03-08");
insert into professor values (2, "Lamar", "Jackson", 35, "Doctorate", "2020-09-23");

-- insert professors into courses
insert into course values (1, "Physics 101", 4, 1);
insert into course values (2, "Math 150", 4, 1);
insert into course (course_ID, name, creds) values (3, "English 120", 4); -- add course without professor
insert into course values (4, "Music 100", 4, 2);

-- insert test students for demonstration
insert into student values (1, "Zach", "Miller", 23, 15);
insert into student values (2, "Samantha", "Testerman", 21, 13);
insert into student values (3, "Jacob", "Ranz", 22, 14);

-- insert students into courses
insert into enrollment values (1, 1); -- adding to Physics 101
insert into enrollment values (1, 3); -- adding to English 120
insert into enrollment values (1, 2); -- adding to Math 150
insert into enrollment values (1, 4); -- adding to Music 100
insert into enrollment values (2, 2); -- adding to Math 150

-- add grades for students
	-- adding 'Zach Miller' grades to Physics 101
	insert into gradebook values (1, 1, "Project 1", 89, 25);
	insert into gradebook values (1, 1, "Project 2", 85, 25);
	insert into gradebook values (1, 1, "Project 3", 78, 25);
	insert into gradebook values (1, 1, "Final", 99, 25);
    
    -- adding 'Zach Miller' grades to Math 150
    insert into gradebook values (1, 2, "Project 1", 87, 25);
    insert into gradebook values (1, 2, "Project 2", 90, 25);
    insert into gradebook values (1, 2, "Project 3", 98, 25);
    insert into gradebook values (1, 2, "Final", 91, 25);
    
    -- adding 'Zach Miller' grades to English 120
    insert into gradebook values (1, 3, "Group Project 1", 79, 25);
	insert into gradebook values (1, 3, "Group Project 2", 95, 25);
    insert into gradebook values (1, 3, "Group Project 3", 97, 25);
    insert into gradebook values (1, 3, "Group Project 4", 83, 25);
    
    -- adding 'Zach Miller' grades to Music 100
    insert into gradebook values (1, 4, "Project 1", 76, 25);
    insert into gradebook values (1, 4, "Project 2", 84, 25);
    insert into gradebook values (1, 4, "Project 3", 89, 25);
    insert into gradebook values (1, 4, "Final", 86, 25);
    
    -- adding 'Samantha Testerman' grades to Math 150
    insert into gradebook values (2, 2, "Project 1", 77, 25);
    insert into gradebook values (2, 2, "Project 2", 96, 25);
    insert into gradebook values (2, 2, "Project 3", 89, 25);
    insert into gradebook values (2, 2, "Final", 89, 25);