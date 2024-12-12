from sqlalchemy import select
from sqlalchemy.orm import Session

from ..models import Negotiation


def property_show(session: Session, property_id: int):
    statement = select(Negotiation).filter_by(property_id=property_id)
    negotiation = session.scalars(statement).one()
    return {
        "approved": negotiation.approved,
        "credit_score": negotiation.credit_score,
        "income": negotiation.income,
        "reason": negotiation.reason,
        "value": negotiation.property.value,
    }
