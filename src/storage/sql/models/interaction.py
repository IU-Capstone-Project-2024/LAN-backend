from sqlalchemy import BigInteger, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.storage.sql.models import Base
from src.storage.sql.__mixin__ import IdMixin

"""
    Model for interactions between profiles, 'like', 'dislike' or 'favourite'
"""


class Interaction(Base, IdMixin):
    __tablename__ = "interactions"

    profile_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("profiles.id"))
    target_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("profiles.id"))
    interaction_type: Mapped[str] = mapped_column(String(10))

    profile = relationship("Profile", foreign_keys=[profile_id])
    target = relationship("Profile", foreign_keys=[target_id])