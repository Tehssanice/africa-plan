from fastapi import FastAPI, HTTPException
from typing import List
from uuid import uuid4, UUID
from models import User, Gender, Role, UpdateUser

app = FastAPI()


database: List[User] = [
    User(
        id=uuid4(),
        first_name="Jamila",
        last_name="Ahmed",
        middle_name="Jacob",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=uuid4(),
        first_name="Ken",
        last_name="Brian",
        middle_name="Tina",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )

]


@app.get("/")
async def print_test():
    return ({"name": "Tessa"})


@app.get("/api/v1/users")
async def fetch_users():
    return database


@app.post("/api/v1/users")
async def register_user(user: User):
    database.append(user)
    return {"id": user.id}


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in database:
        if user.id == user_id:
            database.remove(user)
            return
        raise HTTPException(
            status_code=404,
            detail=f"user with id: {user_id} does not exist"
        )


@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UpdateUser, user_id: UUID,):
    for user in database:
        if user.id == user_id:

            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.last_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return

        raise HTTPException(
            status_code=404,
            detail=f"user with id: {user_id} does not exist"
        )
