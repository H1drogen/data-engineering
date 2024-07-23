DROP DATABASE IF EXISTS normalisationsql;
CREATE DATABASE normalisationsql;

\c normalisationsql;

CREATE TABLE food_orders
(
    customer_name VARCHAR PRIMARY KEY,
    food_order VARCHAR,
    restaurant VARCHAR,
    preference VARCHAR
);



INSERT INTO food_orders
    (customer_name, food_order, restaurant, preference)
VALUES
    ('Jack', 'Cheeseburger, Fries, Tango',	'McDonald''s', 'Takeaway'),
    ('Henry', 'McNuggets, Fries, Coke, Apple Pie', 'McDonald''s', 'Dine-in'),
    ('Jennifer', 'Meatball Sub, Crisps, Oasis',	'Subway', 'Dine-in'),
    ('Tim',	'Wings, Sprite', 'KFC',	'Takeaway'),
    ('Hannah', 'Steak & Cheese Sub, Cookie, Fanta',	'Subway', 'Takeaway'),
    ('Steph', 'Zinger Burger, Fries, Oreo Krushem', 'KFC', 'Takeaway');


SELECT * FROM food_orders;

SELECT customer_name, unnest(string_to_array(food_order, ', ')), restaurant, preference FROM food_orders;