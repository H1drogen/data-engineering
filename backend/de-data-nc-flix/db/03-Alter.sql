\c nc_flix

\echo 'Query the database to find the store with the highest total number of copies of sequels. Let''s assume a film is a sequel if the title contains something like ''II'' or ''VI''\n'

\echo 'This is likely not a good way to identify sequels going forward. Alter the movies table to track this information better and then update the previous query to make use of this new structure.\n'

ALTER TABLE movies
ADD is_sequel boolean
    DEFAULT FALSE;

UPDATE movies
SET is_sequel = TRUE
WHERE title LIKE '% I %'
OR title LIKE '% II%'
OR title LIKE '% IV%'
OR title LIKE '% IX%';

SELECT city
FROM stores
WHERE stores.store_id = (
    SELECT stock.store_id
    FROM stores
    INNER JOIN stock
        ON stores.store_id = stock.store_id
    INNER JOIN movies
        ON stock.movie_id = movies.movie_id
    WHERE is_sequel IS TRUE
    GROUP BY stock.store_id
    ORDER BY COUNT(movies.movie_id)
    LIMIT 1
);
