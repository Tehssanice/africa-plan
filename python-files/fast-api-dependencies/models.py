from sqlmodel import SQLModel, Field
from enum import Enum


class Gender(str, Enum):
    male = "male"
    female = "female"


class UserCreate(SQLModel):
    name: str
    age: int
    is_married: bool
    gender: Gender


class User(UserCreate, table=True):
    id: int | None = Field(default=None, primary_key=True)
