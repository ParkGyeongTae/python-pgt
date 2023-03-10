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
