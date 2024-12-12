from typing import Union

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from ..db import engine
from ..services import property_show
from ..services import property_store

router = APIRouter(
    prefix="/imoveis", responses={500: {"description": "Internal server error"}}
)


class CreatePropertyData(BaseModel):
    credit_score: int = Field(description="The buyer's credit score")
    income: int = Field(description="The buyer's monthly income")
    value: int = Field(description="The value of the property")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "credit_score": 600,
                    "income": 2000,
                    "value": 200000,
                }
            ]
        }
    }


class CreatePropertyReturn(BaseModel):
    id: int = Field(description="The unique identifier of the created property")


@router.post("/", description="Create a new property negotiation entry.")
async def create_property(data: CreatePropertyData) -> CreatePropertyReturn:
    with Session(engine) as session:
        try:
            return property_store(session, data.value, data.credit_score, data.income)
        except Exception as e:
            session.rollback()
            raise HTTPException(
                status_code=500,
                detail="An unexpected error occurred. Please try again later.",
            )


class ShowPropertyReturn(BaseModel):
    approved: bool = Field(description="Whether the negotiation was approved")
    credit_score: int = Field(description="The buyer's credit score")
    income: int = Field(description="The buyer's monthly income")
    reason: Union[str, None] = Field(description="The reason for disapproval, if any")
    value: int = Field(description="The property's value")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "approved": False,
                    "credit_score": 600,
                    "income": 200,
                    "reason": "Income too low",
                    "value": 200000,
                },
                {
                    "approved": True,
                    "credit_score": 600,
                    "income": 2000,
                    "reason": None,
                    "value": 200000,
                },
            ]
        }
    }


@router.get(
    "/{property_id}",
    description="Retrieve the details and risk assessment of a property negotiation.",
)
async def show_property(property_id: int) -> ShowPropertyReturn:
    with Session(engine) as session:
        try:
            return property_show(session, property_id)
        except NoResultFound:
            raise HTTPException(status_code=404, detail="Negotiation not found")
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail="An unexpected error occurred. Please try again later.",
            )
