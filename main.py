from typing import Union

from fastapi import FastAPI

import json, requests, unittest

from pymongo import MongoClient

from bson.json_util import dumps, loads

from bson.objectid import ObjectId

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/getSingleProduct/{item_id}")
def getOne(item_id: str):

        client = MongoClient("mongodb://root:example@localhost:27017/")

        db = client.auto_products

        collection = db.auto_products


        # ID of the object

        query = {"_id": ObjectId(item_id)}

        filter = {"_id": 0}

        # find it
        results = collection.find_one(query, filter)
        print(results)

        # dump to JSON
        results = dumps(results)

        #return
        return json.loads(results)


@app.get("/getAll")
def getAll():
        client = MongoClient("mongodb://root:example@localhost:27017/")

        db = client.auto_products

        collection = db.auto_products

        # find it
        results = collection.find()
        print(results)

        # dump to JSON
        results = dumps(results)

        #return
        return json.loads(results)

@app.get("/addNew")
def read_root():
        client = MongoClient("mongodb://root:example@localhost:27017/")

        db = client.auto_products

        collection = db.auto_products


        # Record to be inserted

        newRecord= {"Product ID": "AUTO014", "Name": "Wheels", "Unit Price": 200.00, "Stock Quantity": 2, "Description": "High-Quality Wheels"}


        # find it
        res = collection.insert_one(newRecord)



@app.get("/deleteOne")
def read_root():
        client = MongoClient("mongodb://root:example@localhost:27017/")

        db = client.auto_products

        collection = db.auto_products


        # Record to be deleted

        deleteRecord= {"Product ID": "AUTO014"}


        # find it
        res = collection.delete_one(deleteRecord)

@app.get("/startsWith/{letter}")
def read_root(letter: str):
        client = MongoClient("mongodb://root:example@localhost:27017/")

        db = client.auto_products

        collection = db.auto_products

        query = {"Name": {"$regex": f"^{letter}", "$options": "i"}}  

        filter = {"_id": 0}

        results = collection.find(query, filter)

        return json.loads(dumps(results))

@app.get("/paginate/{start_id}/{end_id}")
def paginate_products(start_id: str, end_id: str):
        client = MongoClient("mongodb://root:example@localhost:27017/")

        db = client.auto_products

        collection = db.auto_products

        query = {
                "Product ID": {"$gte": start_id, "$lte": end_id}
        }
        filter = {"_id": 0}  
        
        results = collection.find(query, filter)  
        
        return json.loads(dumps(results))

@app.get("/convert/{item_id}")
def read_root(item_id: str):

        client = MongoClient("mongodb://root:example@localhost:27017/")

        db = client.auto_products

        collection = db.auto_products
   

        # ID of the object

        query = {"_id": ObjectId(item_id)}

        filter = {"_id": 0}

        # find it
        results = collection.find_one(query, filter)
        print(results)

        unit_price = results.get("Unit Price", 0)

        r = requests.get('https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_B9FEsBVoE7vuGfuReCHDJvlPKjB2owovnmUMrrEJ')

        convertAmount = r.json()
        new_convertAmount = convertAmount['data']['EUR']

        newAmount = unit_price * new_convertAmount

        print(unit_price)
        print(newAmount)

        # dump to JSON
        results = dumps(results)

        #return
        return json.loads(results), unit_price, newAmount



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
