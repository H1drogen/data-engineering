\c nc_flix

\echo '\nQuery the database to find the number of films in stock for each genre\n'

SELECT COUNT(movie_id), genre_name
FROM (
    SELECT movies_genres.movie_id, genre_name
    FROM movies_genres
    INNER JOIN genres
        ON movies_genres.genre_id = genres.genre_id
    INNER JOIN stock
        ON stock.movie_id = movies_genres.movie_id)
GROUP BY genre_name;

\echo 'Query the database to find the average rating for films in stock in Newcastle.\n'

WITH movies_stock_stores AS (
    SELECT rating, city
    FROM movies
    INNER JOIN stock
        ON movies.movie_id = stock.movie_id
    INNER JOIN stores
        ON stock.store_id = stores.store_id
    WHERE city = 'Newcastle'
)
SELECT ROUND(AVG(rating), 2) AS average_rating_for_city, city
FROM movies_stock_stores
GROUP BY city;

\echo 'Query the database to retrieve all the films released in the 90s that have a rating greater than the total average.\n'

SELECT *
FROM movies
WHERE release_date >= '1990-01-01'
AND release_date <= '2000-01-01'
AND rating > (
    SELECT AVG(rating)
    FROM movies
);

\echo 'Query the database to find the total number of copies that are in stock for the top-rated film from a pool of the five most recently released films.\n'

SELECT COUNT(stock.movie_id) AS copies_top_rated_last_five
FROM stock
WHERE stock.movie_id = (
    SELECT movie_id
    FROM (
        SELECT movie_id, rating, title
        FROM movies
        ORDER BY release_date DESC
        LIMIT 5
    )
ORDER BY rating
LIMIT 1
);

\echo 'Query the database to find a list of all the locations in which customers live that don''t contain a store.\n'

SELECT DISTINCT customers.location AS location_no_store
FROM customers
LEFT JOIN stores
    ON stores.city = customers.location
WHERE store_id IS NULL;

\echo 'Query the database to find a list of all the locations we have influence over (locations of stores and/or customers). There should be no repeated data.\n'
-- I don't know what this query wants from me, what influence?

SELECT *
FROM customers
WHERE location = 'Manchester' OR location = 'Leeds';

\echo 'From a list of our stores which have customers living in the same location, calculate which store has the largest catalogue of stock. What is the most abundant genre in that store?\n'

SELECT genre_name, COUNT(genre_name) AS genre_count
FROM genres
INNER JOIN movies_genres
    ON genres.genre_id = movies_genres.genre_id
INNER JOIN movies
    ON movies_genres.movie_id = movies.movie_id
INNER JOIN stock
    ON movies.movie_id = stock.movie_id
WHERE store_id = (
    SELECT stock.store_id
    FROM stock
    INNER JOIN (
        SELECT DISTINCT stores.store_id
        FROM customers
        INNER JOIN stores
            ON stores.city = customers.location
    ) stores_with_customers
        ON stock.store_id = stores_with_customers.store_id
    GROUP BY stock.store_id
    ORDER BY COUNT(movie_id) DESC
    LIMIT 1
)
GROUP BY genre_name
ORDER BY genre_count DESC
LIMIT 1;