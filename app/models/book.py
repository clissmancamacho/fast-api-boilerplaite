from sqlalchemy import Column, Integer, String, ForeignKey, text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel
from app.models.common import DateTimeModelMixin


class Book(BaseModel, DateTimeModelMixin):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255))
    rating = Column(Integer)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship('Author', back_populates='books')
