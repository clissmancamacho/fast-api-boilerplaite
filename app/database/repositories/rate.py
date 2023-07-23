from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncConnection

from app.database.repositories.base import BaseRepository
from app.models import RateModel


class RatesRepository(BaseRepository):
    def __init__(self, conn: AsyncConnection) -> None:
        super().__init__(conn)

    #
    async def get_rate_by_id(self, *, rate_id: int) -> RateModel:
        query = select(RateModel).where(RateModel.id == rate_id).limit(1)

        raw_result = await self.connection.execute(query)
        result = raw_result.fetchone()
        return result.RateModel if result is not None else result

    #

    async def create_rate(self, *, rate_in) -> RateModel:
        created_rate = RateModel(**rate_in)
        self.connection.add(created_rate)
        await self.connection.commit()
        await self.connection.refresh(created_rate)
        return created_rate

    async def delete_all(self) -> None:
        await super().delete_all(model=RateModel)
