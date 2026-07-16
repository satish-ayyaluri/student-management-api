from pydantic import BaseModel, ConfigDict, Field

class StudentCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    age: int = Field(..., ge=16, le=100)
    course: str = Field(..., min_length=2)

class StudentResponse(StudentCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)