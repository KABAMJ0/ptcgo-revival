"""Server-wide card bans: refused by deck validation in every format and at matchmaking.

Mirrors how formats.json `bannedCards` works, one level up: FormatManager asks
`is_banned` before any per-format rule, so a banned card fails validation in every
format (DeckContainsBannedCards) and shows as illegal in the client's deck builder,
and GameSessionManager refuses a deck holding one before it can reach a game.

The list lives in the `card_bans` table and is cached here; the admin API calls
`reload()` after every change.
"""
import logging
import threading
from typing import Dict, Iterable, List, Optional

_lock = threading.Lock()
_banned: Optional[Dict[str, dict]] = None


def _load() -> Dict[str, dict]:
    from ptcgo.game.content.card_overrides import _table_ready
    if not _table_ready("card_bans"):
        return {}
    from ptcgo.database import db_session, CardBan
    with db_session() as session:
        return {row.archetype_id.lower(): {"reason": row.reason, "banned_by": row.banned_by,
                                           "created_at": str(row.created_at or "")}
                for row in session.query(CardBan)}


def banned() -> Dict[str, dict]:
    global _banned
    if _banned is None:
        with _lock:
            if _banned is None:
                try:
                    _banned = _load()
                except Exception as exc:
                    logging.error("[CardBans] could not read card_bans: %s", exc)
                    return {}
    return _banned


def reload() -> Dict[str, dict]:
    global _banned
    with _lock:
        _banned = _load()
    return _banned


def is_banned(guid) -> bool:
    return str(guid or "").lower() in banned()


def deck_guids(deck_data) -> List[str]:
    piles = (deck_data or {}).get("piles") or {}
    return [str(g).lower() for g in (piles.get("deck") or piles.get("CakePile") or [])]


def banned_in(guids: Iterable[str]) -> List[str]:
    table = banned()
    if not table:
        return []
    return sorted({str(g).lower() for g in guids if str(g).lower() in table})


def display_names(guids: Iterable[str]) -> List[str]:
    from ptcgo.game.scripts.cards import loader as card_loader
    by_guid = {c.guid.lower(): c for c in card_loader.cards}
    out = []
    for g in guids:
        card = by_guid.get(str(g).lower())
        out.append(f"{card.display_name or card.key} ({card.key})" if card else str(g))
    return out


def refusal_text(deck_data) -> Optional[str]:
    """The message a player sees when their deck holds a banned card, else None."""
    hits = banned_in(deck_guids(deck_data))
    if not hits:
        return None
    return "Your deck contains a card banned on this server: " + ", ".join(display_names(hits[:3])) + \
        (f" and {len(hits) - 3} more" if len(hits) > 3 else "") + "."
