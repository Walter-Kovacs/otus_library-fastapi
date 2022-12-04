"""
Create Read Update Delete
"""
from sqlalchemy import select, delete
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from api.schemas.book import BookIn, BookUpdate
from models import Book


# ***************************** CREATE *****************************
async def create_book(session: AsyncSession, api_book: BookIn) -> Book:
    book = Book(**api_book.dict())
    session.add(book)
    await session.commit()

    return book


# ***************************** READ *****************************
async def get_all_books(session: AsyncSession, order_by: str = "") -> list[Book]:
    stmt = select(Book)
    if order_by == "title":
        stmt.order_by(Book.title)
    else:
        stmt.order_by(Book.id)
    result: Result = await session.execute(stmt)
    books = result.scalars().all()

    return books


async def get_books_by_author_id(session: AsyncSession, author_id: int, order_by: str = "") -> list[Book]:
    stmt = select(Book).where(Book.author_id == author_id)
    if order_by == "title":
        stmt.order_by(Book.title)
    else:
        stmt.order_by(Book.id)
    result: Result = await session.execute(stmt)
    books = result.scalars().all()

    return books


async def get_book_by_id(session: AsyncSession, book_id: int) -> Book | None:
    stmt = select(Book).where(Book.id == book_id)
    result: Result = await session.execute(stmt)
    book: Book | None = result.scalar_one_or_none()

    return book


# ***************************** UPDATE *****************************
async def update_book(session: AsyncSession, book_id: int, api_book: BookUpdate) -> Book | None:
    stmt = select(Book).where(Book.id == book_id)
    result: Result = await session.execute(stmt)
    book: Book | None = result.scalar_one_or_none()
    if book is not None:
        if api_book.title is not None:
            book.title = api_book.title
        if api_book.abstract is not None:
            book.abstract = api_book.abstract
        if api_book.count is not None:
            book.count = api_book.count
        session.add(book)
        await session.commit()

    return book


# ***************************** DELETE *****************************
async def delete_book(session: AsyncSession, book_id: int):
    stmt = delete(Book).where(Book.id == book_id)
    await session.execute(stmt)
    await session.commit()
