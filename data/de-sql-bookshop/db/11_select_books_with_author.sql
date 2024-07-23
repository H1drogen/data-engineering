\c my_bookshop

\echo '\n Here is a list of book titles with the corresponding author:\n'

SELECT * FROM books;

SELECT books.book_id, books.author_id, books.title, authors.author_name, books.price_in_pence, books.quantity_in_stock, books.release_date, books.is_fiction FROM books
LEFT JOIN authors
ON books.author_id = authors.author_id;

\echo '\n Here is a list of authors without an associated book:\n'

SELECT * FROM authors
FULL OUTER JOIN books
-- ON is necessary for JOIN. How to join tables together
ON books.author_id = authors.author_id
-- removing any books id without id's
WHERE books.author_id IS NULL;

\echo 'activity 11'