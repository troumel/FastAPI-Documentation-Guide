from fastapi import FastAPI
from enum import Enum

app = FastAPI()


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/items/{item_id}")
def read_item(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model": ModelName.alexnet}

    if model_name == ModelName.resnet:
        return {"model": ModelName.resnet}

    if model_name == ModelName.lenet:
        return {"model": ModelName.lenet}

    return {"model": "unknown"}
