from fastapi import Body, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import model
from .database import engine
from .routers import post, user, auth, vote

# import psycopg2
# import time

# model.Base.metadata.create_all(bind=engine) (no need this, we have alembic now)

app = FastAPI()

#allow other requests from different domains to send request to this API.
origins = ["https://www.google.com"] #list of domains that can access or send requests to our api (useful when only providing access to our personal webapp)
app.add_middleware(CORSMiddleware, #function that runs before every request 
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
async def root():
    return {"message" : "hello world!!!!!!!!"}

# With JWT Authentication we do not store them in api or database but rather in the frontend. It is stateless,
# there is nothing in database to keep track of whether a user is logged in or not