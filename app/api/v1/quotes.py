from fastapi import APIRouter, Depends
from starlette.status import HTTP_200_OK

from app.api.dependencies import get_repository, get_service
from app.database.repositories import RoutesRepository
from app.schemas.quote import QuoteRequest, QuotesResponse
from app.services.quotes import QuotesService
from app.utils import ERROR_RESPONSES, ServiceResult, handle_result

router = APIRouter()


@router.post(
    path="/",
    status_code=HTTP_200_OK,
    response_model=QuotesResponse,
    responses=ERROR_RESPONSES,
    name="quotes",
)
async def quotes(
    *,
    request_quote: QuoteRequest,
    quotes_service: QuotesService = Depends(get_service(QuotesService)),
    routes_repo: RoutesRepository = Depends(get_repository(RoutesRepository)),
) -> ServiceResult:
    """
    Calculate quotes
    """
    result = await quotes_service.calculate_quotes(request=request_quote, routes_repo=routes_repo)

    return await handle_result(result)
