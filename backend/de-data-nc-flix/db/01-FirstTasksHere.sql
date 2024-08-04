\c nc_flix

\echo '\nQuery the database to retrieve all of the movie titles that were released in the 21st century.\n'

SELECT *
FROM movies
WHERE release_date >= '2001-01-01';

\echo 'Query the database to find the oldest customer.\n'

SELECT *
FROM customers
ORDER BY date_of_birth LIMIT 1;

\echo 'Query the database to find the customers whose name begins with the letter D. Organise the results by age, youngest to oldest.\n'

SELECT *
FROM customers
WHERE customer_name like 'D%'
ORDER BY date_of_birth DESC;

\echo 'Query the database to find the average rating of the movies released in the 1980s.\n'

SELECT ROUND(AVG(rating), 2)
FROM movies
WHERE release_date >= '1980-01-01' AND release_date <= '1990-01-01';

\echo 'Query the database to list the locations of our customers, as well as the total and average number of loyalty points for all customers. You can assume that if the loyalty points row is empty, they are a new customer so they should have the value set to zero.\n'

\echo 'Locations:\n'

SELECT DISTINCT location
FROM customers;

\echo 'Total loyalty points:\n'

SELECT SUM(loyalty_points) AS total_l_points
FROM customers;

\echo 'Average loyalty points:\n'

SELECT ROUND(AVG(loyalty_points), 2) AS avg_l_points
FROM customers;

\echo 'The rise in living costs is affecting rentals. Drop the cost of all rentals by 5% and display the updated table. As this is a monetary value, make sure it is rounded to 2 decimal places.\n'

UPDATE movies
SET cost = ROUND(cost * 0.95, 2);

SELECT *
FROM movies;
