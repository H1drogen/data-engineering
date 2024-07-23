\c my_bookshop

\echo '\n Here are the genres for Emma:\n'

SELECT books.title, genre1.genre_type, genre2.genre_type FROM book_with_genres
INNER JOIN genres AS genre1
ON book_with_genres.genre_1 = genre1.genre_id
INNER JOIN genres AS genre2
ON book_with_genres.genre_2 = genre2.genre_id
INNER JOIN books
ON book_with_genres.book_id = books.book_id
WHERE book_with_genres.book_id = 4;

\echo '\n Here are all the dystopian books:\n'

SELECT books.title, genre1.genre_type, genre2.genre_type FROM book_with_genres
INNER JOIN genres AS genre1
ON book_with_genres.genre_1 = genre1.genre_id
INNER JOIN genres AS genre2
ON book_with_genres.genre_2 = genre2.genre_id
INNER JOIN books
ON book_with_genres.book_id = books.book_id
WHERE book_with_genres.genre_1 = 5 OR book_with_genres.genre_2 = 5;