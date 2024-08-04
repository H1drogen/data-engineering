
\c ncstaffsql

CREATE TABLE IF NOT EXISTS staff
(
    staff_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    area VARCHAR(50),
    course VARCHAR(100),
    manager VARCHAR(50),
    mentees INT,
    next_cohort_date TEXT,
    mentees_staff_rating INT,
    daily_rate FLOAT,
    revenue FLOAT
);

CREATE TABLE IF NOT EXISTS dim_management (
    management_id SERIAL PRIMARY KEY,
    staff_id INT REFERENCES staff(staff_id),
    manager VARCHAR(50),
    next_cohort_date TEXT
);

CREATE TABLE IF NOT EXISTS dim_mentees (
    mentees_id SERIAL PRIMARY KEY,
    staff_id INT REFERENCES staff(staff_id),
    mentees INT REFERENCES staff(mentees),
    mentees_staff_rating INT REFERENCES staff(mentees_staff_rating)
);

CREATE TABLE IF NOT EXISTS dim_finances (
    finances_id SERIAL PRIMARY KEY,
    staff_id INT REFERENCES staff(staff_id),
    daily_rate FLOAT REFERENCES staff(daily_rate),
    revenue FLOAT REFERENCES staff(revenue)
)