from sqlalchemy import create_engine

from api.models.notifications import Base

import os
from dotenv import load_dotenv
load_dotenv()

ASYNC_DB_URL = os.environ['ASYNC_DB_URL']

engine = create_engine(ASYNC_DB_URL, echo=True)


def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()
