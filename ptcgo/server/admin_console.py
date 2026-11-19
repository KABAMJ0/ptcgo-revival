"""Operator console endpoints layered on the admin API.

Every handler here runs behind admin_api.route_admin's session check, takes the
acting admin from that server-side session (never from the request body), writes
inside one db_session transaction, and records an AdminAudit row with a before /
after diff in that same transaction.
"""
import asyncio
import datetime
import glob
import json
import logging
import os
from urllib.parse import parse_qs

from sqlalchemy import func

from ptcgo.database import (db_session, Account, Collection, Deck, Wallet, TradeOffer,
                            TournamentEntry, CardOverride, CardBan, AdminAudit)
from ptcgo.database.accounts import hash_password
from ptcgo.game.attributes import AttrID
from ptcgo.game.content import card_overrides
from ptcgo.game.decks import card_bans
from ptcgo.game.scripts.cards import loader as card_loader
from ptcgo.game.scripts.products import loader as product_loader
from ptcgo.server import activity, admin_auth
from ptcgo.server import admin_api as core

MAX_DELTA = 999
MAX_WALLET = 10_000_000
BROADCAST_MAX = 300
MIN_PASSWORD = 12

# POST endpoints that only read. Everything else under POST is a mutation and is
# audited, by its handler or by route_admin's fallback.
READ_ONLY_POSTS = {
    "login", "logout", "players/detail", "cards/search", "cards/lookup",
    "players/inventory", "players/decks", "players/matches", "players/trades",
    "trades/list", "cards/detail", "cards/bodies", "players/deck",
    "players/chat", "chat/recent",
}


# ------------------------------------------------------------------ helpers

def _err(status, message):
    return core._err(status, message)


def _ok(payload=None):
    return core._ok(payload)


def _admin():
    return core.current_admin().get("username", "")


def _audit_row(session, action, target, diff, detail=""):
    """Writes the audit row inside the caller's transaction and feeds the activity view."""
    session.add(AdminAudit(admin=_admin(), action=action, target=str(target)[:190], diff_json=diff))
    core.mark_audited()
    activity.record(action, account=_admin(), detail=detail or str(target), target=str(target), diff=diff)


def _int(value, name, low, high):
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be a whole number")
    if not low <= value <= high:
        raise ValueError(f"{name} must be between {low} and {high}")
    return value


def _account(session, account_id):
    if not isinstance(account_id, str) or not account_id:
        return None
    return session.query(Account).filter_by(account_id=account_id).first()


_CARD_INDEX = {"cards": None, "by_guid": {}}


def _card_index():
    if not card_loader.cards:
        card_loader.load_all()
    if _CARD_INDEX["cards"] is not card_loader.cards:
        _CARD_INDEX["by_guid"] = {c.guid.lower(): c for c in card_loader.cards}
        _CARD_INDEX["cards"] = card_loader.cards
    return _CARD_INDEX["by_guid"]


def _product_index():
    if not product_loader.products:
        product_loader.load_all()
    return {p.guid.lower(): p for p in product_loader.products}


def item_meta(guid):
    """{guid, kind, name, set, number, image} for a card or product GUID."""
    g = str(guid or "").lower()
    card = _card_index().get(g)
    if card is not None:
        number = card.get_attribute_value(AttrID.COLLECTOR_NUMBER)
        return {"guid": card.guid, "kind": "card", "name": card.display_name or card.key,
                "set": card.key, "number": number,
                "image": core._card_image_url(card.key, number),
                "banned": card_bans.is_banned(g)}
    product = _product_index().get(g)
    if product is not None:
        image = product.get_attribute_value(AttrID.IMAGE_NAME, "")
        return {"guid": product.guid, "kind": "product", "name": product.name or product.key,
                "set": product.key, "number": None, "product_type": product.product_type,
                "image": f"/products/{image}.png" if image else None, "banned": False}
    return {"guid": g, "kind": "unknown", "name": g[:8] + "…", "set": None, "number": None,
            "image": None, "banned": False}


def _screen_names(session, ids):
    ids = {i for i in ids if i}
    if not ids:
        return {}
    rows = session.query(Account.account_id, Account.screen_name, Account.username) \
        .filter(Account.account_id.in_(ids)).all()
    return {a: (s or u) for a, s, u in rows}


def _run_on_loop(coro_factory, timeout=5.0):
    """Runs a coroutine on the TCP server's event loop from this HTTP thread."""
    from ptcgo.server import state
    server = state.ACTIVE_TCP_SERVER
    loop = getattr(server, "loop", None)
    if server is None or loop is None or not loop.is_running():
        return None, "the game server is not running in this process"
    future = asyncio.run_coroutine_threadsafe(coro_factory(server), loop)
    try:
        return future.result(timeout=timeout), None
    except Exception as exc:
        return None, str(exc) or exc.__class__.__name__


def _push_collection(account_id):
    """Best effort: refresh an online player's collection screen after a change."""
    from ptcgo.database.player_data import get_merged_collection_payload
    from ptcgo.network.message_names import OutboundMsg
    from ptcgo.network.protocol import WargFlags

    async def push(server):
        client = server.clients_by_account.get(account_id)
        if client is None:
            return False
        payload = await asyncio.to_thread(get_merged_collection_payload, account_id)
        await client.send_packet({"messageName": OutboundMsg.COLLECTION_COUNT_FOUND.value,
                                  "collectionCountList": payload}, 0, flags=WargFlags.CLEAR)
        return True

    pushed, _ = _run_on_loop(push)
    return bool(pushed)


