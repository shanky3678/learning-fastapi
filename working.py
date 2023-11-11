from fastapi import FastAPI, Path;
from enum import Enum
from typing import Union, List, Optional

app = FastAPI()

inventory = {
    1: {
        'Name': 'How To Talk To Anyone',
        'Price': '399$',
        'brand':'bookshop'
    },
    2: {
        'Name': 'Book2',
        'Price': '199$',
        'brand':'bookshop'
    },
    3: {
        'Name': 'Book3',
        'Price': '599$',
        'brand':'bookshop'
    }
}

class ModelName(Enum):
    showDialog = 'ShowDialog'
    reset = 'Reset'
    lenet = "lenet"

@app.get('/')
def home():
    return 'Welcome to book FAST API.';

@app.get('/get-book/{item_id}')
def getBook(item_id: int = Path(description="The ID of the item that you would like to view.",gt=0,lt=4)):
    return inventory[item_id];


@app.get('/get-all/{item_id}')
def getall(*,item_id: int , q: str| None = None):
    return {"item_id": item_id, "q": q}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.showDialog:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == ModelName.reset:
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@app.put('/update-data/')
def updateDataToDatabase():
    return "";
