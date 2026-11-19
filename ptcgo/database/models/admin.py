"""Operator state the admin console owns: card behaviour overrides, card bans, and
the persisted audit trail of every admin mutation.

These live in the game database rather than in json_data/ because a deploy copies
the tracked tree over the live checkout: a JSON file there would be reset to its
committed contents on every deploy, silently undoing an operator's ban or override.
"""
import datetime

from sqlalchemy import func, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from ptcgo.database.base import Base
from ptcgo.database.models.inventory import JSONEncodedDict


class CardOverride(Base):
    """One attack's admin-set behaviour, applied by the card loader at boot.

    `spec_json` holds only what ptcgo.game.content.card_overrides can express:
    {"damage": int, "damage_operator": str, "cost": {TypeName: n},
     "effect": null | {"module": str, "factory": str, "kwargs": {...}}}.
    """
    __tablename__ = 'card_overrides'
    __table_args__ = (UniqueConstraint('archetype_id', 'title', name='uq_card_override_attack'),)

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    archetype_id: Mapped[str] = mapped_column(index=True, nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
    spec_json: Mapped[dict] = mapped_column(JSONEncodedDict, nullable=False)
    enabled: Mapped[bool] = mapped_column(default=True)
    note: Mapped[str] = mapped_column(default="")
    updated_by: Mapped[str] = mapped_column(default="")
    updated_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now(), onupdate=func.now())


class CardBan(Base):
    """A card refused server-wide: by deck validation in every format and at matchmaking."""
    __tablename__ = 'card_bans'

    archetype_id: Mapped[str] = mapped_column(primary_key=True)
    reason: Mapped[str] = mapped_column(default="")
    banned_by: Mapped[str] = mapped_column(default="")
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())


class AdminAudit(Base):
    """Every admin mutation, with the acting admin and a before/after diff."""
    __tablename__ = 'admin_audit'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    at: Mapped[datetime.datetime] = mapped_column(server_default=func.now(), index=True)
    admin: Mapped[str] = mapped_column(default="")
    action: Mapped[str] = mapped_column(index=True, default="")
    target: Mapped[str] = mapped_column(index=True, default="")
    diff_json: Mapped[dict] = mapped_column(JSONEncodedDict, default=dict)
