-- Create a subquery
-- Execute: cat 8-cities_of_california_subquery.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
SELECT name FROM hbtn_0d_usa.*
WHERE name = California
ORDER BY cities.id ASC;
