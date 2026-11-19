"""Tutorial funnel progress: one row per (account, tutorial match) plus the funnel's end.

The account-level row (`match_key == COMPLETE_ROW`) records that the player has
left the tutorial, whether by finishing it or by being skipped: the funnel is a
one-way door, and a returning player must never be dropped back into it.
"""

from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from ptcgo.database.base import Base


class TutorialProgress(Base):
    __tablename__ = 'tutorial_progress'
    __table_args__ = (UniqueConstraint('account_id', 'match_key',
                                       name='uq_tutorial_progress_account_match'),)

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    account_id: Mapped[str] = mapped_column(index=True, nullable=False)
    # a tutorial match key, or COMPLETE_ROW for the account-level row
    match_key: Mapped[str] = mapped_column(default="")
    wins: Mapped[int] = mapped_column(default=0)
    losses: Mapped[int] = mapped_column(default=0)
    # the first-win payout is paid exactly once per match
    rewarded: Mapped[bool] = mapped_column(default=False)
    # set on the account-level row: the player has finished or skipped the funnel
    completed: Mapped[bool] = mapped_column(default=False)
