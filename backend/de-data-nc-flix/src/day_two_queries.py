from pg8000.native import Connection
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv(".env")


def connect_to_db():
    return Connection(
        user=os.getenv("user"),
        password=os.getenv("password"),
        database=os.getenv("database"),
        host=os.getenv("host"),
        port=os.getenv("port"),
    )


def select_movies(sort_by="title", order="ASC", min_rating: int = 0, location=""):
    con = connect_to_db()
    valid_sorts = ["release_date", "rating", "cost"]
    if sort_by not in valid_sorts:
        sort_by = "title"
    if order.upper() != "DESC":
        order = "ASC"
    if not location:
        movies = con.run(
            f"SELECT * FROM movies WHERE rating > :min_rating ORDER BY {sort_by} {order}",
            min_rating=min_rating,
        )
    else:
        movies = con.run(
            "SELECT * FROM movies INNER JOIN stock ON movies.movie_id = stock.movie_id "
            "INNER JOIN stores on stock.store_id = stores.store_id "
            f"WHERE rating > :min_rating AND city = :location ORDER BY {sort_by} {order}",
            min_rating=min_rating,
            location=location,
        )
    columns = [d["name"] for d in con.columns]
    return [dict(zip(columns, movie)) for movie in movies]



pprint(select_movies("rating", "DESC", location="Manchester"))
