from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship

from .base import Base


class Property(Base):
    __tablename__ = "properties"
    value: Mapped[int]
    negotiation: Mapped["Negotiation"] = relationship(back_populates="property")
