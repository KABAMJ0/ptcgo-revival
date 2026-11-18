"""Trainer Challenge progress: one row per (account, opponent) plus league payouts."""

from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from ptcgo.database.base import Base

# `opponent_key` on the row that records a league's completion bonus.
LEAGUE_ROW = ""


class TrainerChallengeProgress(Base):
    __tablename__ = 'trainer_challenge_progress'
    __table_args__ = (UniqueConstraint('account_id', 'league_key', 'opponent_key',
                                       name='uq_tc_progress_account_opponent'),)

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    account_id: Mapped[str] = mapped_column(index=True, nullable=False)
    league_key: Mapped[str] = mapped_column(default="")
    # "" marks the league-completion row (see LEAGUE_ROW)
    opponent_key: Mapped[str] = mapped_column(default="")
    wins: Mapped[int] = mapped_column(default=0)
    losses: Mapped[int] = mapped_column(default=0)
    # the first-win (or league-completion) payout is paid exactly once
    rewarded: Mapped[bool] = mapped_column(default=False)
