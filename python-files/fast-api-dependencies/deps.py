from dbconfig import engine
from sqlmodel import Session


async def get_session():
    session = Session(engine)
    return session
