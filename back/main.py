from typing import Dict
from fastapi import FastAPI, Query
import pandas as pd
from pandasql import sqldf

from utils import construct_sql_command, construct_test_date

app = FastAPI()

products = pd.read_csv('/app/data/data.csv', sep=';')

test = pd.DataFrame(construct_test_date())

@app.get('/products/', response_model=Dict[int, int])
def get_products(percentage_threshold = 10, euro_threshold = 20, last_two = False):
    sql_command = construct_sql_command('products', percentage_threshold, euro_threshold, last_two)
    sql_result = sqldf(sql_command)
    result = {row['product']: row['price_variation'] for _, row in sql_result.iterrows()}
    return result

@app.get('/test/', response_model=Dict[int, int])
def get_test_products(percentage_threshold = 10, euro_threshold = 20, last_two = False):
    sql_command = construct_sql_command('test', percentage_threshold, euro_threshold, last_two)
    sql_result = sqldf(sql_command)
    result = {row['product']: row['price_variation'] for _, row in sql_result.iterrows()}
    return result
