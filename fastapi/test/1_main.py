from fastapi import FastAPI

app = FastAPI()

@app.get(
    path = "/item/icecream",
    summary = "GET Summary",
    description = "GET Description",
    tags = ["GET Method"],
)
async def read_item_icecream():
    return {"item_name": "icecream"}

@app.get(
    path = "/items/{item_name}",
    summary = "GET Summary",
    description = "GET Description",
    tags = ["GET Method"],
)
async def read_item(item_name: str):
    return {"item_name": item_name}





# from typing import Union

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None

# @app.get("/root")
# def read_root():
#     return {"Hello": "World", "Read": "Root", "My": "Name", "Message": "Hello World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}
