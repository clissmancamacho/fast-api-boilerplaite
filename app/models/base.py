from sqlalchemy.orm import declarative_base, declared_attr


class Base:
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    __name__: str


Base = declarative_base(cls=Base)
