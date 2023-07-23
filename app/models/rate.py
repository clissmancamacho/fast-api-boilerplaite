from sqlalchemy import Column, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.models.base import Base
from app.models.common import DateTimeModelMixin


class Rate(Base, DateTimeModelMixin):
    __tablename__ = "rates"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    min_weight_kg = Column(Float, nullable=False)
    max_weight_kg = Column(Float, nullable=False)
    per_kg_rate = Column(Float, nullable=False)
    route_id = Column(Integer, ForeignKey("routes.id"))

    route = relationship("Route", back_populates="rates")

    def __init__(self, **kwargs):
        super(Rate, self).__init__(**kwargs)
