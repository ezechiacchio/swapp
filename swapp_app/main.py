from pydantic import BaseModel
from pymongo import MongoClient
from fastapi import FastAPI
from requests import Response

app = FastAPI()

class Modelo_post(BaseModel):
    pj_name : str
    user_name :str

def get_database():

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://eze:fVIJCdJiV53m7Thl@cluster0.pzvwq.mongodb.net/?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING,connect=False)
    # Create the database for our example (we will use the same database throughout the tutorial
    return client['personajes']


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
    dbname = get_database()


@app.post("/chequearrelacion")
async def get_rel(item:Modelo_post):
    dbname = get_database()
    collection_name = dbname['personajes']
    buscado = {
            "_id":str(item.pj_name+item.user_name).replace(' ','_')
                }
    encontrado = False
    x = (collection_name.find({}))
    for elemento in x:
        if elemento['_id'] == buscado["_id"]:
            encontrado=True
            print(encontrado)
            break
    response = Response()
    response.encontrado = encontrado
    return response


@app.post("/guardardatos")
async def enviar_datos(item:Modelo_post):
    dbname = get_database()

    collection_name = dbname["personajes"]
    item = {
            "_id": str(item.pj_name) + str(item.user_name),
            "pj" :item.pj_name,
            "user":item.user_name}
    try:
        collection_name.insert_one(item)
    except Exception as e :
        print(e)
    return item

@app.get("/seguidos")
async def obtener_seguidos(user:str =""):
    dbname = get_database()
    collection_name = dbname["personajes"]
    lista_seguidos = []
    x = collection_name.find()
    for elemento in x:
        if elemento.get("user",None) == user:
            lista_seguidos.append(elemento.get("pj"))
    response = Response()
    response.lista_seguidos = lista_seguidos 
    return response
