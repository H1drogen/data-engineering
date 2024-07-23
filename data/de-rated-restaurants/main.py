import json
import uvicorn
from fastapi import FastAPI, HTTPException
from pg8000 import DatabaseError

from db.connection import connect_to_db
from pydantic import BaseModel

app = FastAPI()
db = connect_to_db()

class Restaurant(BaseModel):
    restaurant_name: str
    area_id: int
    cuisine: str
    website: str

class AreaID(BaseModel):
    area_id: int

def get_healthcheck():
    return {'message': 'okay'}

@app.get('/')
def get_message():
    return {'message': 'all okay'}

@app.get('/restaurants')
def return_all_restaurants():
    dict = {}
    query = "SELECT * FROM restaurants;"
    outputs = db.run(query)
    for restaurant in outputs:
        dict[restaurant[1]] = {restaurant[3], restaurant[4]}
    return dict

@app.post('/restaurants')
def add_restaurant(restaurant: Restaurant):
    try:
        query = "INSERT INTO restaurants (restaurant_name, area_id, cuisine, website) VALUES (:restaurant_name, :area_id, :cuisine, :website);"
        db.run(query, restaurant_name=restaurant.restaurant_name, area_id=restaurant.area_id, cuisine=restaurant.cuisine, website=restaurant.website)
        new_restaurant = db.run('SELECT * FROM restaurants WHERE restaurant_id=(SELECT max(restaurant_id) FROM restaurants);')
        return {'restaurant': {
            'restaurant_id': new_restaurant[0][0],
            'restaurant_name': new_restaurant[0][1],
            'area_id': new_restaurant[0][2],
            'cuisine': new_restaurant[0][3],
            'website': new_restaurant[0][4]
        }}
    except DatabaseError as e:
        raise HTTPException(status_code=400, detail={'error': str(e.args[0]['D'])})

@app.delete('/restaurants/{restaurant_id}', status_code=204)
def delete_restaurant(restaurant_id: int):
    if db.run('SELECT * FROM restaurants WHERE restaurant_id = :restaurant_id;', restaurant_id=restaurant_id) == []:
        raise HTTPException(status_code=400, detail=f'Restaurant ID {restaurant_id} does not exist')
    query = "DELETE FROM restaurants WHERE restaurant_id = :restaurant_id;"
    db.run(query, restaurant_id=restaurant_id)

@app.patch('/restaurants/{restaurant_id}')
def replace_area_id(restaurant_id: int, area_id: AreaID):
    try:
        query = "UPDATE restaurants SET area_id = :area_id WHERE restaurant_id = :restaurant_id;"
        if db.run('SELECT * FROM restaurants WHERE restaurant_id = :restaurant_id;', restaurant_id=restaurant_id) == []:
            raise HTTPException(status_code=400, detail=f'Restaurant ID {restaurant_id} does not exist')
        db.run(query, area_id=area_id.area_id, restaurant_id=restaurant_id)
        new_restaurant = db.run('SELECT * FROM restaurants WHERE restaurant_id=:restaurant_id);', restaurant_id=restaurant_id)
        return {'restaurant': {
            'restaurant_id': new_restaurant[0][0],
            'restaurant_name': new_restaurant[0][1],
            'area_id': new_restaurant[0][2],
            'cuisine': new_restaurant[0][3],
            'website': new_restaurant[0][4]
        }}
    except DatabaseError as e:
        raise HTTPException(status_code=400, detail={'error': str(e.args[0]['D'])})

@app.add_exception_handler(UnprocessableEntity)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)




