from fastapi import FastAPI
from . import schemas, models
from .database import engine
app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.post('/blog')

def index(blog:schemas.Blog):
    return {'data':{'name':f'Blog title {blog.name}'}}

