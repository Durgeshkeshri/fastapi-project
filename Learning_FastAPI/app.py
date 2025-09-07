from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel
from typing import Annotated, List


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.put("/items/{item_id}")
async def update_item(item_id: Annotated[int,Path(ge=1, le=100)], item: Item, q: Annotated[str | None, Query(min_length=3, max_length=50) ]= None):
    result = {"item_id": item_id, **item.model_dump(exclude={"in_stock"})}
    if q:
        result.update({"q": q})
    return result

@app.get("/items/")
async def read_items(q: List[str] = Query(...)): # makes it required, with no default value
    return {"q": q}

