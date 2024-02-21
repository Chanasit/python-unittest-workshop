from typing import Union
from fastapi import FastAPI, APIRouter
from app.repositories.random import RandomRepository
from app.services.calculator import CalculatorService
from app.utils.log import logging

app = FastAPI()
router = APIRouter()
rand_repo = RandomRepository()
cal_srv = CalculatorService(rand_repo)


@router.get("/")
async def read_root():
    logging.debug("GET /")
    number = str(cal_srv.random_with_constant(2021))
    return {"Hello": "World " + number}


@router.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    logging.debug("GET /item/{}".format(item_id))
    return {"item_id": item_id, "q": q}


app.include_router(router)
