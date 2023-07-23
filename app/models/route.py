from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.models.base import Base
from app.models.common import DateTimeModelMixin


class Route(Base, DateTimeModelMixin):
    __tablename__ = "routes"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    starting_country = Column(String(32), nullable=False)
    destination_country = Column(String(32), nullable=False)
    shipping_channel = Column(String(10), nullable=False)
    min_shipping_range = Column(Integer, nullable=False)
    max_shipping_range = Column(Integer, nullable=False)

    rates = relationship("Rate", back_populates="route")

    def __init__(self, **kwargs):
        super(Route, self).__init__(**kwargs)
