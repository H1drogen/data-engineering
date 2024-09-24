import pandas as pd
import json


def create_df(filename):
    with open(filename, 'r') as file:
        data = json.load(file)['doughnut_data']
        df = pd.DataFrame(data)
    return data


def increase_price(df):
    pass

def get_best_value(df):
    pass

create_df('../data/doughnuts.json')