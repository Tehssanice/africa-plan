from fastapi import APIRouter, Cookie, Header
from typing import Annotated
from pydantic import BaseModel, EmailStr

cookie_route = APIRouter()


class Person(BaseModel):
    user_id: str
    username: str
    password: str
    email: EmailStr


fake_db = {
    "1": {
        "Username": "Tessa",
        "email": "tessa@gmail.com",
        "password": "length123"
    },
    "2": {
        "Username": "Kosi",
        "email": "kosi@gmail.com",
        "password": "uhib3uy73"

    },
    "3": {
        "Username": "Collins",
        "email": "collins@gmail.com",
        "password": "24hggf"

    }
}


@cookie_route.get("/cookie_items/")
async def read_cookie_items(ads_id: str = Cookie()):
    return {"ads_id": ads_id}


@cookie_route.get("/cookie_items/")
async def read_items(user_agent: Annotated[str | None, Header()] = None):
    return {"User-Agent": user_agent}


@cookie_route.post("/person/", response_model=Person)
async def create_person(person: Person):
    fake_db[person.person_id] = person.dict()
    return fake_db


@cookie_route.get("/person/{person_id}")
async def read_person(person_id: str):
    return fake_db[person_id]
