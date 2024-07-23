\c my_bookshop;

\echo '\n Here are all the books that we have in stock:\n'

SELECT * FROM books
WHERE quantity_in_stock > 0;

\echo '\n Here are all the non-fiction books:\n'

SELECT * FROM books
WHERE is_fiction = false;

\echo '\n Here are all the books released in the 1900s:\n'

SELECT * FROM books
WHERE CAST(LEFT(release_date, 4) AS int) BETWEEN 1900 AND 2000;

\echo '\n Here are all the books with "The" in the title:\n'

SELECT * FROM books
WHERE title LIKE ('%The%');

\echo '\n Here are the books sorted in alphabetical order:\n'

SELECT * FROM books
ORDER BY title ASC;



\echo '\n Here is the most expensive book:\n'

SELECT 
    books.title, 
    MAX(books.price_in_pence) AS price_in_pence
FROM books
GROUP BY books.title
ORDER BY price_in_pence DESC
LIMIT 1;

\echo 'activity 4'