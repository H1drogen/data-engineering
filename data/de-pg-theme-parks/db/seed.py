# You will need to write your database connection file
# before being able to run your seed file


from db.connection import db
from pg8000.native import literal
from db.utils.format_rides import format_rides, get_parks_data
from db.utils.format_stalls import format_stalls, format_stalls_foods
# You will need to alter your database connection file
# before being able to run your seed file


def seed(parks, rides, stalls, foods):
    '''Seeds database'''
    db.run("DROP TABLE IF EXISTS rides;")
    db.run("DROP TABLE IF EXISTS stalls_foods;")
    db.run("DROP TABLE IF EXISTS stalls;")
    db.run("DROP TABLE IF EXISTS foods;")
    db.run("DROP TABLE IF EXISTS parks;")
    create_parks()
    create_rides()
    insert_parks(parks)
    insert_rides(rides)
    create_stalls()
    create_foods()
    create_stalls_foods()
    inserted_stalls = insert_stalls(stalls)
    inserted_foods = insert_foods(foods)
    insert_stalls_foods(stalls, inserted_stalls, inserted_foods)


def create_parks():
    '''Creates parks table'''
    db.run("""CREATE TABLE parks (
                  park_id SERIAL PRIMARY KEY,
                  park_name VARCHAR(40) NOT NULL,
                  year_opened INT NOT NULL,
                  annual_attendance INT NOT NULL
    );""")


def create_rides():
    '''Creates rides table'''
    db.run("""CREATE TABLE rides (
                  ride_id SERIAL PRIMARY KEY,
                  park_id INT REFERENCES parks(park_id),
                  ride_name VARCHAR(40) NOT NULL,
                  year_opened INT NOT NULL,
                  votes INT NOT NULL
    );""")


def insert_parks(parks):
    '''inserts parks data'''
    start_of_query = """INSERT INTO parks 
    (park_name, year_opened, annual_attendance)
                    VALUES """

    values = ', '.join([f"""({literal(park['park_name'])}, 
                        {literal(park['year_opened'])}, 
                        {literal(park['annual_attendance'])})"""
                        for park in parks])

    query = start_of_query + values

    db.run(query)


def insert_rides(rides):
    '''Inserts rides data'''

    park_data = get_parks_data()
    formatted_rides = format_rides(rides, park_data)

    start_of_query = """INSERT INTO rides 
    (ride_name, park_id, year_opened, votes)
                    VALUES """

    values = ', '.join([f"""({literal(ride['ride_name'])}, 
                        {literal(ride['park_id'])}, 
                        {literal(ride['year_opened'])},
                        {literal(ride["votes"])})"""
                        for ride in formatted_rides])

    query = start_of_query + values

    db.run(query)


def create_stalls():
    '''Creates stalls table'''
    db.run("""CREATE TABLE stalls (
                  stall_id SERIAL PRIMARY KEY,
                  stall_name VARCHAR(40),
                  park_id INT REFERENCES parks(park_id)
    );""")


def create_foods():
    '''Creates foods table'''
    db.run("""CREATE TABLE foods (
                  food_id SERIAL PRIMARY KEY,
                  food_name VARCHAR(40),
                  vegan_option BOOLEAN
    );""")


def create_stalls_foods():
    '''Creates stalls_foods junction table'''
    db.run("""CREATE TABLE stalls_foods (
                  stall_id INT REFERENCES stalls(stall_id),
                  food_id INT REFERENCES foods(food_id),
                  PRIMARY KEY (stall_id, food_id)
    );""")


def insert_stalls(stalls):
    '''Inserts stalls data'''
    park_data = get_parks_data()
    formatted_stalls = format_stalls(stalls, park_data)

    start_of_query = """INSERT INTO stalls 
                    (stall_name, park_id)
                    VALUES """

    values = ', '.join([f"""({literal(stall['stall_name'])}, 
                        {literal(stall['park_id'])})"""
                        for stall in formatted_stalls])

    end_of_query = " RETURNING *;"

    query = start_of_query + values + end_of_query

    return db.run(query)


def insert_foods(foods):
    '''Inserts foods data'''
    start_of_query = """INSERT INTO foods 
                    (food_name, vegan_option)
                    VALUES """

    values = ', '.join([f"""({literal(food['food_name'])}, 
                        {literal(food['vegan_option'])})"""
                        for food in foods])

    end_of_query = " RETURNING *;"

    query = start_of_query + values + end_of_query

    return db.run(query)


def insert_stalls_foods(og_stalls, stalls, foods):
    '''Inserts stalls_foods data'''
    id_pairs = format_stalls_foods(og_stalls, stalls, foods)

    start_of_query = """INSERT INTO stalls_foods 
                    (stall_id, food_id)
                    VALUES """

    values = ', '.join(
        [f"({literal(stall_id)}, {literal(food_id)})" for stall_id, food_id in id_pairs])

    query = start_of_query + values

    db.run(query)