def _offer_dict(t, names):
    def items(mapping):
        return [{**item_meta(g), "count": int(c)} for g, c in (mapping or {}).items()]
    return {
        "offer_id": t.offer_id, "status": t.status,
        "sender_id": t.sender_id, "sender": names.get(t.sender_id, t.sender_id[:8]),
        "recipient_id": t.recipient_id,
        "recipient": names.get(t.recipient_id) if t.recipient_id else None,
        "accepted_by": t.accepted_by,
        "accepted_by_name": names.get(t.accepted_by) if t.accepted_by else None,
        "offering": items(t.offering_json), "requesting": items(t.requesting_json),
        "created_at": str(t.created_at),
    }


# ---------------------------------------------------------------- players

def player_inventory(data):
    with db_session() as session:
        if _account(session, data.get("account_id")) is None:
            return _err(404, "account not found")
        rows = session.query(Collection).filter_by(account_id=data["account_id"]).all()
        items = [{**item_meta(r.archetype_id), "row_guid": r.archetype_id,
                  "tradable": r.tradable_count, "nontradable": r.nontradable_count}
                 for r in rows]
    items.sort(key=lambda i: (i["kind"] != "card", i.get("set") or "", str(i.get("number") or ""), i["name"]))
    return _ok({"items": items})


def adjust_inventory(data):
    try:
        tradable = _int(data.get("tradable", 0), "tradable", -MAX_DELTA, MAX_DELTA)
        nontradable = _int(data.get("nontradable", 0), "nontradable", -MAX_DELTA, MAX_DELTA)
    except ValueError as exc:
        return _err(400, str(exc))
    if not tradable and not nontradable:
        return _err(400, "nothing to change: both deltas are 0")
    guid = str(data.get("guid") or "").strip().lower()
    if not guid:
        return _err(400, "guid required")
    meta = item_meta(guid)
    with db_session() as session:
        account = _account(session, data.get("account_id"))
        if account is None:
            return _err(404, "account not found")
        row = session.query(Collection).filter(
            Collection.account_id == account.account_id,
            func.lower(Collection.archetype_id) == guid).first()
        if row is None and meta["kind"] == "unknown":
            return _err(404, "no loaded card or product has that GUID")
        before = {"tradable": row.tradable_count if row else 0,
                  "nontradable": row.nontradable_count if row else 0}
        after = {"tradable": before["tradable"] + tradable,
                 "nontradable": before["nontradable"] + nontradable}
        if after["tradable"] < 0 or after["nontradable"] < 0:
            return _err(409, f"the player only owns {before['tradable']} tradable and "
                             f"{before['nontradable']} non-tradable")
        if row is None:
            row = Collection(account_id=account.account_id, archetype_id=meta["guid"],
                             tradable_count=0, nontradable_count=0)
            session.add(row)
        if after["tradable"] == 0 and after["nontradable"] == 0:
            session.delete(row)
        else:
            row.tradable_count, row.nontradable_count = after["tradable"], after["nontradable"]
        diff = {"account_id": account.account_id, "guid": meta["guid"], "item": meta["name"],
                "before": before, "after": after}
        verb = "grant" if tradable + nontradable > 0 else "remove"
        _audit_row(session, "admin_inventory", account.account_id, diff,
                   detail=f"{account.username}: {verb} {meta['name']} "
                          f"tradable {tradable:+d}, non-tradable {nontradable:+d}")
    pushed = _push_collection(diff["account_id"])
    return _ok({"before": before, "after": after, "item": meta, "pushed_to_client": pushed,
                "undo": {"account_id": diff["account_id"], "guid": meta["guid"],
                         "tradable": -tradable, "nontradable": -nontradable}})


def adjust_wallet(data):
    deltas = {}
    try:
        for key in ("coins", "gems", "tickets"):
            deltas[key] = _int(data.get(key, 0), key, -MAX_WALLET, MAX_WALLET)
    except ValueError as exc:
        return _err(400, str(exc))
    if not any(deltas.values()):
        return _err(400, "nothing to change: every delta is 0")
    with db_session() as session:
        account = _account(session, data.get("account_id"))
        if account is None:
            return _err(404, "account not found")
        wallet = session.query(Wallet).filter_by(account_id=account.account_id).first()
        if wallet is None:
            return _err(404, "wallet not found")
        before = {"coins": wallet.coins, "gems": wallet.gems, "tickets": wallet.tickets}
        after = {k: before[k] + deltas[k] for k in before}
        negative = [k for k, v in after.items() if v < 0]
        if negative:
            return _err(409, f"{', '.join(negative)} would go below zero")
        wallet.coins, wallet.gems, wallet.tickets = after["coins"], after["gems"], after["tickets"]
        diff = {"account_id": account.account_id, "before": before, "after": after}
        _audit_row(session, "admin_wallet", account.account_id, diff,
                   detail=f"{account.username}: " + ", ".join(f"{k} {v:+d}" for k, v in deltas.items() if v))
    return _ok({"before": before, "after": after,
                "undo": {"account_id": diff["account_id"], **{k: -v for k, v in deltas.items()}}})


