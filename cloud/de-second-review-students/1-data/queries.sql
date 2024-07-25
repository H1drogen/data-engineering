-- add queries here!

SELECT title, num_items FROM products
INNER JOIN sales ON products.id = sales.product_id
WHERE num_items is not NULL
ORDER BY sales.num_items desc
LIMIT 3;


SELECT title, SUM(products.product_cost * sales.num_items) as monetary_value FROM products
JOIN sales ON products.id = sales.product_id
GROUP BY title
ORDER BY monetary_value desc
LIMIT 3;

SELECT email, phone_number, SUM(products.product_cost * sales.num_items) as spend FROM users
INNER JOIN sales ON users.id = sales.buyer_id
INNER JOIN products ON products.id = sales.product_id
WHERE EXTRACT('month' FROM transaction_ts) = 12 AND EXTRACT('year' FROM transaction_ts) = 2022
GROUP BY email, phone_number
ORDER BY spend desc
LIMIT 1;


