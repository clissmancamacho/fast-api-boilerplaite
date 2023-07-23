from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncConnection
from sqlalchemy.orm import joinedload

from app.database.repositories.base import BaseRepository
from app.models import RouteModel


class RoutesRepository(BaseRepository):
    def __init__(self, conn: AsyncConnection) -> None:
        super().__init__(conn)

    #

    async def create_route(self, *, route_in) -> RouteModel:
        created_route = RouteModel(**route_in)
        self.connection.add(created_route)
        await self.connection.commit()
        await self.connection.refresh(created_route)
        return created_route

    async def get_routes_by_origin_and_destination(self, *, origin: str, destination: str) -> RouteModel:
        query = select(RouteModel).where(RouteModel.starting_country == origin, RouteModel.destination_country == destination).options(joinedload(RouteModel.rates))
        raw_results = await self.connection.execute(query)
        results = raw_results.unique().scalars().all()
        return results

    async def delete_all(self) -> None:
        await super().delete_all(model=RouteModel)
