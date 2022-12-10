from pydantic import BaseModel


class GetAvregeBodyRequest(BaseModel):
    type: str
    froma: str
    to: str


class ReturnToClient():
    def __init__(self,type,value,processed) -> None:
        self.type =type
        self.value=value
        self.processed=processed
