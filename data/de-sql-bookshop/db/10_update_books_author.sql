\c my_bookshop

UPDATE books
SET author_id = 3
WHERE book_id = 1;

UPDATE books
SET author_id = 2
WHERE book_id = 2;

UPDATE books
SET author_id = 7
WHERE book_id = 3;

UPDATE books
SET author_id = 14
WHERE book_id = 4;

UPDATE books
SET author_id = 13
WHERE book_id = 5;

UPDATE books
SET author_id = 15
WHERE book_id = 6;

UPDATE books
SET author_id = 12
WHERE book_id = 7;

UPDATE books
SET author_id = 14
WHERE book_id = 10;

SELECT * FROM books;

\echo 'activity 10'