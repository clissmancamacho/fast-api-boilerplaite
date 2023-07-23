from pydantic import BaseModel


class DataResponse(BaseModel):
    message: str
