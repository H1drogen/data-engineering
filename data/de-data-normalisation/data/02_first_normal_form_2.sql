DROP DATABASE IF EXISTS normalisationsql;
CREATE DATABASE normalisationsql;

\c normalisationsql;

CREATE TABLE nc_mentors
( 
    employee_id INT PRIMARY KEY,
    mentor_name VARCHAR,
    department VARCHAR,
    location VARCHAR
);

INSERT INTO nc_mentors
    (employee_id, mentor_name, department, location)
VALUES
    (1, 'Rose', 'Software', 'Manchester'),
    (2, 'Eli', 'Software, Data', 'Manchester'),
    (3, 'Haz', 'Cloud, Data', 'Manchester'),
    (4, 'Jim', 'Software', 'Leeds'),
    (5, 'John', 'CLoud', 'Manchester'),
    (6, 'Edd', 'Data, Software, CLoud', 'Leeds');

SELECT * FROM nc_mentors;
