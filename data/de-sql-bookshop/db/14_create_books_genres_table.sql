\c my_bookshop

DROP TABLE IF EXISTS books_with_genres;
CREATE TABLE book_with_genres (
    book_with_genres_id SERIAL Primary Key,
    book_id INT REFERENCES books(book_id),
    genre_1 INT REFERENCES genres(genre_id),
    genre_2 INT REFERENCES genres(genre_id)
);
