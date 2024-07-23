\c my_bookshop;

-- create the books table here
DROP TABLE IF EXISTS books;
CREATE TABLE books (
    book_id SERIAL Primary Key,
    title TEXT,
    price_in_pence INT,
    quantity_in_stock INT,
    release_date TEXT,
    is_fiction BOOLEAN
);

\echo 'activity 2'