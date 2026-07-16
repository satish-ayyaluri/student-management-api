from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models
import schemas
import crud
from fastapi import FastAPI, Depends, HTTPException

from database import engine, SessionLocal

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Management API",
    description="A REST API built with FastAPI for managing student records.",
    version="1.0.0"
)
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "Student Management API"
    }

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "FastAPI is working!"}


@app.post("/students", response_model=schemas.StudentResponse)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

@app.get(
    "/students",
    response_model=list[schemas.StudentResponse],
    summary="Get all students",
    description="Returns a list of all students."
)

@app.get("/students/{student_id}", response_model=schemas.StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = crud.get_student(db, student_id)

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return student

@app.put("/students/{student_id}", response_model=schemas.StudentResponse)
def update_student(
    student_id: int,
    student: schemas.StudentCreate,
    db: Session = Depends(get_db)
):
    updated_student = crud.update_student(db, student_id, student)

    if updated_student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return updated_student

@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    deleted_student = crud.delete_student(db, student_id)

    if deleted_student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return {"message": "Student deleted successfully"}