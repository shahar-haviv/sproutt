from service import calculate_Customer_Information
from dto.request import CalculateCustomerInformation

from fastapi import FastAPI , Query

app = FastAPI()

@app.post("/calculatecustomerinformation")
def read_item(calculateCustomerInformation: CalculateCustomerInformation):
    return calculate_Customer_Information(calculateCustomerInformation)
