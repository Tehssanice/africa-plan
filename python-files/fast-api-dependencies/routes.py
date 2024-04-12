from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from typing import Annotated
from deps import get_session
from models import UserCreate, User
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

router = APIRouter(prefix="/userdeps")


@router.post("/user")
async def create_user(user: UserCreate, session: Annotated[Session, Depends(get_session)]):
    user_1 = User(name=user.name, age=user.age,
                  is_married=user.is_married, gender=user.gender)
    session.add(user_1)
    session.commit()

    update_user = {"name": user.name, "age": user.age,
                   "is_married": user.is_married, "gender": user.gender}

    response = {"message": "complete",
                "data": jsonable_encoder(update_user)}

    return JSONResponse(status_code=201, content=response)


@router.get("/user")
async def get_all_user(session: Annotated[Session, Depends(get_session)]):

    user_1 = session.exec(select(User)).all()
    return user_1
