from typing import Any, Dict

from pydantic import BaseModel


class ErrorResponse(BaseModel):
    app_exception: str = "FailToSendAlert"
    context: Dict[str, Any] | None = {"reason": "Not Connected with notification channel"}
    model_config: Dict[str, Any] | None = {"from_attributes": True}


class ApiResponse(BaseModel):
    message: str = "default response message"
    data: BaseModel
    detail: Dict[str, Any] | None = {"key": "val"}
    model_config: Dict[str, Any] | None = {"from_attributes": True}