def player_decks(data):
    from ptcgo.game.decks.validation import DeckValidator
    from ptcgo.game.decks.formats import FormatManager
    from ptcgo.database.player_data import get_owned_counts
    with db_session() as session:
        account = _account(session, data.get("account_id"))
        if account is None:
            return _err(404, "account not found")
        decks = [{"id": d.id, "name": d.name, "data": d.deck_data or {}, "is_avatar": bool(d.is_avatar),
                  "wins": d.overall_wins or 0, "played": d.overall_played or 0}
                 for d in session.query(Deck).filter_by(account_id=account.account_id).all()]
        account_id = account.account_id
    owned = get_owned_counts(account_id)
    manager = FormatManager()
    out = []
    for deck in decks:
        guids = card_bans.deck_guids(deck["data"])
        counts = {}
        for g in guids:
            counts[g] = counts.get(g, 0) + 1
        rows = []
        if not deck["is_avatar"] and guids:
            try:
                validator = DeckValidator({**deck["data"], "deckID": deck["id"]}, owned_counts=owned)
                rows = [{"format": r["formatName"], "valid": r["valid"],
                         "problems": [x["failureType"] for x in r["results"]]}
                        for r in validator.validate(manager.play_format_guids())]
            except Exception as exc:
                rows = [{"format": "—", "valid": False, "problems": [f"validator error: {exc}"]}]
        out.append({
            "id": deck["id"], "name": deck["name"], "is_avatar": deck["is_avatar"],
            "wins": deck["wins"], "played": deck["played"], "size": len(guids),
            "cards": sorted(({**item_meta(g), "count": n} for g, n in counts.items()),
                            key=lambda c: (-c["count"], c["name"])),
            "banned": card_bans.banned_in(guids), "formats": rows,
        })
    return _ok({"decks": out})


def _activity_archive(days=14):
    events = []
    paths = sorted(glob.glob(os.path.join(activity.LOG_DIR, "activity-*.jsonl")))[-days:]
    for path in paths:
        try:
            with open(path, encoding="utf-8") as f:
                for line in f:
                    try:
                        events.append(json.loads(line))
                    except ValueError:
                        continue
        except OSError:
            continue
    return events


def player_matches(data):
    with db_session() as session:
        account = _account(session, data.get("account_id"))
        if account is None:
            return _err(404, "account not found")
        names = {n.lower() for n in (account.username, account.screen_name) if n}
        decks = [{"name": d.name, "wins": d.overall_wins or 0, "played": d.overall_played or 0}
                 for d in session.query(Deck).filter_by(account_id=account.account_id).all()
                 if (d.overall_played or 0) > 0]
        entries = [{"tournament_id": e.tournament_id, "wins": e.wins, "losses": e.losses,
                    "status": e.status, "history": e.history_json or []}
                   for e in session.query(TournamentEntry).filter_by(account_id=account.account_id)]
    seen, matches = set(), []
    archive = _activity_archive() + list(reversed(activity.events_since(limit=10_000)["events"]))
    for e in archive:
        if e.get("kind") not in ("match_start", "match_end", "match_refused_banned", "queue"):
            continue
        key = (e.get("at"), e.get("kind"), e.get("game_id"), e.get("detail"))
        if key in seen:
            continue
        who = (e.get("account") or "").lower()
        detail = (e.get("detail") or "").lower()
        if who in names or any(n and n in detail for n in names):
            seen.add(key)
            matches.append({k: e.get(k) for k in ("at", "kind", "account", "detail", "game_id", "queue")})
    matches.sort(key=lambda e: e.get("at") or "", reverse=True)
    return _ok({"decks": decks, "tournaments": entries, "events": matches[:300],
                "note": "Per-match results are not stored in the database; this view joins the "
                        "activity archive (match_start/match_end events), deck win counters and "
                        "tournament entry histories."})


def player_trades(data):
    account_id = data.get("account_id")
    with db_session() as session:
        if _account(session, account_id) is None:
            return _err(404, "account not found")
        rows = session.query(TradeOffer).filter(
            (TradeOffer.sender_id == account_id) | (TradeOffer.recipient_id == account_id) |
            (TradeOffer.accepted_by == account_id)).order_by(TradeOffer.created_at.desc()).limit(200).all()
        names = _screen_names(session, {x for t in rows for x in (t.sender_id, t.recipient_id, t.accepted_by)})
        return _ok({"trades": [_offer_dict(t, names) for t in rows]})


def kick_player(data):
    account_id = data.get("account_id")
    if not isinstance(account_id, str) or not account_id:
        return _err(400, "account_id required")
    if account_id == core.current_admin().get("account_id"):
        return _err(400, "you cannot kick your own session")
    reason = str(data.get("reason") or "")[:200]

    async def kick(server):
        client = server.clients_by_account.get(account_id)
        if client is None:
            return None
        name = getattr(client.player, "username", account_id)
        await client.disconnect()
        return name

    name, error = _run_on_loop(kick)
    if error:
        return _err(503, error)
    if name is None:
        return _err(404, "that player is not connected")
    with db_session() as session:
        _audit_row(session, "admin_kick", account_id, {"account_id": account_id, "reason": reason},
                   detail=f"kicked {name}" + (f": {reason}" if reason else ""))
    return _ok({"kicked": name})


# ----------------------------------------------------------------- trades

