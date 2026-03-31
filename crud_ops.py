from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel#library used for data validation in FastAPI
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):  #it inherits from the base model
    title: str
    content: str
    published: bool = True # optional field which is not required from client and by default its True
    rating: Optional[int] = None #rating field is also optional and by default its None
    
my_posts = [{"title": "title of post 1", "content": "Content of post1", "id": 1},
            {"title": "Favourite Foods", "content": "I like momos", "id": 2}
            ] #in program memory to store data coming!!


@app.get("/posts")
def get_posts():
    return {"data": my_posts}



@app.post("/posts")
def create_post(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}


@app.get("/posts/{id}")
def get_post(id):
    print(id)
    return {"post_detail": f"Here is post {id}"}