from sqlalchemy import (
    Column,
    Integer,
)
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import (
    declared_attr,
    declarative_base,
)

import config


class Base:
    @declared_attr
    def __tablename__(cls):
        return f'{cls.__name__.lower()}s'

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)
engine = create_async_engine(url=config.DB_URL_ASYNC, echo=config.DB_ECHO)
