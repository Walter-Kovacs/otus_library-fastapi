"""
Create Read Update Delete
"""
from sqlalchemy import select, delete
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from api.schemas.author import AuthorIn, AuthorUpdate
from models import Author


# ***************************** CREATE *****************************
async def create_author(session: AsyncSession, api_author: AuthorIn) -> Author:
    author = Author(**api_author.dict())
    session.add(author)
    await session.commit()

    return author


# ***************************** READ *****************************
async def get_all_authors(session: AsyncSession) -> list[Author]:
    stmt = select(Author).order_by(Author.id)
    result: Result = await session.execute(stmt)
    authors = result.scalars().all()

    return authors


async def get_all_authors_order_by_name(session: AsyncSession) -> list[Author]:
    stmt = select(Author).order_by(Author.name)
    result: Result = await session.execute(stmt)
    authors = result.scalars().all()

    return authors


async def get_author_by_id(session: AsyncSession, author_id: int) -> Author | None:
    stmt = select(Author).where(Author.id == author_id)
    result: Result = await session.execute(stmt)
    author: Author | None = result.scalar_one_or_none()

    return author


# ***************************** UPDATE *****************************
async def update_author(session: AsyncSession, author_id: int, api_author: AuthorUpdate) -> Author | None:
    stmt = select(Author).where(Author.id == author_id)
    result: Result = await session.execute(stmt)
    author: Author | None = result.scalar_one_or_none()
    if author is not None:
        if api_author.name is not None:
            author.name = api_author.name
        if api_author.about is not None:
            author.about = api_author.about
        session.add(author)
        await session.commit()

    return author


# ***************************** DELETE *****************************
async def delete_author(session: AsyncSession, author_id: int):
    stmt = delete(Author).where(Author.id == author_id)
    await session.execute(stmt)
    await session.commit()
