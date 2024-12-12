from typing import Tuple

from dotenv import load_dotenv
import os

from sqlalchemy.orm import Session

from ..models import Negotiation, Property

load_dotenv()

MAX_PROPERTY_VALUE = int(os.getenv("MAX_PROPERTY_VALUE"))
MIN_CREDIT_SCORE = int(os.getenv("MIN_CREDIT_SCORE"))
MIN_PROPERTY_VALUE = int(os.getenv("MIN_PROPERTY_VALUE"))
PAYMENT_DURATION_MONTHS = int(os.getenv("PAYMENT_DURATION_MONTHS"))


def assess_negotiation_risk(
    prop: Property, credit_score: int, income: int
) -> Tuple[bool, str | None]:
    if prop.value < MIN_PROPERTY_VALUE:
        return False, "Property value too low"

    if prop.value > MAX_PROPERTY_VALUE:
        return False, "Property value too high"

    if credit_score < MIN_CREDIT_SCORE:
        return False, "Credit score too low"

    if income < prop.value / PAYMENT_DURATION_MONTHS:
        return False, "Income too low"

    return True, None


def property_store(
    session: Session, value: int, credit_score: int, income: int
) -> {"id": int}:
    prop = Property(value=value)
    [approved, reason] = assess_negotiation_risk(prop, credit_score, income)
    negotiation = Negotiation(
        approved=approved,
        credit_score=credit_score,
        income=income,
        property=prop,
        reason=reason,
    )

    session.add(prop)
    session.add(negotiation)
    session.commit()

    session.refresh(prop)
    return {"id": prop.id}
