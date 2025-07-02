from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE
@router.post("/reviews/", response_model=schemas.Review)
def create_review(review: schemas.ReviewCreate, db: Session = Depends(get_db)):
    return crud.create_review(db, review)

# READ ALL
@router.get("/reviews/", response_model=list[schemas.Review])
def read_reviews(db: Session = Depends(get_db)):
    return db.query(crud.models.Review).all()

# READ BY ID
@router.get("/reviews/{review_id}", response_model=schemas.Review)
def read_review(review_id: int, db: Session = Depends(get_db)):
    review = crud.get_review(db, review_id)
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    return review

# UPDATE
@router.put("/reviews/{review_id}", response_model=schemas.Review)
def update_review(
    review_id: int,
    updated_data: schemas.ReviewCreate,
    db: Session = Depends(get_db)
):
    existing_review = crud.get_review(db, review_id)
    if not existing_review:
        raise HTTPException(status_code=404, detail=f"Review with id={review_id} not found")
    return crud.update_review(db, review_id, updated_data)

# DELETE
@router.delete("/reviews/{review_id}", response_model=schemas.Review)
def delete_review(review_id: int, db: Session = Depends(get_db)):
    review = crud.delete_review(db, review_id)
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    return review