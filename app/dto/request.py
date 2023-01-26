from pydantic import BaseModel


class CalculateCustomerInformation(BaseModel):
    #   The policy duration
    term: int
    #    The policy death benefit.
    coverage: int
    age: int
    height: str
    weight: int


class ReturnToClientCalculateCustomerInformation:
    def __init__(self, term, coverage, healthclass, price) -> None:
        self.term = term
        self.coverage = coverage
        self.healthclass = healthclass
        self.price = price
