from pymongo import MongoClient
import pymongo
from fastapi import FastAPI

app = FastAPI()


def get_database():
    import pymongo

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://eze:fVIJCdJiV53m7Thl@cluster0.pzvwq.mongodb.net/?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)
    # Create the database for our example (we will use the same database throughout the tutorial
    return client['personajes']

# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":    
    dbname = get_database()

@app.get("/getprueba")
def get_base():
    dbname = get_database() 
    
    collection_name = dbname["personajes"]

    item_1 = {
        "nombre" : "carlitos",
        "edad" : 76
    }
    item_2 = {
        "nombre" : "Marcelo",
        "edad" : 26
    }
    collection_name.insert_many([item_1,item_2])
    item_3 = {
        "nombre" : "eduardo",
        "edad" : 26,
        "cantidad de años":26
    }
    collection_name.insert_one(item_3)


    return dbname

global IMAGENES 

IMAGENES = {
    "obi-wan-kenobi": "https://elcomercio.pe/resizer/Y_vWseScianc2lT4mmoJxsDerds=/1200x1200/smart/filters:format(jpeg):quality(75)/cloudfront-us-east-1.images.arcpublishing.com/elcomercio/LO425SZFO5DONMKILCFEAUU2XE.jpg"
}