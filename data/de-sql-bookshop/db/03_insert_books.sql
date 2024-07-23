\c my_bookshop;

INSERT INTO books (title, price_in_pence, quantity_in_stock, release_date, is_fiction)
VALUES ('The Hitchhiker''s Guide to the Galaxy', 899, 560, '1997-10-12', true),
    ('The Little Prince', 699, 1000, '1943-04-06', true),
    ('The Tale of Peter Rabbit', 599, 560, '1902-10-01', true),
    ('Emma', 522, 390, '1815-12-23', true),
    ('Nineteen Eighty-Four: A Novel', 799, 420, '1949-06-08', true),
    ('The Handmaid''s Tale', 899, 10, '1985-08-01', true),
    ('The War of the Worlds', 250, 17, '1897-04-01', true),
    ('Captain Corelli''s Mandolin', 999, 0, '1995-08-29', true),
    ('A Brief History of Time', 825, 0, '1988-04-01', false),
    ('Pride and Prejudice', 699, 4, '1813-01-28', true);

SELECT * FROM books;

\echo 'activity 3'