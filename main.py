from fastapi import FastAPI, HTTPException, Depends
from typing import List, Annotated
import models
import schemas
import crud
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

# Create database tables
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/questions/{question_id}", response_model=schemas.Question)
async def read_question(question_id: int, db: db_dependency):
    db_question = crud.get_question(db, question_id=question_id)
    if db_question is None:
        raise HTTPException(status_code=404, detail='Question not found')
    return db_question

@app.get("/choices/{question_id}", response_model=List[schemas.Choice])
async def read_choices(question_id: int, db: db_dependency):
    db_choices = crud.get_choices_by_question(db, question_id=question_id)
    if not db_choices:
        raise HTTPException(status_code=404, detail='Choices not found')
    return db_choices

@app.post("/questions/", response_model=schemas.Question, status_code=201)
async def create_questions(question: schemas.QuestionBase, db: db_dependency):
    return crud.create_question(db=db, question=question)