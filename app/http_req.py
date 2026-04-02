from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.post("/post")

def create_post(payload: dict = Body(...)):
    print(payload)
    return {"data": "Post has been created"}