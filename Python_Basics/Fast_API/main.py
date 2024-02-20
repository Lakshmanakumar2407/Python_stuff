from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def test_message():
    return {'message':'Hello Worl'}

@app.get("/posts")
def get_posts():
    return {'msg':'Your posts are displayed here'}