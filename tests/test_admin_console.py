"""Headless tests for the admin operator console.

Every new endpoint is checked authorised, unauthorised and with malformed input,
against a throwaway SQLite database. The pre-existing endpoints are swept once to
prove they still answer. Card behaviour overrides are driven through the real
resolve_attack entry point, and card bans through deck validation and matchmaking.
"""
import asyncio
import json
import os
import tempfile
import threading
import unittest
import uuid
from types import SimpleNamespace
from unittest.mock import patch

_TMP = tempfile.mkdtemp(prefix="ptcgo_admin_console_")
os.environ["PTCGO_ACTIVITY_LOG_DIR"] = _TMP

from ptcgo.database import connection  # noqa: E402

connection.DB_PATH = os.path.join(_TMP, "admin_console.db")
connection.engine.dispose()

from ptcgo.database import (  # noqa: E402
    Base, engine, db_session, Account, Wallet, Collection, Deck, TradeOffer, AdminAudit,
    CardOverride, CardBan)
from ptcgo.database.accounts import hash_password  # noqa: E402

Base.metadata.create_all(engine)

from ptcgo.server import admin_api, admin_auth, admin_console, activity  # noqa: E402
from ptcgo.server import state as server_state  # noqa: E402
from ptcgo.game.content import card_overrides  # noqa: E402
from ptcgo.game.content.definitions import ABILITIES_BY_ID, CARD_DEFS_BY_GUID  # noqa: E402
from ptcgo.game.decks import card_bans  # noqa: E402
from ptcgo.game.scripts.cards import loader as card_loader  # noqa: E402

activity.LOG_DIR = _TMP
card_loader.load_all()

ADMIN_PASS = "correct horse battery"
BLITZLE = "9435d343-3a3b-5989-abf6-9ae4bd56775f"   # BW1 Blitzle 40, vanilla "Rear Kick" 20


def _vanilla_card():
    return CARD_DEFS_BY_GUID[BLITZLE]


def call(method, endpoint, body=None, token=None, raw=None):
    headers = {"Cookie": f"{admin_auth.COOKIE_NAME}={token}"} if token else {}
    payload = raw if raw is not None else (json.dumps(body).encode() if body is not None else None)
    result = admin_api.route_admin(method, "/admin/api/" + endpoint, payload, headers=headers)
    status, data = result[0], result[1]
    try:
        parsed = json.loads(data)
    except (ValueError, TypeError):
        parsed = None
    return status, parsed


def audits(action):
    with db_session() as s:
        return [(r.admin, r.target, r.diff_json) for r in
                s.query(AdminAudit).filter_by(action=action).order_by(AdminAudit.id)]


class LoopServer:
    """A stand-in TCP server: a real event loop on a thread plus fake clients."""

    def __init__(self):
        self.loop = asyncio.new_event_loop()
        threading.Thread(target=self.loop.run_forever, daemon=True).start()
        self.clients, self.clients_by_account = [], {}

    def add(self, account_id, username, rooms=()):
        sent, closed = [], []

        async def send_packet(packet, request_id, flags=0):
            sent.append(packet)

        async def disconnect():
            closed.append(True)
            self.clients.remove(client)
            self.clients_by_account.pop(account_id, None)

        client = SimpleNamespace(player=SimpleNamespace(account_id=account_id, username=username,
                                                        screen_name=username),
                                 chat_rooms=set(rooms), send_packet=send_packet,
                                 disconnect=disconnect, sent=sent, closed=closed)
        self.clients.append(client)
        self.clients_by_account[account_id] = client
        return client

    def stop(self):
        self.loop.call_soon_threadsafe(self.loop.stop)


class AdminConsoleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.admin_id, cls.p1, cls.p2 = (str(uuid.uuid4()) for _ in range(3))
        with db_session() as s:
            for account_id, name, is_admin in ((cls.admin_id, "root", True),
                                               (cls.p1, "ash", False), (cls.p2, "misty", False)):
                s.add(Account(account_id=account_id, username=name, screen_name=name.title(),
                              password_hash=hash_password(ADMIN_PASS), is_admin=is_admin))
                s.add(Wallet(account_id=account_id, coins=1000, gems=5, tickets=10))
            s.add(Collection(account_id=cls.p1, archetype_id=BLITZLE, tradable_count=3, nontradable_count=1))
            cls.deck_id = str(uuid.uuid4())
            s.add(Deck(id=cls.deck_id, account_id=cls.p1, name="Zap",
                       deck_data={"piles": {"deck": [BLITZLE] * 5 + ["00000000-0000-0000-0000-000000000000"]}}))
        status, _ = call("POST", "login", {"username": "root", "password": ADMIN_PASS})
        assert status == 200
        cls.token = next(t for t, s in admin_auth._sessions.items() if s["username"] == "root")

    def setUp(self):
        with db_session() as s:
            s.query(TradeOffer).delete()
            s.query(CardBan).delete()
            s.query(CardOverride).delete()
        card_bans.reload()
        card_overrides.apply_live()

    def post(self, endpoint, body=None):
        return call("POST", endpoint, body, token=self.token)

    def get(self, endpoint):
        return call("GET", endpoint, token=self.token)

    def _open_trade(self, sender=None):
        offer_id = str(uuid.uuid4())
        with db_session() as s:
            s.add(TradeOffer(offer_id=offer_id, sender_id=sender or self.p1, recipient_id=None,
                             offering_json={BLITZLE: 1}, requesting_json={BLITZLE: 2}, status="open"))
        return offer_id

    # ------------------------------------------------------------ auth gate

    NEW_GETS = ["console/meta", "cards/bans", "cards/overrides", "cards/overrides/factories", "audit"]
    NEW_POSTS = ["players/inventory", "players/inventory/adjust", "players/wallet/adjust",
                 "players/decks", "players/matches", "players/trades", "players/kick",
                 "trades/list", "trades/cancel", "trades/cancel-account", "trades/reopen",
                 "cards/bans/add", "cards/bans/remove", "cards/detail", "cards/overrides/save",
                 "cards/overrides/delete", "cards/overrides/apply", "server/broadcast", "admin/password",
                 "players/deck", "cards/bodies", "players/chat", "chat/recent"]

    def test_every_new_endpoint_refuses_without_a_session(self):
        for endpoint in self.NEW_GETS:
            self.assertEqual(call("GET", endpoint)[0], 401, endpoint)
            self.assertEqual(call("GET", endpoint, token="forged")[0], 401, endpoint)
        for endpoint in self.NEW_POSTS:
            status, body = call("POST", endpoint, {"account_id": self.p1, "guid": BLITZLE})
            self.assertEqual(status, 401, endpoint)
            self.assertFalse(body["ok"])
        with db_session() as s:
            self.assertEqual(s.query(Collection).filter_by(account_id=self.p1).one().tradable_count, 3)

    def test_every_new_post_rejects_a_non_object_body(self):
        for endpoint in self.NEW_POSTS:
            self.assertEqual(call("POST", endpoint, raw=b"[1,2]", token=self.token)[0], 400, endpoint)
            self.assertEqual(call("POST", endpoint, raw=b"{nope", token=self.token)[0], 400, endpoint)

    # ------------------------------------------------------------ inventory

    def test_inventory_add_remove_and_undo(self):
        status, body = self.post("players/inventory/adjust",
                                 {"account_id": self.p1, "guid": BLITZLE.upper(), "tradable": 2})
        self.assertEqual(status, 200, body)
        self.assertEqual(body["after"], {"tradable": 5, "nontradable": 1})
        status, body = self.post("players/inventory/adjust", {**body["undo"]})
        self.assertEqual(status, 200, body)
        status, body = self.post("players/inventory/adjust",
                                 {"account_id": self.p1, "guid": BLITZLE, "nontradable": -1})
        self.assertEqual(body["after"], {"tradable": 3, "nontradable": 0})
        status, body = self.post("players/inventory", {"account_id": self.p1})
        self.assertEqual([(i["guid"].lower(), i["tradable"], i["nontradable"]) for i in body["items"]],
                         [(BLITZLE, 3, 0)])
        admin, target, diff = audits("admin_inventory")[-1]
        self.assertEqual((admin, target), ("root", self.p1))
        self.assertEqual(diff["before"], {"tradable": 3, "nontradable": 1})
        self.post("players/inventory/adjust", {"account_id": self.p1, "guid": BLITZLE, "nontradable": 1})

    def test_inventory_removing_everything_deletes_the_row(self):
        self.post("players/inventory/adjust", {"account_id": self.p2, "guid": BLITZLE, "tradable": 1})
        status, body = self.post("players/inventory/adjust",
                                 {"account_id": self.p2, "guid": BLITZLE, "tradable": -1})
        self.assertEqual(status, 200, body)
        with db_session() as s:
            self.assertIsNone(s.query(Collection).filter_by(account_id=self.p2).first())

    def test_inventory_malformed(self):
        cases = [
            ({"account_id": self.p1, "guid": BLITZLE, "tradable": -9}, 409),
            ({"account_id": self.p1, "guid": BLITZLE}, 400),
            ({"account_id": self.p1, "guid": BLITZLE, "tradable": "2"}, 400),
            ({"account_id": self.p1, "guid": BLITZLE, "tradable": 1.5}, 400),
            ({"account_id": self.p1, "guid": BLITZLE, "tradable": 10_000}, 400),
            ({"account_id": self.p1, "guid": str(uuid.uuid4()), "tradable": 1}, 404),
            ({"account_id": "nobody", "guid": BLITZLE, "tradable": 1}, 404),
            ({"account_id": self.p1, "tradable": 1}, 400),
        ]
        for body, expected in cases:
            self.assertEqual(self.post("players/inventory/adjust", body)[0], expected, body)
        self.assertEqual(self.post("players/inventory", {"account_id": 7})[0], 404)
        with db_session() as s:
            self.assertEqual(s.query(Collection).filter_by(account_id=self.p1).one().tradable_count, 3)

    def test_inventory_pushes_to_an_online_player(self):
        server = LoopServer()
        client = server.add(self.p2, "misty")
        try:
            with patch.object(server_state, "ACTIVE_TCP_SERVER", server):
                status, body = self.post("players/inventory/adjust",
                                         {"account_id": self.p2, "guid": BLITZLE, "nontradable": 2})
            self.assertEqual(status, 200, body)
            self.assertTrue(body["pushed_to_client"])
            self.assertEqual(client.sent[-1]["messageName"], "CollectionCountFound")
            counts = {c["archetypeID"]: c for c in client.sent[-1]["collectionCountList"]}
            self.assertEqual(counts[BLITZLE]["nontradable"], 2)
        finally:
            server.stop()
            self.post("players/inventory/adjust", {"account_id": self.p2, "guid": BLITZLE, "nontradable": -2})

    # --------------------------------------------------------------- wallet

    def test_wallet_adjust_and_malformed(self):
        status, body = self.post("players/wallet/adjust", {"account_id": self.p2, "coins": 250, "gems": -5})
        self.assertEqual(status, 200, body)
        self.assertEqual(body["after"], {"coins": 1250, "gems": 0, "tickets": 10})
        self.assertEqual(self.post("players/wallet/adjust", {"account_id": self.p2, "gems": -1})[0], 409)
        self.assertEqual(self.post("players/wallet/adjust", {"account_id": self.p2})[0], 400)
        self.assertEqual(self.post("players/wallet/adjust", {"account_id": self.p2, "coins": True})[0], 400)
        self.assertEqual(self.post("players/wallet/adjust", {"account_id": "x", "coins": 1})[0], 404)
        self.assertEqual(self.post("players/wallet/adjust", body["undo"])[0], 200)
        self.assertEqual(audits("admin_wallet")[-2][2]["after"]["coins"], 1250)

    def test_existing_wallet_set_now_audits_a_diff(self):
        status, _ = self.post("players/wallet", {"account_id": self.p2, "coins": 1000, "gems": 5, "tickets": 11})
        self.assertEqual(status, 200)
        admin, _, diff = audits("admin_wallet")[-1]
        self.assertEqual(admin, "root")
        self.assertEqual((diff["before"]["tickets"], diff["after"]["tickets"]), (10, 11))
        self.post("players/wallet", {"account_id": self.p2, "coins": 1000, "gems": 5, "tickets": 10})

    # ------------------------------------------------------ decks / matches

    def test_player_decks_matches_trades(self):
        status, body = self.post("players/decks", {"account_id": self.p1})
        self.assertEqual(status, 200, body)
        deck = body["decks"][0]
        self.assertEqual((deck["name"], deck["size"], deck["cards"][0]["count"]), ("Zap", 6, 5))
        self.assertTrue(deck["formats"] and not any(f["valid"] for f in deck["formats"]))  # 4 cards
        activity.record("match_end", account="Ash", detail="beat Misty (prizes)", game_id="g1")
        status, body = self.post("players/matches", {"account_id": self.p1})
        self.assertEqual(status, 200, body)
        self.assertEqual(body["events"][0]["game_id"], "g1")
        self._open_trade()
        status, body = self.post("players/trades", {"account_id": self.p1})
        self.assertEqual((status, len(body["trades"])), (200, 1))
        self.assertEqual(body["trades"][0]["offering"][0]["name"], "Blitzle")
        for endpoint in ("players/decks", "players/matches", "players/trades"):
            self.assertEqual(self.post(endpoint, {"account_id": "missing"})[0], 404, endpoint)
            self.assertEqual(self.post(endpoint, {})[0], 404, endpoint)

    # ------------------------------------------------------- deck inspector

    def test_inspect_deck_marks_each_card(self):
        status, body = self.post("players/deck", {"account_id": self.p1, "deck_id": self.deck_id})
        self.assertEqual(status, 200, body)
        cards = {c["guid"].lower(): c for c in body["cards"]}
        blitzle, unknown = cards[BLITZLE], cards["00000000-0000-0000-0000-000000000000"]
        self.assertIn("MaxDuplicates", blitzle["problems"])
        self.assertIn("UnownedCards", blitzle["problems"])
        self.assertEqual((blitzle["count"], blitzle["owned"]), (5, 4))
        self.assertTrue(blitzle["legality"]["Unlimited"])
        self.assertFalse(unknown["known"])
        self.assertIn("MustNotContain", unknown["problems"])
        self.assertIn("ExactSize", {p["type"] for p in body["deck_problems"]})
        self.post("cards/bans/add", {"guid": BLITZLE, "reason": "inspect"})
        status, body = self.post("players/deck", {"account_id": self.p1, "deck_id": self.deck_id})
        blitzle = next(c for c in body["cards"] if c["guid"].lower() == BLITZLE)
        self.assertTrue(blitzle["banned"])
        self.assertEqual(blitzle["problems"][0], "banned on this server")
        self.assertFalse(any(blitzle["legality"].values()))
        self.assertEqual(self.post("players/deck", {"account_id": self.p1, "deck_id": "nope"})[0], 404)
        self.assertEqual(self.post("players/deck", {"account_id": self.p2, "deck_id": self.deck_id})[0], 404)
        self.assertEqual(self.post("players/deck", {"account_id": self.p1})[0], 400)
        self.assertEqual(self.post("players/deck", {"account_id": "x", "deck_id": self.deck_id})[0], 404)

    # ----------------------------------------------------------- card bodies

    def test_card_bodies_report_what_each_body_is(self):
        from ptcgo.game.data_utils import unimplemented
        status, body = self.post("cards/bodies", {"query": "Blitzle", "set": "BW1"})
        self.assertEqual(status, 200, body)
        rear_kick = next(b for c in body["cards"] if c["guid"].lower() == BLITZLE for b in c["bodies"])
        self.assertEqual((rear_kick["slot"], rear_kick["status"]), ("Rear Kick", "vanilla"))
        # every reported status agrees with the live object it describes
        for status_name in ("stub", "pattern", "scripted"):
            status, body = self.post("cards/bodies", {"query": "a", "status": status_name, "limit": 5})
            self.assertEqual(status, 200, body)
            self.assertTrue(body["cards"], status_name)
            for card in body["cards"]:
                definition = CARD_DEFS_BY_GUID[card["guid"].lower()]
                live = {a.title: a for a in getattr(definition, "abilities", None) or []}
                for b in card["bodies"]:
                    if b["slot"] not in live:
                        continue
                    a = live[b["slot"]]
                    if b["status"] == "stub":
                        self.assertIs(a.effect, unimplemented)
                    if b["status"] == "pattern":
                        self.assertEqual(a.effect_source, "pattern:" + b["source"])
                    if b["status"] == "scripted":
                        self.assertIsNotNone(a.effect)
                        self.assertIsNot(a.effect, unimplemented)
        self.post("cards/overrides/save", {"guid": BLITZLE, "title": "Rear Kick", "spec": {"effect": None, "damage": 30}})
        self.post("cards/overrides/apply", {"confirm": "APPLY"})
        status, body = self.post("cards/detail", {"guid": BLITZLE})
        self.assertEqual(body["abilities"][0]["body"], {"status": "admin", "source": "vanilla"})
        for bad in ({}, {"query": "a", "status": "weird"}, {"query": "a", "limit": 0}, {"query": "a", "limit": "3"}):
            self.assertEqual(self.post("cards/bodies", bad)[0], 400, bad)

    def test_coverage_shows_both_counts(self):
        from ptcgo.tools import effect_coverage
        status, body = self.get("monitor/coverage")
        self.assertEqual(status, 200, body)
        totals = body["totals"]
        self.assertEqual(totals["script_stubs"], totals["stubbed"] + totals["wording"])
        by_set = {r["set"]: r for r in body["sets"]}
        for row in body["sets"]:
            self.assertEqual(row["script_stubs"], row["stubbed"] + row["wording"], row["set"])
        infos = effect_coverage.scan_cards(only_set="BASE1")
        self.assertEqual(by_set["BASE1"]["script_stub_cards"], sum(i.is_stub for i in infos))
        self.assertEqual(by_set["BASE1"]["script_stubs"],
                         sum(len(i.signature) for i in infos))
        self.assertGreater(totals["trainer_effects"], 0)
        # Abilities a wording pattern bound as passives keep the marker as their effect;
        # they have a body and must not count as stubs (165 did before this fix).
        self.assertEqual(totals["wording"], card_loader.pattern_bound)
        status, body = self.post("cards/bodies", {"query": "Safeguard", "set": "BW10"})
        for card in body["cards"]:
            for b in card["bodies"]:
                if b["slot"] == "Safeguard":
                    self.assertEqual(b["status"], "pattern")

    def test_chat_log_records_and_reads(self):
        from ptcgo.packets.handlers.social import SocialHandler
        sent = []

        async def send_packet(packet, request_id=0, flags=0):
            sent.append(packet)
        sender = SimpleNamespace(player=SimpleNamespace(account_id=self.p1, screen_name="Ash", username="ash"),
                                 chat_rooms={"Lobby_Spirit_1"}, send_packet=send_packet, addr=("127.0.0.1", 1))
        sender.server = SimpleNamespace(clients=[sender], clients_by_account={self.p1: sender})
        handler = SocialHandler(sender)
        asyncio.run(handler.handle_room_chat({"roomID": "Lobby_Spirit_1", "message": "trade me your Blitzle or else"}, 0, 0))
        asyncio.run(handler.handle_private_chat({"accountID": self.p2, "message": "psst scam offer"}, 0, 0))
        status, body = self.post("players/chat", {"account_id": self.p1, "limit": 10})
        self.assertEqual(status, 200, body)
        kinds = [(m["kind"], m["message"]) for m in body["messages"][:2]]
        self.assertEqual(kinds, [("private", "psst scam offer"), ("room", "trade me your Blitzle or else")])
        status, body = self.post("players/chat", {"account_id": self.p2})
        self.assertEqual([m["message"] for m in body["messages"]][:1], ["psst scam offer"])
        status, body = self.post("chat/recent", {"query": "blitzle"})
        self.assertEqual((status, body["messages"][0]["from"]), (200, "Ash"))
        before = len(audits("admin_call"))
        for bad, code in (({"account_id": "nobody"}, 404), ({"account_id": self.p1, "limit": 0}, 400),
                          ({"account_id": self.p1, "limit": "5"}, 400), ({"account_id": self.p1, "query": 5}, 400)):
            self.assertEqual(self.post("players/chat", bad)[0], code, bad)
        self.assertEqual(self.post("chat/recent", {"limit": 99999})[0], 400)
        self.assertEqual(len(audits("admin_call")), before)  # read-only: no audit rows

    def test_fonts_are_self_hosted(self):
        page = admin_api.route_admin("GET", "/admin", None)[1].decode()
        self.assertNotIn("googleapis", page)
        self.assertNotIn("gstatic", page)
        import re as _re
        fonts = _re.findall(r"url\((/admin/fonts/[a-z0-9-]+\.woff2)\)", page)
        self.assertEqual(len(fonts), 6)
        for url in fonts:
            status, payload, ctype = admin_api.route_admin("GET", url, None)[:3]
            self.assertEqual((status, ctype), (200, "font/woff2"))
            self.assertEqual(payload[:4], b"wOF2")
        for bad in ("/admin/fonts/../admin_api.py", "/admin/fonts/OFL.txt", "/admin/fonts/x.woff2"):
            self.assertEqual(admin_api.route_admin("GET", bad, None)[0], 404, bad)

    # ----------------------------------------------------------------- kick

    def test_kick(self):
        self.assertEqual(self.post("players/kick", {"account_id": self.p1})[0], 503)  # no server
        server = LoopServer()
        client = server.add(self.p1, "ash")
        try:
            with patch.object(server_state, "ACTIVE_TCP_SERVER", server):
                status, body = self.post("players/kick", {"account_id": self.p1, "reason": "spam"})
                self.assertEqual(status, 200, body)
                self.assertEqual(client.closed, [True])
                self.assertEqual(self.post("players/kick", {"account_id": self.p1})[0], 404)
                self.assertEqual(self.post("players/kick", {"account_id": self.admin_id})[0], 400)
                self.assertEqual(self.post("players/kick", {})[0], 400)
        finally:
            server.stop()
        self.assertEqual(audits("admin_kick")[-1][2]["reason"], "spam")

    # --------------------------------------------------------------- trades

    def test_trade_takedown_and_reopen(self):
        offer_id = self._open_trade()
        status, body = self.post("trades/list", {"status": "open"})
        self.assertEqual([t["offer_id"] for t in body["trades"]], [offer_id])
        status, body = self.post("trades/cancel", {"offer_id": offer_id, "reason": "scam"})
        self.assertEqual(status, 200, body)
        self.assertEqual(self.post("trades/cancel", {"offer_id": offer_id})[0], 409)
        status, body = self.post("trades/list", {"status": "cancelled"})
        self.assertTrue(body["trades"][0]["admin_cancelled"])
        status, body = self.post("trades/reopen", {"offer_id": offer_id})
        self.assertEqual(status, 200, body)
        with db_session() as s:
            self.assertEqual(s.query(TradeOffer).filter_by(offer_id=offer_id).one().status, "open")
        diff = audits("admin_trade_takedown")[-1][2]
        self.assertEqual((diff["before"]["status"], diff["after"]["status"]), ("open", "cancelled"))

    def test_trade_reopen_refuses_an_owner_cancel(self):
        offer_id = self._open_trade()
        with db_session() as s:
            s.query(TradeOffer).filter_by(offer_id=offer_id).one().status = "cancelled"
        self.assertEqual(self.post("trades/reopen", {"offer_id": offer_id})[0], 409)

    def test_trade_cancel_account_and_malformed(self):
        ids = [self._open_trade(), self._open_trade(), self._open_trade(sender=self.p2)]
        status, body = self.post("trades/cancel-account", {"account_id": self.p1})
        self.assertEqual((status, sorted(body["cancelled"])), (200, sorted(ids[:2])))
        self.assertEqual(self.post("trades/cancel-account", {"account_id": "x"})[0], 404)
        self.assertEqual(self.post("trades/cancel", {"offer_id": "missing"})[0], 404)
        self.assertEqual(self.post("trades/cancel", {})[0], 404)
        self.assertEqual(self.post("trades/reopen", {"offer_id": "missing"})[0], 404)
        self.assertEqual(self.post("trades/list", {"status": "weird"})[0], 400)
        self.assertEqual(self.post("trades/list", {"limit": 0})[0], 400)
        self.assertEqual(self.post("trades/list", {"limit": "5"})[0], 400)

    # ----------------------------------------------------------------- bans

    def test_ban_refuses_validation_and_matchmaking(self):
        from ptcgo.game.decks.validation import validate_deck
        from ptcgo.game.decks.formats import FormatManager
        from ptcgo.game.session.manager import GameSessionManager

        deck = {"deckID": "d", "piles": {"deck": [BLITZLE] * 4}}
        formats = FormatManager().play_format_guids()
        from ptcgo.game.attributes import DeckFormat
        unlimited = validate_deck(deck, [DeckFormat.UNLIMITED.value])[0]
        self.assertNotIn("DeckContainsBannedCards", [r["failureType"] for r in unlimited["results"]])
        status, body = self.post("cards/bans/add", {"guid": BLITZLE, "reason": "test"})
        self.assertEqual(status, 200, body)
        self.assertTrue(card_bans.is_banned(BLITZLE.upper()))
        for row in validate_deck(deck, formats):
            offenders = sum((r["offendingArchetypeIDs"] for r in row["results"]
                             if r["failureType"] == "DeckContainsBannedCards"), [])
            self.assertIn(BLITZLE, offenders, row["formatName"])

        manager = GameSessionManager()
        sent = []

        async def send_packet(packet, request_id, flags=0):
            sent.append(packet)
        client = SimpleNamespace(player=SimpleNamespace(account_id=self.p1, username="ash"),
                                 addr=("127.0.0.1", 1), send_packet=send_packet)
        asyncio.run(manager.add_to_queue(client, "Unlimited", deck, {}))
        self.assertEqual(sent[-1]["messageName"], "MatchRequestError")
        self.assertIn("Blitzle", sent[-1]["errorMsg"]["id"])
        self.assertNotIn(client, [e["client"] for e in manager.queues.get("Unlimited", [])])
        asyncio.run(manager.start_solo_match(client, deck, "solo", {}))
        self.assertEqual(sent[-1]["messageName"], "MatchRequestError")

        game_id = "banned-" + uuid.uuid4().hex
        manager.pending_pairings[game_id] = {"players": {
            self.p1: {"client": client, "deck": deck, "ready": True},
            "bot": {"client": None, "deck": {}, "ready": True}}, "is_solo": True}
        asyncio.run(manager._transition_to_game(game_id))
        self.assertNotIn(game_id, manager.active_sessions)
        self.assertEqual(sent[-1]["messageName"], "MatchRequestError")

        status, body = self.get("cards/bans")
        self.assertEqual((body["bans"][0]["guid"].lower(), body["bans"][0]["decks_holding"]), (BLITZLE, 1))
        status, body = self.post("cards/bans/remove", {"guid": BLITZLE})
        self.assertEqual(status, 200, body)
        self.assertFalse(card_bans.is_banned(BLITZLE))
        self.assertEqual(audits("admin_card_ban")[-1][0], "root")

    def test_ban_malformed(self):
        self.assertEqual(self.post("cards/bans/add", {"guid": str(uuid.uuid4())})[0], 404)
        self.assertEqual(self.post("cards/bans/add", {})[0], 404)
        self.assertEqual(self.post("cards/bans/add", {"guid": BLITZLE})[0], 200)
        self.assertEqual(self.post("cards/bans/add", {"guid": BLITZLE})[0], 409)
        self.assertEqual(self.post("cards/bans/remove", {"guid": str(uuid.uuid4())})[0], 404)

    # ------------------------------------------------------------ overrides

    def _drive_attack(self, flips=None):
        """Resolves Blitzle's first attack through the engine; returns the amounts dealt."""
        from ptcgo.tools import effect_smoke as smoke
        from ptcgo.game.session.effects import EffectContext, resolve_attack

        dealt = []
        original = EffectContext.deal_damage

        async def spy(ctx, amount=None, target=None, *args, **kwargs):
            if target is None:
                dealt.append(amount if amount is not None else ctx.ability.damage)
            return await original(ctx, amount, target, *args, **kwargs)

        async def fixed_flips(ctx, count, title="", *args, **kwargs):
            return list(flips)[:count]

        async def drive():
            rig = smoke.Rig(_vanilla_card(), smoke.pick_filler_basic(), smoke.basic_energy_guids())
            try:
                entities = rig.setup("pokemon")
                attack = ABILITIES_BY_ID[_vanilla_card().abilities[0].ability_id]
                await resolve_attack(rig.session, smoke.P1, entities["p1_active"], attack, attack.ability_id)
            except smoke.GameOver:
                pass
            finally:
                rig.session.cleanup()

        with patch.object(EffectContext, "deal_damage", spy):
            if flips is not None:
                with patch.object(EffectContext, "flip_coins", fixed_flips):
                    asyncio.run(drive())
            else:
                asyncio.run(drive())
        return dealt

    def _pie_entry(self):
        from ptcgo.game.attributes import AttrID
        card = card_loader.cards_by_guid[BLITZLE]
        return json.loads(card.attributes[str(AttrID.PIE_ABILITIES.value)]["value"])[0]

    def test_override_changes_the_engine_and_the_client_payload_then_reverts(self):
        self.assertEqual(self._drive_attack(), [20])
        status, body = self.post("cards/overrides/save", {
            "guid": BLITZLE, "title": "Rear Kick",
            "spec": {"damage": 50, "cost": {"Lightning": 2},
                     "effect": {"module": "attacks_common", "factory": "flip_damage",
                                "kwargs": {"coins": 2, "per_heads": 30}}}})
        self.assertEqual(status, 200, body)
        self.assertEqual(self._drive_attack(flips=[True, True]), [20])   # saved, not yet applied
        status, body = self.post("cards/overrides/apply", {"confirm": "APPLY"})
        self.assertEqual(status, 200, body)
        self.assertEqual(body["report"][0]["status"], "applied")
        self.assertEqual(self._drive_attack(flips=[True, True]), [60])
        self.assertEqual(self._drive_attack(flips=[True, False]), [30])
        self.assertEqual((self._pie_entry()["damage"], self._pie_entry()["cost"]), (50, {"Lightning": 2}))

        status, body = self.post("cards/overrides/save", {"guid": BLITZLE, "title": "Rear Kick",
                                                          "spec": {"damage": 70, "effect": None}})
        self.post("cards/overrides/apply", {"confirm": "APPLY"})
        self.assertEqual(self._drive_attack(), [70])

        status, body = self.post("cards/overrides/delete", {"guid": BLITZLE, "title": "Rear Kick"})
        self.assertEqual(status, 200, body)
        self.post("cards/overrides/apply", {"confirm": "APPLY"})
        self.assertEqual(self._drive_attack(), [20])
        self.assertEqual(self._pie_entry()["damage"], 20)
        self.assertIsNone(_vanilla_card().abilities[0].effect)
        diff = audits("admin_card_override")[-1][2]
        self.assertEqual(diff["before"]["spec"]["damage"], 50)

    def test_override_applies_at_boot_through_the_loader(self):
        with db_session() as s:
            s.add(CardOverride(archetype_id=BLITZLE, title="Rear Kick", spec_json={"damage": 90}))
        try:
            card_loader.load_all(force=True)
            self.assertEqual(len(card_loader.last_errors), 0)
            self.assertEqual(CARD_DEFS_BY_GUID[BLITZLE].abilities[0].damage, 90)
            self.assertEqual(self._pie_entry()["damage"], 90)
            self.assertEqual(card_overrides.report[0]["status"], "applied")
        finally:
            with db_session() as s:
                s.query(CardOverride).delete()
            card_loader.load_all(force=True)
        self.assertEqual(CARD_DEFS_BY_GUID[BLITZLE].abilities[0].damage, 20)

    def test_override_refuses_what_it_cannot_express(self):
        ability_card = next(d for d in CARD_DEFS_BY_GUID.values()
                            if any(type(a).__name__ == "Ability" for a in getattr(d, "abilities", []) or []))
        ability_title = next(a.title for a in ability_card.abilities if type(a).__name__ == "Ability")
        refused = [
            {"guid": ability_card.guid, "title": ability_title, "spec": {"damage": 10}},
            {"guid": BLITZLE, "title": "Rear Kick", "spec": {"retreat_cost": 0}},
            {"guid": BLITZLE, "title": "Rear Kick", "spec": {"effect": {"factory": "flip_damage",
                                                                      "kwargs": {"also": "x"}}}},
            {"guid": BLITZLE, "title": "Rear Kick", "spec": {"effect": {"factory": "damage_per",
                                                                      "kwargs": {"per": 10}}}},
            {"guid": BLITZLE, "title": "Rear Kick", "spec": {"effect": {"factory": "flip_damage_table",
                                                                      "kwargs": {"steps": {"1": 10}}}}},
            {"guid": BLITZLE, "title": "Rear Kick", "spec": {"effect": {"factory": "os.system"}}},
            {"guid": BLITZLE, "title": "Rear Kick", "spec": {"effect": {"module": "trainers",
                                                                      "factory": "heal"}}},
            {"guid": BLITZLE, "title": "Rear Kick", "spec": {"effect": {"factory": "flip_damage",
                                                                      "kwargs": {"coins": "2"}}}},
            {"guid": BLITZLE, "title": "Rear Kick", "spec": {"cost": {"Plasma": 1}}},
            {"guid": BLITZLE, "title": "Rear Kick", "spec": {"damage": -10}},
            {"guid": BLITZLE, "title": "Rear Kick", "spec": {}},
            {"guid": BLITZLE, "title": "No Such Attack", "spec": {"damage": 10}},
            {"guid": str(uuid.uuid4()), "title": "Rear Kick", "spec": {"damage": 10}},
        ]
        for body in refused:
            status, response = self.post("cards/overrides/save", body)
            self.assertEqual(status, 422, (body, response))
            self.assertTrue(response["error"].startswith("refused"), response)
        self.assertEqual(self.post("cards/overrides/save", {"guid": BLITZLE})[0], 400)
        self.assertEqual(self.post("cards/overrides/save", {"guid": BLITZLE, "title": "Rear Kick",
                                                            "spec": {"damage": 10}, "enabled": "yes"})[0], 400)
        self.assertEqual(self.post("cards/overrides/apply", {})[0], 400)
        self.assertEqual(self.post("cards/overrides/delete", {"guid": BLITZLE, "title": "Rear Kick"})[0], 404)
        with db_session() as s:
            self.assertEqual(s.query(CardOverride).count(), 0)

    def test_card_detail_and_catalog(self):
        status, body = self.post("cards/detail", {"guid": BLITZLE})
        self.assertEqual(status, 200, body)
        self.assertEqual(body["abilities"][0]["title"], "Rear Kick")
        self.assertEqual(body["abilities"][0]["effect"], "vanilla")
        self.assertEqual(self.post("cards/detail", {"guid": "zzz"})[0], 404)
        status, body = self.get("cards/overrides/factories")
        names = {f["factory"] for f in body["factories"]}
        self.assertIn("flip_damage", names)
        self.assertNotIn("damage_per", names)
        flip = next(f for f in body["factories"] if f["factory"] == "flip_damage")
        self.assertIn("also", flip["not_settable"])
        self.assertEqual(self.get("cards/overrides")[0], 200)

    # --------------------------------------------------------------- server

    def test_broadcast(self):
        self.assertEqual(self.post("server/broadcast", {"message": "hi"})[0], 503)
        server = LoopServer()
        in_lobby = server.add(self.p1, "ash", rooms=["Lobby_Spirit_1"])
        nowhere = server.add(self.p2, "misty")
        try:
            with patch.object(server_state, "ACTIVE_TCP_SERVER", server):
                status, body = self.post("server/broadcast", {"message": "Restart at 22:00"})
                self.assertEqual((status, body["reached"]), (200, 1))
                self.assertEqual(self.post("server/broadcast", {"message": ""})[0], 400)
                self.assertEqual(self.post("server/broadcast", {"message": "x" * 301})[0], 400)
        finally:
            server.stop()
        self.assertEqual(in_lobby.sent[-1]["messageName"], "NotifyChat")
        self.assertEqual(in_lobby.sent[-1]["message"], "Restart at 22:00")
        self.assertEqual(nowhere.sent, [])

    def test_password_rotation_uses_the_session_account(self):
        status, _ = call("POST", "login", {"username": "root", "password": ADMIN_PASS})
        other = [t for t, s in admin_auth._sessions.items() if s["username"] == "root" and t != self.token]
        self.assertEqual(self.post("admin/password", {"current": "wrong", "new": "x" * 14})[0], 403)
        self.assertEqual(self.post("admin/password", {"current": ADMIN_PASS, "new": "short"})[0], 400)
        self.assertEqual(self.post("admin/password", {"current": ADMIN_PASS, "new": ADMIN_PASS})[0], 400)
        self.assertEqual(self.post("admin/password", {"new": "x" * 14})[0], 400)
        status, body = self.post("admin/password", {"current": ADMIN_PASS, "new": "a much longer secret",
                                                     "account_id": self.p1})
        self.assertEqual(status, 200, body)
        self.assertGreaterEqual(body["other_sessions_ended"], 1)
        self.assertTrue(all(admin_auth.get_session(t) is None for t in other))
        with db_session() as s:
            self.assertEqual(s.query(Account).filter_by(account_id=self.p1).one().password_hash,
                             hash_password(ADMIN_PASS))
            s.query(Account).filter_by(account_id=self.admin_id).one().password_hash = hash_password(ADMIN_PASS)
        diff = audits("admin_password")[-1][2]
        self.assertNotIn(ADMIN_PASS, json.dumps(diff))

    def test_self_protection(self):
        self.assertEqual(self.post("players/ban", {"account_id": self.admin_id})[0], 400)
        self.assertEqual(self.post("players/delete", {"account_id": self.admin_id, "confirm": "DELETE"})[0], 400)
        self.assertEqual(self.post("accounts/set-admin", {"account_id": self.admin_id, "is_admin": False})[0], 400)

    def test_audit_log_and_generic_mutation_audit(self):
        status, _ = self.post("codes", {"code": "AUDITME", "reward": {"coins": 1}})
        self.assertEqual(status, 200)
        admin, target, diff = audits("admin_call")[-1]
        self.assertEqual((admin, target, diff["request"]["code"]), ("root", "codes", "AUDITME"))
        status, body = self.get("audit?limit=1")
        self.assertEqual((status, body["entries"][0]["action"]), (200, "admin_call"))
        self.assertEqual(self.get("audit?limit=abc")[0], 400)
        self.post("codes/delete", {"code": "AUDITME"})


