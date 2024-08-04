\c nc_flix

SELECT t4.store_id, city, customers, total_movies, customer_name AS most_loyal_customer, title, average_score
FROM (
    SELECT stores.store_id, stores.city, COUNT(customer_id) AS customers
    FROM rentals
    INNER JOIN stock
        ON rentals.stock_id = stock.stock_id
    INNER JOIN stores
        ON stock.store_id = stores.store_id
    GROUP BY city, stores.store_id) t1
    INNER JOIN (
        SELECT store_id, COUNT(stock_id) AS total_movies
        FROM stock
        GROUP BY store_id
    ) AS t2
    ON t2.store_id = t1.store_id
INNER JOIN (
    WITH t3 AS (
        SELECT COUNT(customer_id) AS customers, customer_id, store_id
        FROM rentals
        INNER JOIN stock
            ON rentals.stock_id = stock.stock_id
        GROUP BY customer_id, store_id
        )
        SELECT store_id, customer_id AS most_loyal_customer_id
        FROM t3
        WHERE (store_id, customers) IN (SELECT store_id, MAX(customers) FROM t3 GROUP BY store_id)
    ) t4
    ON t1.store_id = t4.store_id
INNER JOIN customers
    ON customers.customer_id = most_loyal_customer_id
INNER JOIN (
    WITH t5 AS (
        SELECT COUNT(movie_id) AS movie_rentals, movie_id, store_id
        FROM rentals
        INNER JOIN stock
            ON rentals.stock_id = stock.stock_id
        GROUP BY store_id, movie_id
    )
    SELECT store_id, movie_id AS most_rented_movie_id
    FROM t5
    WHERE (store_id, movie_rentals) IN (SELECT store_id, MAX(movie_rentals) FROM t5 GROUP BY store_id)
    ) t6
    ON t1.store_id = t6.store_id
INNER JOIN movies
    ON movies.movie_id = most_rented_movie_id
INNER JOIN (
    SELECT stores.store_id, ROUND(AVG(rating), 1) AS average_score
    FROM stores
    INNER JOIN stock
        ON stores.store_id = stock.stock_id
    INNER JOIN movies
        ON stock.movie_id = movies.movie_id
    GROUP BY stores.store_id
) t7
    ON t1.store_id = t7.store_id;