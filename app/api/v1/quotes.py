from fastapi import APIRouter, Depends
from starlette.status import HTTP_200_OK

from app.utils import ERROR_RESPONSES, ServiceResult, handle_result

router = APIRouter()


# @router.post(
#     path="/",
#     status_code=HTTP_200_OK,
#     response_model=UserResponse,
#     responses=ERROR_RESPONSES,
#     name="quotes",
# )
# async def quotes(
#     *,
#     users_service: UsersService = Depends(get_service(UsersService)),
#     users_repo: UsersRepository = Depends(get_repository(UsersRepository)),
#     user_in: UserInSignIn,
#     settings: AppSettings = Depends(get_app_settings),
# ) -> ServiceResult:
#     """
#     Create new users.
#     """
#     secret_key = str(settings.secret_key.get_secret_value())
#     result = await users_service.signin_user(users_repo=users_repo, user_in=user_in, secret_key=secret_key)

#     return await handle_result(result)
