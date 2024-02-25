from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

class customModel(BaseModel):
    title: str
    content: str
    published: bool = True
    store: bool = True
    rating: Optional[int] = None

app = FastAPI()

post_storer = list()

@app.get("/")
def test_message():
    return {'message':'Hello World'}

@app.get("/posts")
def get_posts():
    return {'posts': post_storer}

@app.get("/posts/{id}")
def get_posts_by_id(id):
    temp = None
    
    for posts in post_storer:
        # print(posts['id'], type(posts['id']), id, type(id))
        if posts['id'] == int(id):
            print(id)
            temp =  {'post': posts}
            break

    return temp


@app.post("/posts")
def post_posts(user_payload: customModel = Body(...)):
    # print(user_payload, type(user_payload))

    diction = user_payload.model_dump()
    diction.update({'id':randrange(1,10000000000)})
    post_storer.append(diction)
    # print(diction)

    if user_payload.published == True :
        return {"data":[user_payload, f"your data is stored with id - {diction["id"]}"]}
    else:
        return f'Published value is false'