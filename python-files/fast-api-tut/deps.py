from main import engine, Session


async def get_session():
    session = Session(engine)
    return session
