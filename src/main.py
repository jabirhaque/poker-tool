from typing import List, Annotated
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from model import Game, Card
from service import probability

app = FastAPI()

origins = [
    "http://127.0.0.1:8000",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test")
async def test(item: Annotated[list[str] | None, Query()] = None, type: str = None):
    return {"list of items": item,
            "type": type}

@app.get("/get_probability")
async def get_probability(pocket: Annotated[list[str] | None, Query()] = None, community: Annotated[list[str] | None, Query()] = None, opponent_num: int = None):
    # http://127.0.0.1:8000/get_probability?pocket=TD&pocket=3S&community=TH&community=4S&community=2C&opponent_num=1
    pocket = [Card(key) for key in pocket]
    community = [Card(key) for key in community]
    game = Game(pocket, community, opponent_num, [])
    return {'probability': probability(game)}