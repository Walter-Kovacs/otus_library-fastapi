"""
Create Read Update Delete
"""
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from api.schemas.author import AuthorIn
from models import Author


# Create
async def create_author(session: AsyncSession, api_author_in: AuthorIn) -> Author:
    author = Author(**api_author_in.dict())
    session.add(author)
    await session.commit()

    return author


# Read
async def get_all_authors(session: AsyncSession) -> list[Author]:
    stmt = select(Author).order_by(Author.id)
    result: Result = await session.execute(stmt)
    authors = result.scalars().all()

    return authors


async def get_author_by_id(session: AsyncSession, author_id: int) -> Author | None:
    stmt = select(Author).where(Author.id == author_id)
    result: Result = await session.execute(stmt)
    author: Author | None = result.scalar_one_or_none()

    return author
