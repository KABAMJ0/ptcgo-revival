"""Trainer Challenge progress: availability, match results, payouts and reset.

One row per (account, opponent) holds the win/loss tally and whether the
first-win payout was paid; a second row per (account, league) records that the
league-completion bonus was paid. Payouts land through
`grant_reward_in_session`, the same grant code redemption and the shop use, so
the wallet and collection stay consistent with everything else.
"""

import logging

from ptcgo.database import db_session, TrainerChallengeProgress, LEAGUE_ROW
from ptcgo.database.economy_data import grant_reward_in_session
from ptcgo.game.content import trainer_challenge as content


def _rows(session, account_id):
    """{(league_key, opponent_key): row} for every progress row of the account."""
    rows = session.query(TrainerChallengeProgress).filter_by(account_id=account_id).all()
    return {(row.league_key, row.opponent_key): row for row in rows}


def _wins_of(rows, league_key, opponent_key):
    """Wins already recorded for one opponent in the session's loaded rows."""
    return int(getattr(rows.get((league_key, opponent_key)), "wins", 0) or 0)


def _beaten(progress, opponent_key):
    row = progress.get(opponent_key) or {}
    return int(row.get("wins") or 0) > 0


def load(account_id):
    """{opponent_key: {"wins", "losses"}} — the league-completion rows excluded."""
    with db_session() as session:
        return {
            row.opponent_key: {"wins": int(row.wins or 0),
                               "losses": int(row.losses or 0),
                               "rewarded": bool(row.rewarded)}
            for row in session.query(TrainerChallengeProgress)
            .filter_by(account_id=account_id).all()
            if row.opponent_key != LEAGUE_ROW
        }


def available(opponent_key, progress):
    """Whether this opponent can be played: every earlier league and opponent is beaten."""
    found = content.find(opponent_key)
    if found is None:
        return False
    league, _, position = found
    for earlier in content.leagues():
        if earlier is league:
            break
        if not all(_beaten(progress, other.key) for other in earlier.opponents):
            return False
    return all(_beaten(progress, other.key) for other in league.opponents[:position])


def status_rows(account_id):
    """The panel's opponent list: every opponent with its availability.

    `status` is one of the client's three OpponentStatus names.
    """
    progress = load(account_id)
    rows = []
    for league in content.leagues():
        for opponent in league.opponents:
            if _beaten(progress, opponent.key):
                state = "Completed"
            elif available(opponent.key, progress):
                state = "Available"
            else:
                state = "Unavailable"
            rows.append({"key": opponent.key, "name": opponent.name,
                         "image": opponent.image, "status": state})
    return rows


def losses(account_id):
    """Total losses across the challenge, the panel's `losses` figure."""
    return sum(row["losses"] for row in load(account_id).values())


def record_result(account_id, opponent_key, won):
    """Records one finished match and pays whatever it earned.

    Returns {"ok", "granted": {"coins", "products"}, "unlocked": [keys],
    "league_completed": key|None}; `ok` is False for an unknown opponent, so a
    match against something that is not a league opponent records nothing.
    """
    found = content.find(opponent_key)
    if found is None:
        logging.warning(f"[TrainerChallenge] Unknown opponent '{opponent_key}' for {account_id}")
        return {"ok": False}
    league, opponent, _ = found
    granted = {"coins": 0, "products": {}}
    completed = None
    with db_session() as session:
        rows = _rows(session, account_id)
        row = rows.get((league.key, opponent_key))
        if row is None:
            row = TrainerChallengeProgress(account_id=account_id,
                                           league_key=league.key,
                                           opponent_key=opponent_key,
                                           wins=0, losses=0, rewarded=False)
            session.add(row)
        if won:
            row.wins += 1
        else:
            row.losses += 1
        if won and not row.rewarded:
            row.rewarded = True
            granted["coins"] += opponent.coins

        league_row = rows.get((league.key, LEAGUE_ROW))
        if league_row is None:
            league_row = TrainerChallengeProgress(account_id=account_id,
                                                  league_key=league.key,
                                                  opponent_key=LEAGUE_ROW,
                                                  wins=0, losses=0, rewarded=False)
            session.add(league_row)
        cleared = won and all(
            other.key == opponent_key or _wins_of(rows, league.key, other.key) > 0
            for other in league.opponents
        )
        if cleared and not league_row.rewarded:
            league_row.rewarded = True
            granted["coins"] += league.coins
            pack = _league_pack(league)
            if pack:
                granted["products"][pack] = league.packs
            completed = league.key

        if granted["coins"] or granted["products"]:
            grant_reward_in_session(session, account_id, dict(granted))
        session.flush()

    progress = load(account_id)
    unlocked = [other.key for entry in content.leagues() for other in entry.opponents
                if available(other.key, progress) and not _beaten(progress, other.key)]
    logging.info(f"[TrainerChallenge] {account_id} {'beat' if won else 'lost to'} "
                 f"{opponent.name} ({league.name}); granted {granted}")
    return {"ok": True, "granted": granted, "unlocked": unlocked,
            "league_completed": completed}


def reset(account_id, league_key=None):
    """Clears challenge progress for one league, or every league when key is None."""
    with db_session() as session:
        query = session.query(TrainerChallengeProgress).filter_by(account_id=account_id)
        if league_key is not None:
            query = query.filter_by(league_key=league_key)
        removed = query.delete(synchronize_session=False)
    logging.info(f"[TrainerChallenge] Reset {removed} progress row(s) for {account_id} "
                 f"(league={league_key or 'all'})")
    return removed


def _league_pack(league):
    """The booster pack a cleared league pays: one eligible product, chosen by league order."""
    from ptcgo.game.content.starter import starter_booster_packs
    packs = sorted(starter_booster_packs(), key=lambda product: product.key)
    if not packs:
        return None
    position = [entry.key for entry in content.leagues()].index(league.key)
    return packs[position % len(packs)].guid
