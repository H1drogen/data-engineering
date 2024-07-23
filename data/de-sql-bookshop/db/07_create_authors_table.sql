\c my_bookshop

DROP TABLE IF EXISTS authors;
CREATE TABLE authors (
    author_id SERIAL Primary Key,
    author_name TEXT,
    fun_fact TEXT
);

SELECT *
FROM authors

\echo 'activity 7'