class PreExistingEndpointsAnswer(unittest.TestCase):
    """Every endpoint the panel had before the console still routes and answers."""

    GETS = ["metrics", "overview", "products", "accounts", "monitor/activity?limit=5",
            "monitor/sessions", "monitor/counters", "monitor/coverage", "monitor/live", "players",
            "trades", "versus-seasons", "formats", "tournaments", "codes", "shop", "pages",
            "pages/assets", "tournaments/standings/none"]
    # Endpoints that write tracked json_data files or rebuild bundles are checked with
    # input they refuse, which proves they route without touching the files.
    POSTS = [("players/detail", {"account_id": "missing"}, 404),
             ("cards/search", {"query": "blitzle"}, 200),
             ("cards/lookup", {"guids": [BLITZLE]}, 200),
             ("accounts/grant-all-cards", {}, 400),
             ("accounts/grant-all-products", {}, 400),
             ("accounts/set-admin", {}, 400),
             ("players/collection/clear", {"account_id": "missing"}, 404),
             ("players/wallet", {"account_id": "missing"}, 404),
             ("players/ban", {"account_id": "missing"}, 404),
             ("players/delete", {"account_id": "missing", "confirm": "no"}, 400),
             ("versus-seasons", {"seasons": []}, 400),
             ("formats", {"formats": "nope"}, 400),
             ("tournaments", {"definition": None}, 400),
             ("tournaments/toggle", {"tournament_id": "none"}, 404),
             ("tournaments/delete", {"tournament_id": "none"}, 404),
             ("codes/update", {"code": "none"}, 404),
             ("codes/delete", {"code": "none"}, 404),
             ("shop", {}, 400),
             ("shop/toggle", {"id": -1}, 404),
             ("shop/delete", {"id": -1}, 404),
             ("pages", {}, 400),
             ("pages/toggle", {"id": "x"}, 400),
             ("pages/delete", {"id": -1}, 404),
             ("pages/assets/custom", {"image": "nope"}, 400)]

    @classmethod
    def setUpClass(cls):
        with db_session() as s:
            if s.query(Account).filter_by(username="sweeper").first() is None:
                s.add(Account(account_id=str(uuid.uuid4()), username="sweeper", screen_name="Sweeper",
                              password_hash=hash_password(ADMIN_PASS), is_admin=True))

    def test_preexisting_endpoints_answer(self):
        status, _ = call("POST", "login", {"username": "sweeper", "password": ADMIN_PASS})
        self.assertEqual(status, 200)
        token = next(t for t, s in admin_auth._sessions.items() if s["username"] == "sweeper")
        self.assertEqual(call("GET", "session", token=token)[1]["authenticated"], True)
        self.assertEqual(admin_api.route_admin("GET", "/admin", None)[0], 200)
        for endpoint in self.GETS:
            status, body = call("GET", endpoint, token=token)
            self.assertEqual(status, 200, (endpoint, body))
        self.assertEqual(call("GET", "cards/search", token=token)[0], 400)
        self.assertIn(call("GET", "card-image/BW1/40", token=token)[0], (200, 404))
        for endpoint, body, expected in self.POSTS:
            status, response = call("POST", endpoint, body, token=token)
            self.assertEqual(status, expected, (endpoint, response))
            self.assertNotIn("unknown endpoint", (response or {}).get("error", ""))
        status, _ = call("POST", "logout", token=token)
        self.assertEqual(status, 200)


if __name__ == "__main__":
    unittest.main()
