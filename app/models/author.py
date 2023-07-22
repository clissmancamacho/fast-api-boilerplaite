from sqlalchemy import Column, Integer, String, text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel
from app.models.common import DateTimeModelMixin


class Author(BaseModel, DateTimeModelMixin):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255))
    age = Column(Integer)
    books = relationship('Book', back_populates='author')
