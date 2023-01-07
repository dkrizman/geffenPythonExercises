import pandas as pd
import pymongo as pm 
from pymongo import MongoClient
from pandas.io.json import json_normalize

def get_db(host, db_name, collectionName):
    client = MongoClient(host)
    db = client[db_name]
    collection = db[collectionName]
    return collection

def getDbNames(host):
    client = MongoClient(host)
    dataBases = client.list_database_names()
    return dataBases

def getCollections(host, db_name):
    client = MongoClient(host)
    db = client[db_name]
    collections = db.list_collection_names()
    return collections

if __name__ == '__main__':
    import pandas_profiling as ppf
    stocks = get_db('localhost:27017', 'dan1', 'stocks2015')
    res = stocks.find({}).limit(110)
    l = list(res)
    df = pd.DataFrame(l)
    df.drop(['_id'], axis=1, inplace = True)
    j = df.to_json(date_format='iso', orient='split')
    profile = ppf.ProfileReport(df, minimal=True,title='Pandas Profiling Report', progress_bar=True )
    profile.to_file(output_file="C:\\Users\\dkrizman\\Desktop\\temp\output.html")