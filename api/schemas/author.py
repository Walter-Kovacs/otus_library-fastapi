from pydantic import (
    BaseModel,
    Field,
    constr,
)


class BaseAuthor(BaseModel):
    name: constr(min_length=1, max_length=100) = Field(..., example="Jack London")
    about: str = Field(None)


class AuthorOut(BaseAuthor):
    id: int

    class Config:
        orm_mode = True


class AuthorIn(BaseAuthor):
    pass


class AuthorUpdate(BaseModel):
    name: constr(min_length=1, max_length=100) = Field(None, example="Jack London")
    about: str = Field(None)
