from pydantic import BaseModel
from fastapi import FastAPI, Query, Path
from enum import Enum
from typing import Annotated
from routers import main_2


app = FastAPI()
app.include_router(main_2.router)


database = {
    "1": {
        "name": "clara Jones",
        "age": 40,
    },

    "2": {
        "name": "Collins Jones",
        "age": 49,

    }
}


class Colours(str, Enum):
    teal = "teal"
    brown = "brown"
    paleyelllow = "paleyelllow"


@app.get("/")
def read_root():
    return {"Hello": "African plan"}


@app.post("/")
def post_root():
    return {"Hello": "I sent a post request"}


@app.put("/")
def put_root():
    return {"Hi": "This is a pit request"}


@app.delete("/")
def delete_root():
    return {"Hey": "I sent a delete request"}


@app.patch("/")
def patch_root():
    return {"People": "I made a patch request"}


#################################

# Path Parameters

@app.get("/members/{member_id}")
def get_members(member_id: str):
    return database[member_id]


@app.get("/products/me")
async def read_user_me():
    return {"product_id": "the current user"}


@app.get("/countries/{country_id}")
async def read_country(user_id: str):
    return {"country_id": user_id}


@app.get("/managers")
async def read_managers():
    return ["Bean", "Elfo"]


@app.get("/colours/{colour_name}")
def get_colours(colour_name: Colours):
    return {f"{colour_name.name}, is a beautiful color"}


#####################################
 # Query parameters


fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"}
]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10, ):
    return fake_items_db[skip: skip + limit]


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


#####################################
# Request body


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.post("/items/")
async def create_item(item: Item):
    return item


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, ** item.model_dump()}


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, ** item.model_dump()}
    if q:
        result.update({"q": q})
    return result


##################################
# Query Parameters and String Validations

@app.get("/items/")
async def read_items(q: str | None = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/")
async def read_items(q: Annotated[str, Query(min_length=3)]):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/")
async def read_items(q: Annotated[list[str] | None, Query()] = None):
    query_items = {"q": q}
    return query_items


#######################################
# Path Parameters and Numeric Validations

@app.post("/items/{item_id}", deprecated=True)
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/{item_id}")
async def read_items(q: str, item_id: int = Path(title="The ID of the item to get")):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")], q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
