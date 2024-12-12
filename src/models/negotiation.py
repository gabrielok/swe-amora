from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .base import Base


class Negotiation(Base):
    __tablename__ = "negotiations"
    approved: Mapped[bool]
    property: Mapped["Property"] = relationship(back_populates="negotiation")
    property_id: Mapped[int] = mapped_column(ForeignKey("properties.id"), index=True)
