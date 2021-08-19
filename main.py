from fastapi import FastAPI
from uuid import uuid4
from pydantic import BaseModel

# uuid4.new()
# id = uuid4()

app = FastAPI()
items = [ 
    {'id': 'cda02c8e-408b-412e-8697-b2f083e2a859', 'name': 'paper1'},
    {'id': 'cda02c8e-408b-412e-8697-b2f083123859', 'name':'pencil1'},
    {'id': 'cda02c8e-408b-142e-8697-b2f083e2a859', 'name':'pencil2'},
    {'id': 'cda02c8e-4023-412e-8697-b2f083e2a859', 'name':'pencil3'},
    {'id': 'c232c28e-408b-412e-8697-b2f083e2a859', 'name': 'paper4'},
    {'id': 'cda1428e-408b-412e-8697-b2f083e2a859', 'name':'pencil5'},
    {'id': 'cda0248e-408b-412e-8697-b2f083e2a859', 'name':'pencil6'},
    {'id': 'cda02c8e-408b-432e-8697-2f0123e2a859', 'name':'pencil7'},
    {'id': '12311222-408b-412e-8697-b2f083e2a859', 'name':'pencil8'},
    {'id': 'cda02c8e-408b-412e-8697-123f083e2a83', 'name':'pencil9'}
    ]

@app.get("/")
def read_root():
    return {"Hello": "World"}

class Item(BaseModel):
    user_id:str
    password: str

@app.get("/items/{items_id}")
def read_item(items_id: str):
    for i in range(len(items)):
       if items[i]['id'] == items_id:
        return {"name": items[i]['name']}
    
# get post(create) patch(update) delete(delete)!

@app.post("/items")
async def create_item(item: Item):
    items.append(items.dict())
    return items

@app.patch("/items/")
async def update_item(item: Item):
    return 0

@app.delete("/items/{items_id}")
async def delete_item(item: Item):
    return 0