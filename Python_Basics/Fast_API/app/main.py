from fastapi import FastAPI, Response, status, HTTPException
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

class customModel_patch(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    update: bool = True

app = FastAPI()

post_storer = list()

@app.get("/")
def test_message():
    return {'message':'Hello World'}

@app.get("/posts")
def get_posts():
    return {'posts': post_storer}

@app.get("/posts/{id}")
def get_posts_by_id(id: int, response: Response):
    temp = None
    
    for posts in post_storer:
        if posts['id'] == id:
            temp =  {'post': posts}
            return {'Post-Detail':temp}
    
    if temp == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id - {id} was not found",
                            headers={'test-header':'test-header'})

        # The below code can be coverted to single line which was performed above
        # response.status_code = 404 # instead of remembering this we can use status
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'msg':f'Post with id - {id} was not found'}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def post_posts(user_payload: customModel = Body(...)):
    # print(user_payload, type(user_payload))

    diction = user_payload.model_dump()
    diction.update({'id':randrange(1,100)})
    post_storer.append(diction)
    # print(diction)

    if user_payload.published == True :
        # raise HTTPException(status_code=status.HTTP_201_CREATED, detail=f'Your Post was successfully created with id - {diction[id]}')
        # Instead of the above cde, we can simply pass it in paramter
        return {"data":[user_payload, f"your data is stored with id - {diction["id"]}"]}
    else:
        return f'Published value is false'
    
@app.delete("/posts/{id}")
def delete_post(id: int):
    id_found = None

    for index, post in enumerate(post_storer):
        if post['id'] == id:
            id_found = True
            del post_storer[index]
            # return f'Deleted post with id = {id}' # since the reponse is 204, It isn't logical to have return content
            # so we can do it in thisway
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,
                                detail='Deleted')
    
    if id_found is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Post Not Found")


def get_user_specified_post(post_id):
    global post_storer
    for post in post_storer:
        if post['id'] == post_id:
            return post

@app.patch("/posts/{id}")
def update_posts(id: int, user_payload: customModel_patch = Body()):

    post = get_user_specified_post(id)

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f'Post was not found')

    user_payload_dict = user_payload.model_dump()

    if user_payload.update == True:
        for key,val in user_payload_dict.items():
            if key is not None:
                post[key] = val
                return f'Value updated'
    else:
        return f"You don't want it to be updated"
    

@app.put("/posts/{id}")
def full_update_post(id: int, user_payload: customModel = Body()):
    post = get_user_specified_post(id)
    flag = None

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f'Post was not found')

    user_payload_dict = user_payload.model_dump()

    for key, value in user_payload_dict.items():
        post[key] = value
        flag = True

    if flag == True:
        return Response(status_code=status.HTTP_200_OK,
                        content = 'Value Updated dude')

# i think put is better than patch 
