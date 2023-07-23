import json
import logging

from fastapi import Depends, File
from starlette.status import HTTP_200_OK

from app.api.dependencies import get_repository
from app.core import constant
from app.database.repositories import RatesRepository, RoutesRepository
from app.services.base import BaseService
from app.utils import ServiceResult, response_5xx, return_service

logger = logging.getLogger(__name__)


class RatesService(BaseService):
    @return_service
    async def init_rates(
        self, routes_repo: RoutesRepository = Depends(get_repository(RoutesRepository)), rates_repo: RatesRepository = Depends(get_repository(RatesRepository)), file: File = None
    ) -> ServiceResult:
        try:
            file = file.read()
            data = json.loads(file.decode("utf-8"))
            for route in data:
                route_json = {}
                route_json["starting_country"] = route["starting_country"]
                route_json["destination_country"] = route["destination_country"]
                route_json["shipping_channel"] = route["shipping_channel"]
                route_json["min_shipping_range"] = route["shipping_time_range"]["min_days"]
                route_json["max_shipping_range"] = route["shipping_time_range"]["max_days"]

                new_route = await routes_repo.create_route(route_in=route_json)

                for rate in route["rates"]:
                    new_rate = {}
                    new_rate["min_weight_kg"] = rate["min_weight_kg"]
                    new_rate["max_weight_kg"] = rate["max_weight_kg"]
                    new_rate["per_kg_rate"] = rate["per_kg_rate"]
                    new_rate["route_id"] = new_route.id
                    new_rate = await rates_repo.create_rate(rate_in=new_rate)

            return dict(
                status_code=HTTP_200_OK,
                content={
                    "message": constant.SUCCESS_DATA_CREATED,
                },
            )

        except Exception as e:
            await rates_repo.delete_all()
            await routes_repo.delete_all()
            logger.error(e)
            return response_5xx()

    @return_service
    async def flush_rates(self, routes_repo: RoutesRepository = Depends(get_repository(RoutesRepository)), rates_repo: RatesRepository = Depends(get_repository(RatesRepository))) -> ServiceResult:
        await rates_repo.delete_all()
        await routes_repo.delete_all()
        return dict(
            status_code=HTTP_200_OK,
            content={
                "message": constant.SUCCESS_DATA_FLUSH,
            },
        )
