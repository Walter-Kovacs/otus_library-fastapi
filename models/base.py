from sqlalchemy import (
    Column,
    Integer,
)
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