def trades_list(data):
    status = data.get("status") or None
    if status not in (None, "open", "accepted", "cancelled", "declined"):
        return _err(400, "status must be open, accepted, cancelled or declined")
    try:
        limit = _int(data.get("limit", 200), "limit", 1, 1000)
    except ValueError as exc:
        return _err(400, str(exc))
    with db_session() as session:
        q = session.query(TradeOffer)
        if status:
            q = q.filter_by(status=status)
        rows = q.order_by(TradeOffer.created_at.desc()).limit(limit).all()
        names = _screen_names(session, {x for t in rows for x in (t.sender_id, t.recipient_id, t.accepted_by)})
        counts = dict(session.query(TradeOffer.status, func.count()).group_by(TradeOffer.status).all())
        taken_down = {a.target for a in session.query(AdminAudit.target).filter_by(action="admin_trade_takedown")}
        offers = [_offer_dict(t, names) for t in rows]
    for offer in offers:
        offer["admin_cancelled"] = offer["status"] == "cancelled" and offer["offer_id"] in taken_down
    return _ok({"trades": offers, "counts": counts})


def _takedown(session, offer, reason):
    before = offer.status
    offer.status = "cancelled"
    _audit_row(session, "admin_trade_takedown", offer.offer_id,
               {"offer_id": offer.offer_id, "sender_id": offer.sender_id,
                "before": {"status": before}, "after": {"status": "cancelled"}, "reason": reason},
               detail=f"took down trade {offer.offer_id[:8]}" + (f": {reason}" if reason else ""))


def trade_cancel(data):
    reason = str(data.get("reason") or "")[:200]
    with db_session() as session:
        offer = session.query(TradeOffer).filter_by(offer_id=str(data.get("offer_id") or "")).first()
        if offer is None:
            return _err(404, "trade offer not found")
        if offer.status != "open":
            return _err(409, f"only open offers can be taken down; this one is {offer.status}")
        _takedown(session, offer, reason)
    return _ok({"offer_id": data["offer_id"], "status": "cancelled"})


def trade_cancel_account(data):
    reason = str(data.get("reason") or "")[:200]
    with db_session() as session:
        account = _account(session, data.get("account_id"))
        if account is None:
            return _err(404, "account not found")
        offers = session.query(TradeOffer).filter_by(sender_id=account.account_id, status="open").all()
        for offer in offers:
            _takedown(session, offer, reason or f"all offers by {account.username}")
        return _ok({"cancelled": [o.offer_id for o in offers]})


def trade_reopen(data):
    offer_id = str(data.get("offer_id") or "")
    with db_session() as session:
        offer = session.query(TradeOffer).filter_by(offer_id=offer_id).first()
        if offer is None:
            return _err(404, "trade offer not found")
        if offer.status != "cancelled":
            return _err(409, f"only a cancelled offer can be reopened; this one is {offer.status}")
        last = session.query(AdminAudit).filter(
            AdminAudit.target == offer_id,
            AdminAudit.action.in_(("admin_trade_takedown", "admin_trade_reopen"))) \
            .order_by(AdminAudit.id.desc()).first()
        if last is None or last.action != "admin_trade_takedown":
            return _err(409, "this offer was cancelled by its owner, not by an admin; it stays cancelled")
        offer.status = "open"
        _audit_row(session, "admin_trade_reopen", offer_id,
                   {"offer_id": offer_id, "before": {"status": "cancelled"}, "after": {"status": "open"}},
                   detail=f"reopened trade {offer_id[:8]}")
    return _ok({"offer_id": offer_id, "status": "open"})


# ------------------------------------------------------------------- bans

def _clear_archetype_caches():
    try:
        from ptcgo.packets.handlers import data_sync
        data_sync._clear_derived_caches()
    except Exception as exc:
        logging.error(f"[Admin] could not clear archetype caches: {exc}")


def _queued_with(guid):
    from ptcgo.game.session.manager import GameSessionManager
    hits = []
    for name, entries in list(GameSessionManager().queues.items()):
        for entry in list(entries or []):
            if guid in card_bans.deck_guids(entry.get("deck")):
                player = getattr(entry.get("client"), "player", None)
                hits.append({"queue": name, "account": getattr(player, "username", "?")})
    return hits


def bans_list():
    table = card_bans.reload()
    with db_session() as session:
        decks = [(d.account_id, card_bans.deck_guids(d.deck_data)) for d in session.query(Deck).all()]
    out = []
    for guid, info in table.items():
        holders = {a for a, guids in decks if guid in guids}
        out.append({**item_meta(guid), **info, "decks_holding": sum(1 for _, g in decks if guid in g),
                    "players_holding": len(holders)})
    out.sort(key=lambda b: b.get("created_at") or "", reverse=True)
    return _ok({"bans": out})


def ban_card(data):
    guid = str(data.get("guid") or "").strip().lower()
    meta = item_meta(guid)
    if meta["kind"] != "card":
        return _err(404, "no loaded card has that GUID")
    reason = str(data.get("reason") or "").strip()[:300]
    with db_session() as session:
        if session.query(CardBan).filter(func.lower(CardBan.archetype_id) == guid).first():
            return _err(409, f"{meta['name']} is already banned")
        session.add(CardBan(archetype_id=guid, reason=reason, banned_by=_admin()))
        _audit_row(session, "admin_card_ban", guid,
                   {"guid": guid, "card": f"{meta['name']} ({meta['set']} {meta['number']})",
                    "before": {"banned": False}, "after": {"banned": True}, "reason": reason},
                   detail=f"banned {meta['name']} ({meta['set']})")
    card_bans.reload()
    _clear_archetype_caches()
    return _ok({"banned": meta, "queued_with_card": _queued_with(guid)})


