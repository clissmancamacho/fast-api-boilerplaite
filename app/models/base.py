from sqlalchemy.orm import declarative_base, declared_attr


class BaseModel:
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    __name__: str


BaseModel = declarative_base(cls=BaseModel)
