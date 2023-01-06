from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "*",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def homePage():
    return {"data": {"message": "Home Page"}}


@app.get('/store')
async def storePage():
    return {"data": {"message": "Store Page"}}