def unban_card(data):
    guid = str(data.get("guid") or "").strip().lower()
    with db_session() as session:
        row = session.query(CardBan).filter(func.lower(CardBan.archetype_id) == guid).first()
        if row is None:
            return _err(404, "that card is not banned")
        before = {"banned": True, "reason": row.reason, "banned_by": row.banned_by}
        session.delete(row)
        meta = item_meta(guid)
        _audit_row(session, "admin_card_unban", guid,
                   {"guid": guid, "card": meta["name"], "before": before, "after": {"banned": False}},
                   detail=f"unbanned {meta['name']}")
    card_bans.reload()
    _clear_archetype_caches()
    return _ok({"unbanned": guid, "undo": {"guid": guid, "reason": before["reason"]}})


# -------------------------------------------------------------- overrides

def _definition(guid):
    from ptcgo.game.content.definitions import CARD_DEFS_BY_GUID
    _card_index()
    return CARD_DEFS_BY_GUID.get(str(guid or "").lower())


def card_detail(data):
    guid = str(data.get("guid") or "").strip().lower()
    meta = item_meta(guid)
    definition = _definition(guid)
    if meta["kind"] != "card" or definition is None:
        return _err(404, "no loaded card has that GUID")
    with db_session() as session:
        rows = {r.title: {"spec": r.spec_json, "enabled": r.enabled, "note": r.note,
                          "updated_by": r.updated_by, "updated_at": str(r.updated_at)}
                for r in session.query(CardOverride).filter(func.lower(CardOverride.archetype_id) == guid)}
    from ptcgo.game.data_utils import Attack
    abilities = []
    for ability in getattr(definition, "abilities", None) or []:
        entry = card_overrides.describe_attack(ability)
        entry["stored_override"] = rows.get(ability.title)
        entry["body"] = body_of(ability, isinstance(ability, Attack))
        abilities.append(entry)
    return _ok({"card": meta, "abilities": abilities, "bodies": card_bodies(definition),
                "trainer": not abilities,
                "refusal": None if abilities else
                "This card has no attacks. Trainer, Energy and Ability bodies cannot be overridden."})


def overrides_list():
    with db_session() as session:
        rows = session.query(CardOverride).order_by(CardOverride.updated_at.desc()).all()
        stored = [{"guid": r.archetype_id, "title": r.title, "spec": r.spec_json, "enabled": r.enabled,
                   "note": r.note, "updated_by": r.updated_by, "updated_at": str(r.updated_at)}
                  for r in rows]
    status = {(r.get("guid"), r.get("title")): r for r in card_overrides.report}
    for row in stored:
        meta = item_meta(row["guid"])
        row["card"] = meta
        state = status.get((row["guid"].lower(), row["title"]))
        row["status"] = state["status"] if state else ("disabled" if not row["enabled"] else "pending")
        row["error"] = state.get("error") if state else None
    return _ok({"overrides": stored, "last_applied_at": card_overrides.last_applied_at,
                "last_mode": card_overrides.last_mode,
                "reload": "Saved rows apply at the next server start. 'Apply now' re-applies the "
                          "whole table to the running server without a restart."})


def override_save(data):
    guid = str(data.get("guid") or "").strip().lower()
    title = data.get("title")
    if not isinstance(title, str) or not title:
        return _err(400, "title required")
    try:
        spec = card_overrides.validate(_definition(guid), title, data.get("spec"))
    except card_overrides.OverrideError as exc:
        return _err(422, f"refused: {exc}")
    enabled = data.get("enabled", True)
    if not isinstance(enabled, bool):
        return _err(400, "enabled must be true or false")
    note = str(data.get("note") or "")[:300]
    with db_session() as session:
        row = session.query(CardOverride).filter(func.lower(CardOverride.archetype_id) == guid,
                                                 CardOverride.title == title).first()
        before = {"spec": row.spec_json, "enabled": row.enabled} if row else None
        if row is None:
            row = CardOverride(archetype_id=guid, title=title, spec_json=spec)
            session.add(row)
        row.spec_json, row.enabled, row.note, row.updated_by = spec, enabled, note, _admin()
        meta = item_meta(guid)
        _audit_row(session, "admin_card_override", f"{guid}:{title}",
                   {"guid": guid, "card": meta["name"], "title": title, "before": before,
                    "after": {"spec": spec, "enabled": enabled}},
                   detail=f"override {meta['name']} / {title}: {json.dumps(spec)[:160]}")
    return _ok({"saved": {"guid": guid, "title": title, "spec": spec, "enabled": enabled},
                "pending": True})


def override_delete(data):
    guid = str(data.get("guid") or "").strip().lower()
    title = data.get("title")
    with db_session() as session:
        row = session.query(CardOverride).filter(func.lower(CardOverride.archetype_id) == guid,
                                                 CardOverride.title == title).first()
        if row is None:
            return _err(404, "no override stored for that attack")
        before = {"spec": row.spec_json, "enabled": row.enabled, "note": row.note}
        session.delete(row)
        _audit_row(session, "admin_card_override_delete", f"{guid}:{title}",
                   {"guid": guid, "title": title, "before": before, "after": None},
                   detail=f"removed override {guid[:8]} / {title}")
    return _ok({"deleted": {"guid": guid, "title": title}, "pending": True,
                "undo": {"guid": guid, "title": title, **before}})


