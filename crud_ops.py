from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel#library used for data validation in FastAPI
from typing import Optional
from random import randrange
from fastapi import Response, status, HTTPException

app = FastAPI()

class Post(BaseModel):  #it inherits from the base model
    title: str
    content: str
    published: bool = True # optional field which is not required from client and by default its True
    rating: Optional[int] = None #rating field is also optional and by default its None
    
my_posts = [{"title": "title of post 1", "content": "Content of post1", "id": 1},
            {"title": "Favourite Foods", "content": "I like momos", "id": 2}
            ] #in program memory to store data coming!!

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


@app.get("/posts")
def get_posts():
    return {"data": my_posts}



@app.post("/posts")
def create_post(post: Post, status_code = status.HTTP_201_CREATED): #if we want to throw a specific HTTP status code , pass it as parameter in the function
    post_dict = post.dict()
    post_dict['id'] = randrange(0,1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/latest")
def get_latest_post():
    post = my_posts[len(my_posts) - 1]
    return {"detail": post}
#path order matters over here if this end point is put below the next function it will throw an error as FastAPI doesn't know the difference b/w /posts/latest and /posts/{id}

@app.get("/posts/{id}") #get post by id.....#id is the path parameter
def get_post(id: int, response: Response):  #validation -> id is getting converted to int if not 
    post = find_post(id)
    # if not post:
    #     response.status_code = 404 #used to throw an 404 error if requestes resource is not available
    #     return {"message": f"Post with id: {id} was not found"} #it will pass this message if resource is not available
    if not post: #using exception handling(in-built in FastAPI rather than hard coding like above)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not found")
    return {"post_detail": f"Here is post {id}"}

