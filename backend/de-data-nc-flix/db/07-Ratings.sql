\c nc_flix

SELECT genre_name, title, movies.rating
FROM movies
INNER JOIN movies_genres
    ON movies.movie_id = movies_genres.movie_id
INNER JOIN genres
    ON movies_genres.genre_id = genres.genre_id
WHERE (genre_name, rating) IN (
    SELECT genre_name, MIN(rating)
    FROM movies
    INNER JOIN movies_genres
        ON movies.movie_id = movies_genres.movie_id
    INNER JOIN genres
        ON movies_genres.genre_id = genres.genre_id
    GROUP BY genre_name
);

SELECT DISTINCT genre_name, title, rating
FROM stock
INNER JOIN stores
    ON stock.store_id = stores.store_id
INNER JOIN movies
    ON stock.movie_id = movies.movie_id
INNER JOIN movies_genres
    ON movies.movie_id = movies_genres.movie_id
INNER JOIN genres
    ON movies_genres.genre_id = genres.genre_id
WHERE city = 'Manchester'
ORDER BY genre_name;