def overrides_apply(data):
    if data.get("confirm") != "APPLY":
        return _err(400, 'confirm with {"confirm": "APPLY"}')
    try:
        results = card_overrides.apply_live()
    except Exception as exc:
        logging.error(f"[Admin] live override apply failed: {exc}", exc_info=True)
        return _err(500, f"apply failed: {exc}")
    with db_session() as session:
        _audit_row(session, "admin_card_override_apply", "card_overrides",
                   {"applied": sum(r["status"] == "applied" for r in results),
                    "refused": [r for r in results if r["status"] != "applied"]},
                   detail=f"applied card overrides live ({len(results)} rows)")
    return _ok({"report": results})


# ----------------------------------------------------------------- server

def broadcast(data):
    message = str(data.get("message") or "").strip()
    if not message or len(message) > BROADCAST_MAX:
        return _err(400, f"message must be 1 to {BROADCAST_MAX} characters")
    from ptcgo.network.message_names import OutboundMsg
    sender = {"accountID": core.current_admin().get("account_id", ""),
              "displayName": str(data.get("sender") or "Server")[:24]}

    async def send(server):
        reached = 0
        for client in list(server.clients):
            rooms = getattr(client, "chat_rooms", None)
            if not getattr(client, "player", None) or not rooms:
                continue
            for room_id in list(rooms):
                await client.send_packet({"messageName": OutboundMsg.NOTIFY_CHAT.value, "roomID": room_id,
                                          "userInfo": sender, "message": message}, 0)
            reached += 1
        return reached

    reached, error = _run_on_loop(send)
    if error:
        return _err(503, error)
    with db_session() as session:
        _audit_row(session, "admin_broadcast", "chat", {"message": message, "reached": reached},
                   detail=f"broadcast to {reached} players: {message[:120]}")
    return _ok({"reached": reached})


def rotate_password(data, token):
    admin = core.current_admin()
    current, new = data.get("current"), data.get("new")
    if not isinstance(current, str) or not isinstance(new, str):
        return _err(400, "current and new passwords required")
    if len(new) < MIN_PASSWORD:
        return _err(400, f"the new password must be at least {MIN_PASSWORD} characters")
    if new == current:
        return _err(400, "the new password must differ from the current one")
    with db_session() as session:
        account = _account(session, admin.get("account_id"))
        if account is None:
            return _err(404, "your account no longer exists")
        if account.password_hash != hash_password(current):
            return _err(403, "current password is wrong")
        account.password_hash = hash_password(new)
        _audit_row(session, "admin_password", account.account_id,
                   {"account": account.username, "changed": True},
                   detail=f"{account.username} rotated their password")
    ended = admin_auth.destroy_sessions_for(admin.get("account_id"), keep=token)
    return _ok({"rotated": True, "other_sessions_ended": ended})


def audit_log(query_string):
    query = parse_qs(query_string or "")
    try:
        limit = max(1, min(1000, int((query.get("limit") or [200])[0])))
    except ValueError:
        return _err(400, "limit must be a number")
    target = (query.get("target") or [None])[0]
    with db_session() as session:
        q = session.query(AdminAudit)
        if target:
            q = q.filter(AdminAudit.target == target)
        rows = q.order_by(AdminAudit.id.desc()).limit(limit).all()
        return _ok({"entries": [{"id": r.id, "at": str(r.at), "admin": r.admin, "action": r.action,
                                 "target": r.target, "diff": r.diff_json} for r in rows]})


def console_meta():
    return _ok({
        "admin": _admin(),
        "energy_types": sorted(card_overrides.TYPE_BY_NAME),
        "conditions": sorted(card_overrides.CONDITION_BY_NAME),
        "damage_operators": list(card_overrides.DAMAGE_OPERATORS),
        "bans": len(card_bans.banned()),
    })


# -------------------------------------------------------------- card bodies

def _callable_source(fn):
    """'attacks_common.flip_damage' for a factory body, 'card script' for a local one."""
    module = getattr(fn, "__module__", "") or ""
    qual = (getattr(fn, "__qualname__", "") or type(fn).__name__).split(".<locals>")[0]
    if module.startswith("card_script_"):
        return f"card script: {qual}"
    return f"{module.rsplit('.', 1)[-1]}.{qual}" if module else qual


def body_of(entry, is_attack):
    """{status, source} for one attack, ability or card-level hook.

    status: stub (the unimplemented marker; an attack still deals printed damage),
    pattern (bound from the printed wording at load), admin (an override),
    scripted (a hand-written or factory body), vanilla (an attack with no
    effect beyond damage), passive / trigger (continuous or event bodies), none.
    """
    from ptcgo.game.data_utils import unimplemented
    effect = getattr(entry, "effect", None)
    source = str(getattr(entry, "effect_source", "") or "")
    passive = getattr(entry, "passive", None)
    if effect is unimplemented and passive is None:
        return {"status": "stub", "source": "unimplemented"}
    if source.startswith("admin:"):
        return {"status": "admin", "source": source[6:]}
    if source.startswith("pattern:"):
        return {"status": "pattern", "source": source[8:]}
    if effect is not None and effect is not unimplemented:
        trigger = getattr(entry, "trigger", None)
        return {"status": "scripted", "source": _callable_source(effect)
                + (f" (on {trigger})" if trigger else "")}
    if passive is not None:
        return {"status": "passive", "source": type(passive).__name__ if type(passive).__name__ != "Passive"
                else "Passive"}
    if is_attack:
        return {"status": "vanilla", "source": "printed damage only"}
    return {"status": "none", "source": "no body"}


