\c my_bookshop

DROP TABLE IF EXISTS genres;
CREATE TABLE genres (
    genre_id SERIAL Primary Key,
    genre_type varchar(15)
);

\echo 'activity 12'