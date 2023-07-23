from fastapi import APIRouter, Depends, UploadFile
from starlette.status import HTTP_200_OK

from app.api.dependencies import get_repository, get_service
from app.database.repositories import RatesRepository, RoutesRepository
from app.schemas.data import DataResponse
from app.services.rates import RatesService
from app.utils import ERROR_RESPONSES, ServiceResult, handle_result

router = APIRouter()


@router.post(
    path="/init",
    status_code=HTTP_200_OK,
    response_model=DataResponse,
    responses=ERROR_RESPONSES,
    name="data:init",
)
async def init(
    *,
    file: UploadFile,
    rates_service: RatesService = Depends(get_service(RatesService)),
    rates_repo: RatesRepository = Depends(get_repository(RatesRepository)),
    routes_repo: RoutesRepository = Depends(get_repository(RoutesRepository)),
) -> ServiceResult:
    """
    Add data to DB
    """
    result = await rates_service.init_rates(routes_repo=routes_repo, rates_repo=rates_repo, file=file.file)

    return await handle_result(result)


@router.get(
    path="/flush",
    status_code=HTTP_200_OK,
    response_model=DataResponse,
    responses=ERROR_RESPONSES,
    name="data:flush",
)
async def flush(
    *,
    rates_service: RatesService = Depends(get_service(RatesService)),
    rates_repo: RatesRepository = Depends(get_repository(RatesRepository)),
    routes_repo: RoutesRepository = Depends(get_repository(RoutesRepository)),
) -> ServiceResult:
    """
    Remove data from DB
    """
    result = await rates_service.flush_rates(routes_repo=routes_repo, rates_repo=rates_repo)

    return await handle_result(result)
