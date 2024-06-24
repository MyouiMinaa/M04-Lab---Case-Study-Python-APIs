from pydantic import BaseModel

class BookSchema(BaseModel):
    book_name: str
    author: str
    publisher: str

class BookDisplay(BookSchema):
    id: int

    class Config:
        from_attributes = True