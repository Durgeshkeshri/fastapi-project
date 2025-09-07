from typing import Union

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from pydantic import BaseModel

"""
import orjson

import orjson

# Python dict → JSON bytes
json_bytes = orjson.dumps({"foo": "bar"})
print(json_bytes)  # b'{"foo":"bar"}'

# Bytes → String
json_str = json_bytes.decode("utf-8")
print(json_str)    # {"foo":"bar"}

# JSON (bytes) → Python dict
data = orjson.loads(json_bytes)
print(data)        # {'foo': 'bar'}


"""

app = FastAPI(default_response_class=ORJSONResponse)

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool,None] = None

@app.get("/")
def read_root():
    return {'data':'Hello World'}


@app.get("/fast-items/{item_id}", response_class=ORJSONResponse) # to use orjson response for specific route
def read_item(item_id: int):
    return {"item_id": item_id, "message": "This uses orjson!"}

@app.get(f"/items/{{item_id}}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put(f"/items/{{item_id}}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item": item}


