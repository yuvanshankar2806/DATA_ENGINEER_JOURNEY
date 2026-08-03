# SQL Syntax

# TOCREATE DATABASE database_name;
CREATE DATABASE StudentDB;
# TO USE database_name;
USE StudentDB;
# TO CREATE TABLE table_name 

    CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    department VARCHAR(30),
    marks INT
);


# Insert data into the table

INSERT INTO Students
VALUES
(1, 'Alice', 20, 'CSE', 89),
(2, 'Bob', 21, 'ECE', 75),
(3, 'Charlie', 19, 'IT', 92),
(4, 'David', 22, 'CSE', 81),
(5, 'Eva', 20, 'EEE', 68);

# To SELECT data from the table

SELECT * FROM Students;

SELECT name, marks
FROM Students;

# To use WHERE clause to filter data

SELECT *
FROM Students
WHERE department = 'CSE';
