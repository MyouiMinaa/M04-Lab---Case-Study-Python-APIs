from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import uvicorn
from database import SessionLocal, engine
import models
import crud
import book_schemas as schemas


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/books", response_model=schemas.BookDisplay)
def create_book(book: schemas.BookSchema, db: Session = Depends(get_db)):
    return crud.create_book(db=db, book=book)

@app.get("/books", response_model=list[schemas.BookDisplay])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_books(db=db, skip=skip, limit=limit)

@app.get("/books/{book_id}", response_model=schemas.BookDisplay)
def read_book(book_id: int, db: Session = Depends(get_db)):
    return crud.get_book(db=db, book_id=book_id)
@app.get("/")
def read_root():
    return {"Welcome to the Book API!"}

@app.put("/books/{book_id}", response_model=schemas.BookDisplay)
def update_book(book_id: int, book: schemas.BookSchema, db: Session = Depends(get_db)):
    return crud.update_book(db=db, book_id=book_id, book=book)

@app.delete("/books/{book_id}", response_model=schemas.BookDisplay)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    return crud.delete_book(db=db, book_id=book_id)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
