\c my_bookshop
ALTER TABLE books
ADD column author_id int REFERENCES authors(author_id);

\echo 'activity 9'