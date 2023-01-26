import pandas as pd
from pandas import DataFrame
from fastapi import HTTPException
from dto.request import (
    CalculateCustomerInformation,
    ReturnToClientCalculateCustomerInformation,
)
from utils.consts import *
from utils.ratesenum import HealthClassToNumber


def _Chek_Health_Class(weight: int, row):
    if row["Declined"].values[0] <= weight:
        return "Declined"
    elif row["Standard"].values[0] <= weight:
        return "Standard"
    elif row["Standard Plus"].values[0] <= weight:
        return "Standard Plus"
    elif row["Preferred"].values[0] <= weight:
        return "Preferred"
    elif row["Preferred Plus"].values[0] <= weight:
        return "Preferred Plus"
    raise HTTPException(status_code=400, detail="Under weight we cannt insure him")


def _Get_Rates_Df():
    df = pd.read_excel("./Rates-table.xlsx", "Full rates")
    df.columns.values[0] = "Term"
    df.columns.values[1] = "Age"
    return df


def _Chek_Rates(RowRates: DataFrame, HealthClass: str, coverage: int):
    if 999999 <= coverage:
        return _Match_Health_Class_To_Factor(RowRates, HealthClass, step999)
    elif 499999 <= coverage:
        return _Match_Health_Class_To_Factor(RowRates, HealthClass, step499)
    elif 250000 <= coverage:
        return _Match_Health_Class_To_Factor(RowRates, HealthClass, step250)
    raise HTTPException(status_code=400, detail="coverage amount isnt insurabele")


def _Match_Health_Class_To_Factor(RowRates: DataFrame, HealthClass: str, prefix: int):
    ColumIndex = (
        HealthClassToNumber[HealthClass.strip().replace(" ", "")].value + prefix
    )
    factor = RowRates.iloc[:, [ColumIndex]].values[0][0]
    return factor


def calculate_Customer_Information(
    calculateCustomerInformation: CalculateCustomerInformation,
):
    HealthClassDf = pd.read_excel("./healthClassCleand.xlsx")
    RowHealthClass = HealthClassDf.loc[
        (HealthClassDf["Height"] == calculateCustomerInformation.height)
    ]
    HealthClass = _Chek_Health_Class(
        calculateCustomerInformation.weight, RowHealthClass
    )
    RatesDf = _Get_Rates_Df()
    RowRates = RatesDf.loc[
        (RatesDf["Term"] == calculateCustomerInformation.term)
        & (RatesDf["Age"] == calculateCustomerInformation.age)
    ]
    factor = _Chek_Rates(RowRates, HealthClass, calculateCustomerInformation.coverage)
    price = calculateCustomerInformation.coverage / 1000 * factor
    return {
        "price": price,
        "health-class": HealthClass,
        "teram": calculateCustomerInformation.term,
        "coverage": calculateCustomerInformation.coverage,
    }
