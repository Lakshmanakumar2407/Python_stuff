import time
from typing import Optional
from fastapi import FastAPI, Response, HTTPException, status
from fastapi.params import Body
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

# Creatin the base model
class PostModel(BaseModel):
    title :str
    content: str
    published: Optional[bool] = True

while True:
    try:
        conn = psycopg2.connect(host = 'localhost',
                                database = "Fast_api_CRUD", 
                                user = "postgres",
                                password = 'root',
                                cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Connection Successful")
        break
    except Exception as error:
        print('Error occured')
        print('error - ', error)
        print()
        print('Retrying after 5 Seconds...')
        time.sleep(5)

# RETRIEVE/ READ
@app.get('/')
def home():
    return {'Response':'Welcome to Posts Home page'}

@app.get('/posts')
def get_posts():
    cursor.execute("SELECT * FROM public.posts")
    all_posts = cursor.fetchall()

    return {'Posts':all_posts}

@app.get('/posts/latest')
def get_latest_posts():
    cursor.execute("""SELECT title, content, created_at FROM public.posts 
                   ORDER BY created_at DESC 
                   LIMIT 1""")
    latest_post = cursor.fetchone()

    return {'Latest_post':latest_post}

@app.get('/posts/{id}')
def get_posts_by_id(id: int):
    post_id = str(id)

    # should convert id back to str in the sql field and not in argument beacuse the user may input some string there
    cursor.execute("SELECT title, content, created_at FROM public.posts WHERE id = %s", (post_id,))
    specific_post = cursor.fetchall()


    if len(specific_post)==0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id = {post_id} was not found")

    return {'Post': specific_post}

@app.get('/posts/latest/limit={num}')
def get_latest_posts_by_limit(num: int):
    post_num = str(num)
    
    cursor.execute("""SELECT title, content, created_at FROM public.posts 
                   ORDER BY created_at DESC 
                   LIMIT %s""", (post_num,))
    
    latest_posts = cursor.fetchall()
    return {"Latest Posts" : latest_posts}


# CREATE
@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_post(input_post: PostModel = Body(), response = Response):
    title = input_post.title
    content = input_post.content
    publish = input_post.published

    cursor.execute("INSERT INTO public.posts(title, content, published) VALUES(%s, %s, %s) RETURNING title, content",
                   (title, content, publish))
    new_post = cursor.fetchall()

    conn.commit()

    return {'msg':'Post_created', 'Post':new_post}


# UPDATE
@app.put('/posts/{id}')
def update_post(id: int, updated_post: PostModel = Body(...)):
    post_id = str(id)
    updated_title = updated_post.title
    updated_content = updated_post.content

    cursor.execute("""UPDATE public.posts 
                   SET title = %s, 
                   content = %s WHERE id = %s 
                   RETURNING *""", (updated_title, 
                                    updated_content,
                                    post_id))
    conn.commit()
    updated = cursor.fetchone()

    return {'Updated Post':updated}


# DELETE
@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    post_id = str(id)

    cursor.execute("""DELETE FROM public.posts 
                   WHERE id = %s 
                   RETURNING * """, (post_id,))
    deleted_post = cursor.fetchone()
    conn.commit()

    if deleted_post == None:    
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Post Not found in Database')
    
    return None