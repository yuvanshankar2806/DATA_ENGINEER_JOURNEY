#EG 1

SELECT *
FROM Students
WHERE Marks > 80;

#EG 2

SELECT *
FROM Students
WHERE City = 'Chennai';

#EG 3

SELECT *
FROM Students
WHERE Course = 'Python';

#EG 4

SELECT *
FROM Students
WHERE Marks BETWEEN 60 AND 90;

#EG 5

SELECT *
FROM Students
WHERE Name LIKE 'D%';

#EG 6

SELECT *
FROM Students
WHERE City IN ('Chennai', 'Salem');

#EG 7

SELECT *
FROM Students
ORDER BY Marks DESC;

