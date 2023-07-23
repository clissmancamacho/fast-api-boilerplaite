import logging

from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from starlette.status import HTTP_200_OK

from app.api.dependencies import get_repository
from app.database.repositories import RoutesRepository
from app.schemas.quote import QuoteRequest
from app.services.base import BaseService
from app.utils import (
    ServiceResult,
    calculate_final_quotes,
    calculate_gross_weight,
    calculate_service_fee,
    calculate_volumetric_weight,
    oversized_boxes_fee,
    overweighed_boxes_fee,
    response_5xx,
    return_service,
)

logger = logging.getLogger(__name__)


class QuotesService(BaseService):
    @return_service
    async def calculate_quotes(self, request: QuoteRequest, routes_repo: RoutesRepository = Depends(get_repository(RoutesRepository))) -> ServiceResult:
        try:
            routes = await routes_repo.get_routes_by_origin_and_destination(origin=request.starting_country, destination=request.destination_country)
            gross_weight = calculate_gross_weight(request.boxes)
            volumetric_weight = calculate_volumetric_weight(request.boxes)
            chargeable_weight = max(gross_weight, volumetric_weight)
            logger.debug(gross_weight)
            logger.debug(volumetric_weight)
            overweight_fee = overweighed_boxes_fee(request.starting_country, request.boxes)
            oversized_fee = oversized_boxes_fee(request.starting_country, request.boxes)
            service_fee = calculate_service_fee(request.starting_country)

            quotes = calculate_final_quotes(routes, chargeable_weight, overweight_fee, oversized_fee, service_fee)

            return dict(
                status_code=HTTP_200_OK,
                content={"quotes": jsonable_encoder(quotes)},
            )

        except Exception as e:
            logger.error(e)
            return response_5xx()
