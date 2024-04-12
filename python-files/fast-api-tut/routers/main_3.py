from fastapi import APIRouter, Depends
from sqlmodel import SQLModel, Field, create_engine, Session, select
from typing import Annotated
from enum import Enum
from deps import get_session

field = APIRouter(prefix="/fields")


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


sqlite_file_name = "clientbase.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

SQLModel.metadata.create_all(engine)


@field.post("/user/")
async def create_user(user: UserCreate, session: Annotated[Session, Depends(get_session)]):
    with Session(engine) as session:
        user_1 = User(name=user.name, age=user.age,
                      is_married=user.is_married, gender=user.gender)
        session.add(user_1)
        session.commit()

    return {"name": user.name, "age": user.age, "is_married": user.is_married, "gender": user.gender}


@field.get("/user/")
async def get_all_user():

    with Session(engine) as session:
        user_1 = session.exec(select(User)).all()
        return user_1