def card_bodies(definition):
    """Every body a card carries, labelled by where it lives on the card."""
    from ptcgo.game.data_utils import Attack, TrainerCardDef, EnergyCardDef
    out = []
    for ability in getattr(definition, "abilities", None) or []:
        is_attack = isinstance(ability, Attack)
        out.append({"slot": ability.title, "kind": "attack" if is_attack else "ability",
                    "text": ability.game_text, **body_of(ability, is_attack)})
    if isinstance(definition, TrainerCardDef):
        out.append({"slot": "Trainer effect", "kind": "trainer", "text": "", **body_of(definition, False)})
        stadium = getattr(definition, "ability", None)
        if stadium is not None:
            out.append({"slot": stadium.title, "kind": "stadium", "text": stadium.game_text,
                        **body_of(stadium, False)})
    if isinstance(definition, EnergyCardDef):
        hooks = [n for n in ("on_attach", "attach_cost", "passive") if getattr(definition, n, None) is not None]
        out.append({"slot": "Energy hooks", "kind": "energy", "text": "",
                    "status": "scripted" if hooks else "none",
                    "source": ", ".join(hooks) if hooks else "provides energy only"})
    elif getattr(definition, "passive", None) is not None and not isinstance(definition, TrainerCardDef):
        out.append({"slot": "Card passive", "kind": "passive", "text": "",
                    "status": "passive", "source": type(definition.passive).__name__})
    for granted in getattr(definition, "granted_abilities", None) or []:
        out.append({"slot": granted.title, "kind": "granted ability", "text": granted.game_text,
                    **body_of(granted, False)})
    return out


BODY_STATUSES = ("stub", "scripted", "pattern", "admin", "vanilla", "passive", "none")


def card_bodies_search(data):
    from ptcgo.game.content.definitions import CARD_DEFS_BY_GUID
    query = str(data.get("query") or "").strip().lower()
    set_filter = str(data.get("set") or "").strip().upper()
    status = data.get("status") or "all"
    if status != "all" and status not in BODY_STATUSES:
        return _err(400, "status must be all or one of " + ", ".join(BODY_STATUSES))
    if not query and not set_filter:
        return _err(400, "give a query or a set code")
    try:
        limit = _int(data.get("limit", 60), "limit", 1, 300)
    except ValueError as exc:
        return _err(400, str(exc))
    _card_index()
    results, scanned = [], 0
    for card in card_loader.cards:
        if set_filter and card.key.upper() != set_filter:
            continue
        if query and query not in f"{card.display_name or ''} {card.guid} {card.key}".lower():
            continue
        definition = CARD_DEFS_BY_GUID.get(card.guid.lower())
        if definition is None:
            continue
        scanned += 1
        bodies = card_bodies(definition)
        if status != "all" and not any(b["status"] == status for b in bodies):
            continue
        counts = {}
        for b in bodies:
            counts[b["status"]] = counts.get(b["status"], 0) + 1
        results.append({**item_meta(card.guid), "bodies": bodies, "counts": counts})
        if len(results) >= limit:
            break
    return _ok({"cards": results, "matched": scanned, "truncated": len(results) >= limit})


# ------------------------------------------------------------ deck inspector

def inspect_deck(data):
    from ptcgo.game.decks.validation import DeckValidator, card_display_name
    from ptcgo.game.decks.formats import FormatManager
    from ptcgo.database.player_data import get_owned_counts
    deck_id = data.get("deck_id")
    if not isinstance(deck_id, str) or not deck_id:
        return _err(400, "deck_id required")
    with db_session() as session:
        account = _account(session, data.get("account_id"))
        if account is None:
            return _err(404, "account not found")
        deck = session.query(Deck).filter_by(account_id=account.account_id, id=deck_id).first()
        if deck is None:
            return _err(404, "that player has no deck with that id")
        deck_data, name, account_id = deck.deck_data or {}, deck.name, account.account_id
    owned = get_owned_counts(account_id)
    manager = FormatManager()
    validator = DeckValidator({**deck_data, "deckID": deck_id}, owned_counts=owned)
    formats = manager.play_format_guids()
    rows = validator.validate(formats)
    deck_problems, card_problems = [], {}
    seen_base = set()
    for row in rows:
        for detail in row["results"]:
            kind = detail["failureType"]
            text = (detail.get("explanation") or {}).get("id", "")
            per_format = kind == "DeckContainsBannedCards" or (kind == "BoolRestriction" and row["format"])
            for guid in detail["offendingArchetypeIDs"]:
                card_problems.setdefault(guid, set()).add(
                    "not legal in " + row["formatName"] if kind == "DeckContainsBannedCards" else kind)
            if not per_format and kind not in seen_base:
                seen_base.add(kind)
                deck_problems.append({"type": kind, "text": text})
    counts = {}
    for g in validator.guids:
        counts[g] = counts.get(g, 0) + 1
    by_guid = {c.guid.lower(): c for c in validator.cards}
    format_names = [manager.format_name(f) for f in formats]
    cards = []
    for guid, n in counts.items():
        card = by_guid.get(guid)
        legality = {}
        if card is not None:
            for f in formats:
                legality[manager.format_name(f)] = manager.is_card_legal(f, card)
        problems = sorted(card_problems.get(guid, ()))
        banned = card_bans.is_banned(guid)
        if banned:
            problems.insert(0, "banned on this server")
        cards.append({**item_meta(guid), "count": n, "owned": owned.get(guid),
                      "legality": legality, "problems": problems, "banned": banned,
                      "known": card is not None,
                      "copy_name": card_display_name(card) if card is not None else None})
    cards.sort(key=lambda c: (not c["problems"], c["name"]))
    return _ok({"deck": {"id": deck_id, "name": name, "size": len(validator.guids)},
                "formats": [{"format": r["formatName"], "valid": r["valid"],
                             "problems": sorted({d["failureType"] for d in r["results"]})} for r in rows],
                "format_names": format_names, "deck_problems": deck_problems, "cards": cards})


