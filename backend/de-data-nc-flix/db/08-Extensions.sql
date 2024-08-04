\c nc_flix

ALTER TABLE stock
ADD condition VARCHAR
    DEFAULT 'undamaged';

UPDATE stock
SET condition = 'damaged'
WHERE movie_id = (
    SELECT movie_id
    FROM movies
    WHERE title = 'Episode IX - The Rise of Skywalker'
);


INSERT INTO stores
(city)
SELECT location FROM (
    SELECT COUNT(customer_id) AS customers, location
    FROM customers
    WHERE location NOT IN (
        SELECT city
        FROM stores
    )
    GROUP BY location
    ORDER BY customers DESC
    LIMIT 2
);

INSERT INTO stock
(store_id, movie_id)
SELECT store_id, movie_id
FROM (
    SELECT (SELECT store_id FROM stores ORDER BY store_id DESC LIMIT 1), movie_id
    FROM movies
    WHERE rating IS NOT NULL
    ORDER BY rating DESC
    LIMIT 10
)
UNION
SELECT store_id, movie_id
FROM (
    SELECT (SELECT store_id FROM stores ORDER BY store_id DESC LIMIT 1 OFFSET 1), movie_id
    FROM movies
    WHERE rating IS NOT NULL
    ORDER BY rating DESC
    LIMIT 10
);