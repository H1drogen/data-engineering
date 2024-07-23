'''This module is the entrypoint for the `Cat's Rare Treasures` FastAPI app.'''
import uvicorn

from db.seed import seed_db
from fastapi import FastAPI, Query
from db.connection import connect_to_db
from pydantic import BaseModel


app = FastAPI()

@app.get('/api/healthcheck')
def get_healthcheck():
    return {'message' : 'all ok'}

@app.get('/api/treasures')
def get_treasures(max_age = None, min_age = None, colour = None, sort_by: str = Query(default="age", enum=["age", "cost_at_auction", "treasure_name"]), order: str = Query(default="ASC", enum=['ASC', 'DESC'])):
    conn = connect_to_db()
    sql_query = f'''SELECT treasure_id, treasure_name, colour, age, cost_at_auction, shop_name FROM treasures
                INNER JOIN shops ON treasures.shop_id = shops.shop_id '''
    if colour is not None:
        sql_query = sql_query + ' WHERE colour = :colour'
        if max_age is not None:
            sql_query = sql_query + ' AND colour = :colour'
    else:
        if max_age is not None:
            sql_query = sql_query + ' WHERE age < :max_age'
    if order is not None or sort_by is not None:
        sql_query = sql_query + f' ORDER BY {sort_by} {order}'
    response = conn.run(sql_query, colour=colour, max_age=max_age)
    answer = []
    keys = ['treasure_id', 'treasure_name', 'colour', 'age', 'cost_at_auction', 'shop_name']
    for t in response:
        m = dict(zip(keys, t))
        answer.append(m)
    return {'treasures' : answer}

class NewTreasure(BaseModel):
    treasure_name: str
    colour: str
    age: int
    cost_at_auction: float
    shop_id: int

@app.post('/api/treasures', status_code=201)
def post_treasure(new_treasure: NewTreasure):
    conn = connect_to_db()
    treasure_name = new_treasure.treasure_name
    colour = new_treasure.colour
    age = new_treasure.age
    cost_at_auction = new_treasure.cost_at_auction
    shop_id = new_treasure.shop_id
    insert_query = '''INSERT INTO treasures (treasure_name, colour, age, cost_at_auction, shop_id)
    VALUES(:treasure_name, :colour, :age, :cost_at_auction, :shop_id) RETURNING * ;'''
    response = conn.run(insert_query, treasure_name=treasure_name, colour=colour, age=age,
                        cost_at_auction=cost_at_auction, shop_id=shop_id)
    a =[]
    print(response)
    keys = ['treasure_name', 'colour', 'age', 'cost_at_auction', 'shop_id']

    del response[0][0]
    for t in response:
        m = dict(zip(keys, t))
        a.append(m)
    print(a)
    return a

class DiscountedTreasure(BaseModel):
    # treasure_id : int
    new_price : float

@app.patch('/api/treasures/{treasure_id}')
def patch_price(discounted_treasure: DiscountedTreasure, treasure_id):
    conn = connect_to_db()
    new_price = discounted_treasure.new_price
    # treasure_id = discounted_treasure.treasure_id
    patch_query = '''UPDATE treasures SET cost_at_auction = :new_price
    WHERE treasure_id = :treasure_id RETURNING *'''
    response = conn.run(patch_query, new_price=new_price, treasure_id=treasure_id)
    print(response)
    keys = ['treasure_id', 'treasure_name', 'colour', 'age', 'cost_at_auction', 'shop_id']
    response = response[0]
    m = dict(zip(keys, response))
    return {'treasure': m}

@app.delete('/api/treasures/{treasure_id}', status_code=204)
def delete_treasure(treasure_id: int):
    conn = connect_to_db()
    query = 'DELETE FROM treasures WHERE treasure_id = :treasure_id'
    conn.run(query, treasure_id=treasure_id)

@app.get('/api/shops')
def get_shops():
    conn = connect_to_db()
    sql_query = 'SELECT * FROM shops'
    response = conn.run(sql_query)
    answer = []
    keys = ['shop_id', 'shop_name', 'slogan']
    for t in response:
        m = dict(zip(keys, t))
        answer.append(m)
    for entry in answer:
        shop_id = entry['shop_id']
        stock_value_query = 'SELECT SUM(treasures.cost_at_auction) FROM treasures WHERE shop_id = :shop_id;'
        entry['stock_value'] = conn.run(stock_value_query, shop_id=shop_id)[0][0]
    return answer