# ------------------------------------------------------------ script stubs

_SCRIPT_STUBS = {"rows": None}


def script_stub_counts():
    """{set folder: {"script_stubs", "script_stub_cards", "trainer_script_stubs"}} read from the
    card files the way ptcgo/tools/effect_coverage.py reads them (AST, never imported).
    Scripts only change with a deploy, and a deploy restarts the process, so one scan per
    process is current."""
    if _SCRIPT_STUBS["rows"] is not None:
        return _SCRIPT_STUBS["rows"]
    import ast
    from ptcgo.tools import effect_coverage as ec
    root = card_loader.scripts_dir
    rows = {}
    for set_code in sorted(os.listdir(root)):
        set_dir = os.path.join(root, set_code)
        if not os.path.isdir(set_dir) or set_code in ec.SKIP_DIRS:
            continue
        row = rows.setdefault(set_code, {"script_stubs": 0, "script_stub_cards": 0, "trainer_script_stubs": 0})
        for filename in os.listdir(set_dir):
            if not filename.endswith(".py") or filename == "__init__.py":
                continue
            try:
                with open(os.path.join(set_dir, filename), encoding="utf-8") as f:
                    tree = ast.parse(f.read())
            except (OSError, SyntaxError):
                continue
            call = ec._find_card_call(tree)
            if call is None:
                continue
            card_level = ec._is_unimplemented(
                ec._call_kwargs(call, ["guid", "key", "name", "collector_number", "set_code", "rarity"]).get("effect"))
            entries = sum(1 for node in ast.walk(call)
                          if node is not call and isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                          and node.func.id in ec.ABILITY_CALL_NAMES
                          and ec._is_unimplemented(ec._call_kwargs(node, ["title", "game_text"]).get("effect")))
            row["script_stubs"] += entries
            row["trainer_script_stubs"] += int(card_level)
            row["script_stub_cards"] += int(bool(entries or card_level))
    _SCRIPT_STUBS["rows"] = rows
    return rows


# --------------------------------------------------------------- chat log

def _chat_lines(data, account_id=None):
    from ptcgo.server import chat_log
    try:
        limit = _int(data.get("limit", 200), "limit", 1, 2000)
    except ValueError as exc:
        return None, _err(400, str(exc))
    query = data.get("query")
    if query is not None and not isinstance(query, str):
        return None, _err(400, "query must be text")
    return chat_log.recent(account_id=account_id, query=query, limit=limit), None


def player_chat(data):
    with db_session() as session:
        account = _account(session, data.get("account_id"))
        if account is None:
            return _err(404, "account not found")
        account_id = account.account_id
    lines, error = _chat_lines(data, account_id)
    from ptcgo.server import chat_log
    return error or _ok({"messages": lines, "retention_days": chat_log.RETENTION_DAYS})


def chat_recent(data):
    lines, error = _chat_lines(data)
    return error or _ok({"messages": lines})


# --------------------------------------------------------------- dispatch

def dispatch(method, endpoint, data, query_string, token):
    """Returns a response tuple, or None when the endpoint is not a console endpoint."""
    if method == "GET":
        routes = {
            "console/meta": console_meta,
            "cards/bans": bans_list,
            "cards/overrides": overrides_list,
            "cards/overrides/factories": lambda: _ok({"factories": card_overrides.factory_catalog()}),
            "audit": lambda: audit_log(query_string),
        }
        handler = routes.get(endpoint)
        return handler() if handler else None
    if method != "POST":
        return None
    routes = {
        "players/inventory": player_inventory,
        "players/inventory/adjust": adjust_inventory,
        "players/wallet/adjust": adjust_wallet,
        "players/decks": player_decks,
        "players/matches": player_matches,
        "players/trades": player_trades,
        "players/kick": kick_player,
        "players/deck": inspect_deck,
        "players/chat": player_chat,
        "chat/recent": chat_recent,
        "cards/bodies": card_bodies_search,
        "trades/list": trades_list,
        "trades/cancel": trade_cancel,
        "trades/cancel-account": trade_cancel_account,
        "trades/reopen": trade_reopen,
        "cards/bans/add": ban_card,
        "cards/bans/remove": unban_card,
        "cards/detail": card_detail,
        "cards/overrides/save": override_save,
        "cards/overrides/delete": override_delete,
        "cards/overrides/apply": overrides_apply,
        "server/broadcast": broadcast,
    }
    if endpoint == "admin/password":
        return rotate_password(data, token)
    handler = routes.get(endpoint)
    return handler(data) if handler else None
