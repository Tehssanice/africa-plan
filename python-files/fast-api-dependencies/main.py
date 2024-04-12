from fastapi import FastAPI
from routes import router
from dbconfig import engine
from sqlmodel import SQLModel


app = FastAPI()

app.include_router(router)


@app.on_event("startup")
async def startup():
    SQLModel.metadata.create_all(engine)
