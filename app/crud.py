from sqlalchemy.orm import Session
from app import models, schemas

def get_review(db: Session, review_id: int):
    return db.query(models.Review).filter(models.Review.id == review_id).first()

def create_review(db: Session, review: schemas.ReviewCreate):
    db_review = models.Review(**review.dict())
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def update_review(db: Session, review_id: int, review: schemas.ReviewCreate):
    db_review = db.query(models.Review).filter(models.Review.id == review_id).first()
    if db_review:
        db_review.book_title = review.book_title
        db_review.reviewer_name = review.reviewer_name
        db_review.content = review.content
        db_review.rating = review.rating
        db.commit()
        db.refresh(db_review)
    return db_review

def delete_review(db: Session, review_id: int):
    db_review = db.query(models.Review).filter(models.Review.id == review_id).first()
    if db_review:
        db.delete(db_review)
        db.commit()
    return db_review