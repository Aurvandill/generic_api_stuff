from pydantic import BaseModel
from http import HTTPStatus

class Response(BaseModel):
    resp_code: HTTPStatus
    resp_data: dict