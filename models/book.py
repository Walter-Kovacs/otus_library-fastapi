from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship

from . import Base


class Book(Base):
    __table_args__ = (
        UniqueConstraint('title', 'author_id', name='title_author_unique_constraint'),
    )

    title = Column(
        String(200),
        nullable=False,
    )
    author_id = Column(
        Integer,
        ForeignKey('authors.id'),
        nullable=False,
    )
    abstract = Column(
        Text,
    )
    count = Column(
        Integer,
    )

    author = relationship('Author', back_populates='books')
