from pydantic import (
    BaseModel,
    Field,
    constr,
)

title_constraint = constr(min_length=1, max_length=200)


class BookBase(BaseModel):
    title: title_constraint = Field(..., example="The Call of the Wild")
    author_id: int = Field(...)
    abstract: str
    count: int


class BookIn(BookBase):
    pass


class BookOut(BookBase):
    id: int

    class Config:
        orm_mode = True


class BookUpdate(BookBase):
    title: title_constraint = Field(None)
    author_id: int = Field(None)
