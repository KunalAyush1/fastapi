from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel#library used for data validation in FastAPI
from typing import Optional


app = FastAPI()

class Post(BaseModel):  #it inherits from the base model
    title: str
    content: str
    published: bool = True # optional field which is not required from client and by default its True
    rating: Optional[int] = None #rating field is also optional and by default its None

@app.post("/post")
def root(new_post: Post):
    print(new_post.published) #prints the data coming from client side after validation
    print(new_post.rating)
    new_post.dict() #makes the data to a Python's dictionary
    return {"data": new_post}
    