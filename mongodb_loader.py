import pandas as pd
from pymongo import MongoClient


def _mongo_connect(db):
    client = MongoClient()
    database = client[db]
    return database

def read_mongo(db, collection, query={}, no_id=True):
    database = _mongo_connect(db)
    data = database[collection].find(query)
    dataframe =  pd.DataFrame(list(data))

    # Delete the _id
    if no_id and '_id' in dataframe.keys():
        del dataframe['_id']

    return dataframe