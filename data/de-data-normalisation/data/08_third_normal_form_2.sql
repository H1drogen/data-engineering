DROP DATABASE IF EXISTS normalisationsql;
CREATE DATABASE normalisationsql;

\c normalisationsql;

CREATE TABLE nc_restaurant_employees
( 
    employee_no VARCHAR PRIMARY KEY,
    full_name VARCHAR,
    employment VARCHAR,
    shift VARCHAR
);


INSERT INTO nc_restaurant_employees
    (employee_no, full_name, employment, shift)
VALUES
('NC0001', 'Gordon Ramsay', 'Full-time', 'All Day'),
('NC0002', 'Jamie Oliver', 'Part-time', 'Evening'),
('NC0003', 'Rachael Ray', 'Full-time', 'All Day'),
('NC0004', 'Wolfgang Puck', 'Full-time', 'All Day'),
('NC0005', 'Giada De Laurentiis', 'Full-time', 'All Day'),
('NC0006', 'Alan Ducasse', 'Part-time', 'Evening'),
('NC0007', 'Anne Burrell', 'Full-time', 'All Day'),
('NC0008', 'David Chang', 'Part-time', 'Evening'),
('NC0009', 'Guy Fieri', 'Part-time', 'Evening');

CREATE TABLE employee_jobs
(
    employee_no VARCHAR,
    job_title VARCHAR,
    FOREIGN KEY (employee_no) REFERENCES nc_restaurant_employees(employee_no)
);

INSERT INTO employee_jobs
    (employee_no, job_title)
VALUES
('NC0001', 'Head Chef'),
('NC0001', 'Owner'),
('NC0002', 'Waiter'),
('NC0003', 'Chef'),
('NC0004', 'Bartender'),
('NC0004', 'Dishwasher'),
('NC0005', 'Waiter'),
('NC0005', 'Dishwasher'),
('NC0006', 'Waiter'),
('NC0006', 'Bartender'),
('NC0007', 'Chef'),
('NC0008', 'Chef'),
('NC0009','Bartender');

SELECT * FROM nc_restaurant_employees;
SELECT * FROM employee_jobs;
