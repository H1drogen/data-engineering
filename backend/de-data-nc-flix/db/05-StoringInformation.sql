\c nc_flix

CREATE TABLE rentals (
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
    WHEN classification = 'U' THEN 'yes' ELSE 'no'
END AS is_age_appropriate,
CASE
    WHEN city = 'Birmingham' THEN 'yes' ELSE 'no'
END AS is_available_birmingham,
CASE
    WHEN total_rentals <= 5 THEN 'yes' ELSE 'no'
END AS is_rented_max_5
FROM movies
INNER JOIN (
    SELECT COUNT(rental_id) AS total_rentals, movie_id
    FROM rentals
    RIGHT JOIN stock
        ON rentals.stock_id = stock.stock_id
    GROUP BY movie_id
) rc
    ON movies.movie_id = rc.movie_id
INNER JOIN stock
    ON movies.movie_id = stock.movie_id
INNER JOIN stores
    ON stock.store_id = stores.store_id;
