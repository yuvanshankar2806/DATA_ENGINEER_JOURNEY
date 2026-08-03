# How to use where clause 

SELECT *
FROM Students
WHERE marks > 80;

SELECT *
FROM Students
WHERE age = 20;

# To use AND operator in WHERE clause

SELECT *
FROM Students
WHERE age = 20 AND department = 'CSE';

# To use OR operator in WHERE clause

SELECT *
FROM Students
WHERE age = 20 OR department = 'CSE';

# To use ORDER BY clause to sort data

SELECT *
FROM Students
ORDER BY marks DESC;

SELECT *
FROM Students
ORDER BY name ASC;

# To use LIMIT clause to limit the number of rows returned

SELECT *
FROM Students
LIMIT 3;

# To use distinct keyword to get unique values

SELECT DISTINCT department
FROM Students;

# To use Alias

SELECT
name AS Student_Name,
marks AS Score
FROM Students;
