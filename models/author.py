from sqlalchemy import (
    Column,
    String,
    Text,
)
from sqlalchemy.orm import relationship

from . import Base


class Author(Base):
    name = Column(
        String(100),
        nullable=False,
        unique=True,
    )
    about = Column(
        Text,
    )

    books = relationship('Book', back_populates='author')
