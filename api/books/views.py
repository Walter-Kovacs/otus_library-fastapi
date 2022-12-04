from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.ext.asyncio import AsyncSession

from api.books import crud
from api.schemas.book import (
    BookIn,
    BookOut,
    BookUpdate,
)
from models import Author, Book
from models.db import get_session


router = APIRouter(
    prefix='/books',
    tags=['Books']
)


@router.get('', response_model=list[BookOut])
async def get_books(
    author_id: int = None,
    order_by: str = "",
    session: AsyncSession = Depends(get_session),
) -> list[Book]:

    if author_id is not None:
        return await crud.get_books_by_author_id(session, author_id, order_by)
    return await crud.get_all_books(session, order_by)


@router.post('', response_model=BookOut, status_code=status.HTTP_201_CREATED)
async def create_book(book_in: BookIn, session: AsyncSession = Depends(get_session)) -> Book:
    return await crud.create_book(session, book_in)


@router.get('/{book_id}')
async def get_book_by_id(book_id: int, session: AsyncSession = Depends(get_session)) -> Book:
    book: Book = await crud.get_book_by_id(session, book_id)
    if book:
        return book

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book id={book_id} does not exist.",
    )
