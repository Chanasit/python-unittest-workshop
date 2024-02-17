from typing import Union
from fastapi import FastAPI

app = FastAPI()

import os
print(os.getenv("AWS_KEY"))


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
