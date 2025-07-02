from pydantic import BaseModel

class ReviewBase(BaseModel):
    book_title: str
    reviewer_name: str
    content: str
    rating: float

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int

    class Config:
        from_attributes = True  # For Pydantic v2+