from fastapi import FastAPI

app = FastAPI()

@app.get("/getprueba")
def get_iris():
    return "holamundo"
