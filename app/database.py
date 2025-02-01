import os
import urllib.parse
from pathlib import Path
from typing import Callable

from dotenv import load_dotenv
from loguru import logger
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import DeclarativeMeta, Session, declarative_base, sessionmaker


class DatabaseInstance:
    _base: DeclarativeMeta = None

    def __init__(self):
        self._base = declarative_base()
        self._engine = create_engine(
            self.get_database_url(), connect_args={"check_same_thread": False}
        )
        self._session_maker = sessionmaker(autocommit=False, bind=self._engine)

    @property
    def base(self) -> DeclarativeMeta:
        return self._base

    @staticmethod
    def get_database_url() -> str:
        DATABASE_URL = "sqlite:///shortener.db"
        return DATABASE_URL

    def initialize_session(self) -> Session:
        return self._session_maker()

    def delete_all_tables_and_metadata(self):
        session = self.initialize_session()

        self.base.metadata.reflect(self._engine)
        self.base.metadata.drop_all(self._engine)

        session.commit()
        session.close()


def load_env():
    dotenv_file = Path(f"app/.env")
    load_dotenv(dotenv_file)
    logger.info(f'loaded env:{os.environ["ENV"]}')


load_env()
db_instance = DatabaseInstance()


def get_db_session():
    if hasattr(get_db_session, "_session") and not get_db_session._session.is_active:
        return get_db_session._session
    session = db_instance.initialize_session()
    get_db_session._session = session
    return session


def db_session_wrapper(func: Callable):
    def wrapped_func(*args, **kwargs):
        with get_db_session() as session:
            return func(*args, **kwargs)

    return wrapped_func


# def db_session_wrapper(func: Callable):
#     async def wrapped_func(*args, **kwargs):
#         async with get_db_session() as session:
#             return await func(*args, **kwargs)

#     return wrapped_func
