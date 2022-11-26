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
)
from models import Author
from models.db import get_session

router = APIRouter(
    prefix='/authors',
    tags=['Authors'],
)


@router.get('', response_model=list[AuthorOut])
async def get_all_authors(session: AsyncSession = Depends(get_session)) -> list[AuthorOut]:
    authors: list[Author] = await crud.get_all_authors(session)
    return [
        AuthorOut(
            name=author.name,
            about=author.about,
            id=author.id,
        )
        for author in authors
    ]


@router.get('/{author_id}', response_model=AuthorOut)
async def get_author_by_id(author_id: int, session: AsyncSession = Depends(get_session)) -> AuthorOut:
    author: Author = await crud.get_author_by_id(session, author_id)
    if author:
        return AuthorOut(
            name=author.name,
            about=author.about,
            id=author.id,
        )

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Author id={author_id} does not exist.',
    )


@router.post('', response_model=AuthorOut, status_code=status.HTTP_201_CREATED)
async def add_author(author_in: AuthorIn, session: AsyncSession = Depends(get_session)) -> AuthorOut:
    author: Author = await crud.create_author(session, author_in)
    return AuthorOut(
        name=author.name,
        about=author.about,
        id=author.id,
    )
