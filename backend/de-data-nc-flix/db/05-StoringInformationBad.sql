\c nc_flix

DROP TABLE IF EXISTS rentals;

CREATE TABLE IF NOT EXISTS rentals (
    rental_id SERIAL PRIMARY KEY,
    stock_id int REFERENCES stock(stock_id),
    rental_start DATE,
    rental_end DATE,
    customer_id int REFERENCES customers(customer_id)
);

INSERT INTO rentals
(stock_id, rental_start, rental_end, customer_id)
VALUES
(1, '2020-08-15', '2020-09-13', 1),
(2, '2022-02-02', '2022-02-13', 2),
(3, '2023-06-15', '2020-07-12', 3),
(3, '2023-06-15', '2020-07-12', 3),
(3, '2023-06-15', '2020-07-12', 3),
(3, '2023-06-15', '2020-07-12', 3),
(3, '2023-06-15', '2020-07-12', 3),
(3, '2023-06-15', '2020-07-12', 3),
(3, '2023-06-15', '2020-07-12', 3),
(22, '2023-06-15', '2020-07-12', 5),
(22, '2023-06-15', '2020-07-12', 5),
(22, '2023-06-15', '2020-07-12', 5),
(22, '2023-06-15', '2020-07-12', 5),
(22, '2023-06-15', '2020-07-12', 5),
(22, '2023-06-15', '2020-07-12', 5);

SELECT DISTINCT movies.movie_id, title,
CASE
    WHEN movies.classification = 'U' THEN 'yes'
    ELSE 'no'
END AS age_appropriate,
CASE
    WHEN stores.city = 'Birmingham' THEN 'yes'
    ELSE 'no'
END AS available_in_birmingham,
-- This case doesn't work because the COUNT(rental_id) always returns the total
-- count of rentals. Instead, you have to compute COUNT(rental_id) for each movie, separately
CASE
    WHEN (  SELECT COUNT(rental_id) FROM rentals
            INNER JOIN stock ON rentals.stock_id = stock.stock_id
            INNER JOIN movies ON stock.movie_id = movies.movie_id
            -- WHERE movies.movie_id = stock.stock_id
            -- The WHERE clause here unnecessarily constrains the
            -- resulting rows to have the movie_id equal to the stock_id
            )
            <= 5 THEN 'yes'
    ELSE 'no'
END AS rented_less_than_5_times
FROM movies
INNER JOIN stock ON movies.movie_id = stock.movie_id
INNER JOIN stores ON stock.store_id = stores.store_id;
