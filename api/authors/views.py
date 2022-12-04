from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.ext.asyncio import AsyncSession

from api.authors import crud
from api.schemas.author import (
    AuthorIn,
    AuthorOut,
    AuthorUpdate,
)
from models import Author
from models.db import get_session

router = APIRouter(
    prefix='/authors',
    tags=['Authors'],
)


@router.get('', response_model=list[AuthorOut])
async def get_all_authors(order_by: str = "", session: AsyncSession = Depends(get_session)) -> list[Author]:
    if order_by == "name":
        return await crud.get_all_authors_order_by_name(session)
    return await crud.get_all_authors(session)


@router.get('/{author_id}', response_model=AuthorOut)
async def get_author_by_id(author_id: int, session: AsyncSession = Depends(get_session)) -> Author:
    author: Author = await crud.get_author_by_id(session, author_id)
    if author:
        return author

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Author id={author_id} does not exist.",
    )


@router.post('', response_model=AuthorOut, status_code=status.HTTP_201_CREATED)
async def add_author(author_in: AuthorIn, session: AsyncSession = Depends(get_session)) -> Author:
    return await crud.create_author(session, author_in)


@router.patch('/{author_id}', response_model=AuthorOut)
async def update_author(
    author_id: int,
    author_update: AuthorUpdate,
    session: AsyncSession = Depends(get_session)
) -> Author:

    author: Author = await crud.update_author(session, author_id, author_update)
    if author:
        return author

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Author id={author_id} does not exist.",
    )


@router.delete('/{author_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_author(author_id: int, session: AsyncSession = Depends(get_session)):
    await crud.delete_author(session, author_id)
