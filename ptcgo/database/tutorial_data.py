"""Tutorial funnel progress: which scripted matches are beaten, and what that pays.

A fresh account enters the funnel and leaves it once both scripted matches are
won or the funnel is skipped. Everything a returning player sees afterwards is
`completed(account_id) == True`, which is also what keeps the scene from pulling
them back in.

A win marks the match's payout *pending* instead of paying it, because the scene
owns that handshake: `PvEInterstitialsController` reports pending rewards,
`TutorialRewardsClaimer` answers by sending `TutorialClaimRewards`, and the claim
pays through `grant_reward_in_session` — the same grant code redemption and the
shop use, so the wallet and collection stay consistent with everything else.
"""

import logging

from ptcgo.database import db_session, TutorialProgress
from ptcgo.database.economy_data import grant_reward_in_session
from ptcgo.game.content import tutorial as content

_MATCH_KEYS = tuple(entry.key for entry in content.matches())


def _rows(session, account_id):
    """{match_key: row}, including the account-level row under COMPLETE_ROW."""
    return {row.match_key: row
            for row in session.query(TutorialProgress).filter_by(account_id=account_id).all()}


def _ensure_row(session, account_id, match_key):
    row = session.query(TutorialProgress).filter_by(
        account_id=account_id, match_key=match_key).first()
    if row is None:
        row = TutorialProgress(account_id=account_id, match_key=match_key,
                               wins=0, losses=0, rewarded=False, completed=False)
        session.add(row)
    return row


def load(account_id):
    """{match_key: {"wins", "losses", "rewarded"}} for the scripted matches."""
    with db_session() as session:
        return {row.match_key: {"wins": int(row.wins or 0),
                                "losses": int(row.losses or 0),
                                "rewarded": bool(row.rewarded)}
                for row in session.query(TutorialProgress).filter_by(account_id=account_id).all()
                if row.match_key in _MATCH_KEYS}


def completed(account_id):
    """Whether this account has finished or been skipped out of the funnel."""
    with db_session() as session:
        row = session.query(TutorialProgress).filter_by(
            account_id=account_id, match_key=content.COMPLETE_ROW).first()
        return bool(row is not None and row.completed)


def rewards_pending(account_id):
    """Whether a won match still has its payout to collect.

    The scene sends `TutorialClaimRewards` the moment this is true, so it is what
    makes the reward handshake happen at all, and it is the `waitingForRewards`
    flag in the status payload.
    """
    return any(row["wins"] and not row["rewarded"] for row in load(account_id).values())


def status_rows(account_id):
    """The tutorial panel's opponents, the matches still to win.

    Empty once the funnel is over and nothing is left to collect, which is the
    "no more tutorial matches" state the ending panels render.
    """
    if completed(account_id) and not rewards_pending(account_id):
        return []
    return content.status_rows(load(account_id))


def losses(account_id):
    """Total tutorial losses, the panel's `losses` figure."""
    return sum(row["losses"] for row in load(account_id).values())


def next_match(account_id):
    """The match the funnel is on: the first one not yet beaten, or None."""
    if completed(account_id):
        return None
    progress = load(account_id)
    for entry in content.matches():
        if int((progress.get(entry.key) or {}).get("wins") or 0) == 0:
            return entry
    return None


def record_result(account_id, match_key, won):
    """Records one finished tutorial match and leaves its payout pending.

    Returns {"ok", "granted": {"coins", "products"}, "completed": bool}; `ok` is
    False for a match key the funnel does not have, so a stray result records
    nothing. The last win closes the funnel.
    """
    entry = content.find(match_key)
    if entry is None:
        logging.warning(f"[Tutorial] Unknown match '{match_key}' for {account_id}")
        return {"ok": False}
    granted = {"coins": 0, "products": {}}
    with db_session() as session:
        row = _ensure_row(session, account_id, entry.key)
        if won:
            row.wins = int(row.wins or 0) + 1
            if not row.rewarded:
                granted["coins"] += entry.coins
                if entry.packs:
                    pack = _tutorial_pack()
                    if pack:
                        granted["products"][pack] = entry.packs
        else:
            row.losses = int(row.losses or 0) + 1
        session.flush()
        finished = _close_if_finished(session, account_id)
    logging.info(f"[Tutorial] {account_id} {'won' if won else 'lost'} {entry.name} "
                 f"({entry.key}); funnel complete: {finished}; pending {granted}")
    return {"ok": True, "granted": granted, "completed": finished}


