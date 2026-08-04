# WHERE clause

SELECT *
FROM Students
WHERE Age = 20;

# Comparison Operators

#EG 1
SELECT *
FROM Students
WHERE Marks > 80;

#EG 2
SELECT Name, Course
FROM Students
WHERE Course = 'Python';

# Logical Operators

#AND

SELECT *
FROM Students
WHERE Age = 20 AND Marks > 80;

#OR

SELECT *
FROM Students
WHERE Course = 'Python'
OR Course = 'Java';
#NOT

SELECT *
FROM Students
WHERE NOT City = 'Chennai';

#IN

SELECT *
FROM Students
WHERE City IN ('Chennai', 'Salem');

#BETWEEN

SELECT *
FROM Students
WHERE Marks BETWEEN 70 AND 90;

#LIKE

SELECT *
FROM Students
WHERE Name LIKE 'A%';

#NULL

SELECT *
FROM Students
WHERE City IS NULL;

#ORDER BY

SELECT *
FROM Students
ORDER BY Marks ASC;

