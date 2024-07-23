# Create your utility functions here, feel free to make additional files

from db.connection import db


def get_parks_data():
    parks = db.run("""SELECT * FROM parks;""")
    keys = ["park_id", "park_name", "year_opened", "annual_attendance"]

    park_dicts = [{keys[i]: park[i] for i in range(4)} for park in parks]

    return park_dicts


def format_rides(rides, parks):
    lookup = {park["park_name"]: park["park_id"] for park in parks}

    formatted_rides = [dict(ride, park_id=lookup[ride["park_name"]]) for ride in rides]

    for ride in formatted_rides:
        del ride["park_name"]

    return formatted_rides