def claim(account_id):
    """Pays every pending first-win payout; the answer to `TutorialClaimRewards`."""
    granted = {"coins": 0, "products": {}}
    with db_session() as session:
        rows = _rows(session, account_id)
        for entry in content.matches():
            row = rows.get(entry.key)
            if row is None or not row.wins or row.rewarded:
                continue
            row.rewarded = True
            granted["coins"] += entry.coins
            if entry.packs:
                pack = _tutorial_pack()
                if pack:
                    granted["products"][pack] = granted["products"].get(pack, 0) + entry.packs
        if granted["coins"] or granted["products"]:
            grant_reward_in_session(session, account_id, dict(granted))
    logging.info(f"[Tutorial] {account_id} claimed {granted}")
    return {"ok": True, "granted": granted,
            "claimed": bool(granted["coins"] or granted["products"])}


def mark_completed(account_id, reason="skipped"):
    """Ends the funnel for this account without playing it (a returning player)."""
    with db_session() as session:
        row = _ensure_row(session, account_id, content.COMPLETE_ROW)
        row.completed = True
    logging.info(f"[Tutorial] {account_id} leaves the funnel ({reason})")


def reset(account_id):
    """Clears tutorial progress so the funnel plays again (tests and admin)."""
    with db_session() as session:
        removed = session.query(TutorialProgress).filter_by(
            account_id=account_id).delete(synchronize_session=False)
    return removed


# Marker row for the one-time backfill: accounts that existed before the funnel
# was scripted are already past it. An empty account id cannot collide with a real
# one, and the marker is what makes the pass idempotent across restarts instead of
# sealing every account that is halfway through the funnel.
BACKFILL_MARKER = "backfill"


def backfill_completed():
    """Marks every account that predates the tutorial as having left the funnel.

    Accounts created before the scripted flow existed are returning players:
    dropping them into the intro would strand them behind a scene their progress
    no longer matches. Runs once; accounts created afterwards only get a row when
    they actually finish or are explicitly skipped.
    """
    from ptcgo.database import Account
    with db_session() as session:
        done = session.query(TutorialProgress).filter_by(
            account_id="", match_key=BACKFILL_MARKER).first()
        if done is not None:
            return 0
        existing = {row.account_id for row in session.query(TutorialProgress)
                    .filter_by(match_key=content.COMPLETE_ROW).all()}
        pending = [account.id for account in session.query(Account).all()
                   if account.id not in existing]
        for account_id in pending:
            session.add(TutorialProgress(account_id=account_id,
                                         match_key=content.COMPLETE_ROW,
                                         wins=0, losses=0, rewarded=False, completed=True))
        session.add(TutorialProgress(account_id="", match_key=BACKFILL_MARKER,
                                     wins=0, losses=0, rewarded=False, completed=True))
    if pending:
        logging.info(f"[Tutorial] {len(pending)} pre-tutorial account(s) marked as "
                     f"having left the funnel")
    return len(pending)


def _close_if_finished(session, account_id):
    """Sets the account-level row once every scripted match has been beaten."""
    rows = _rows(session, account_id)
    for entry in content.matches():
        row = rows.get(entry.key)
        if row is None or int(row.wins or 0) == 0:
            return False
    row = rows.get(content.COMPLETE_ROW) or _ensure_row(
        session, account_id, content.COMPLETE_ROW)
    row.completed = True
    return True


def _tutorial_pack():
    """The booster a tutorial win pays: one eligible product, chosen by match order."""
    from ptcgo.game.content.starter import starter_booster_packs
    packs = sorted(starter_booster_packs(), key=lambda product: product.key)
    if not packs:
        return None
    position = next(index for index, entry in enumerate(content.matches()) if entry.packs)
    return packs[position % len(packs)].guid
