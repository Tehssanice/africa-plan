from fastapi import FastAPI
from enum import Enum

app = FastAPI()

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


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]


@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]


@app.get("/colours/{colour_name}")
def get_colours(colour_name: Colours):
    return {f"{colour_name.name}, is a beautiful color"}

 #####################################
 # Query parameters


fake_items_db = [{"item_name": "Foo"}, {
    "item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]
