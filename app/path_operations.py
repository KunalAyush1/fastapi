from fastapi import FastAPI

app = FastAPI()
@app.get("/")

def get_posts():
	return {"data": "These are your posts"}