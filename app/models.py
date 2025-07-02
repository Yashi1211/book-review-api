from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    book_title = Column(String, index=True)
    reviewer_name = Column(String, index=True)
    content = Column(String)
    rating = Column(Float)