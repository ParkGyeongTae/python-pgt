from enum import Enum

from fastapi import FastAPI

app = FastAPI()

class ModelName(str, Enum):
    icecream = "아이스크림"
    snack = "과자"
    chocolate = "초콜렛"

@app.get(
    path = "/item/price",
    summary = "Summary",
    description = "Description",
    tags = ["Tags"],
)
async def read_price(item_name: ModelName):
    if item_name is ModelName.icecream:
        price = 3000
    elif item_name is ModelName.snack:
        price = 5000
    elif item_name is ModelName.chocolate:
        price = 7000
    else:
        pass
    return {"item_name": item_name, "price": price}
