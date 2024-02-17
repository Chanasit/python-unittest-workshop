from typing import Union
from fastapi import FastAPI
from app.repositories.random import RandomRepository
from app.services.calculator import CalculatorService

app = FastAPI()
rand_repo = RandomRepository()
cal_srv = CalculatorService(rand_repo)


@app.get("/")
async def read_root():
    number = str(cal_srv.random_with_constant(2021))
    return {"Hello": "World " + number }


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
