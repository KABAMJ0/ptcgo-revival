"""Trainer Challenge end to end, headless: content, progression, payouts, match.

Runs against a throwaway SQLite file so no development database is touched.
The match leg plays a real game through `GameSession.run_gameplay_sequence`
with the AI in both seats, so it exercises the AI's turn policy and the
end-of-game result hook rather than calling the recorder directly.

    python tests/test_trainer_challenge.py
"""

import asyncio
import os
import tempfile
import unittest
import uuid

from ptcgo.game.scripts.cards import loader as card_loader

_TMP_DIR = tempfile.mkdtemp(prefix="ptcgo-tc-test-")

from ptcgo.database import connection as db_connection   # noqa: E402  (path set below)
db_connection.DB_PATH = os.path.join(_TMP_DIR, "test.db")

from ptcgo.database import Base, engine, db_session, Collection, Wallet   # noqa: E402
from ptcgo.database import trainer_challenge_data                         # noqa: E402
from ptcgo.game.content import trainer_challenge as content               # noqa: E402
from ptcgo.game.session.ai_player import AIPlayer                         # noqa: E402
from ptcgo.game.session.constants import GamePhase                        # noqa: E402
from ptcgo.game.session.legal_actions import ACTION_USE_ATTACK           # noqa: E402
from ptcgo.game.session.game_session import GameSession                   # noqa: E402
from ptcgo.game.session.manager import GameSessionManager                 # noqa: E402
from ptcgo.packets.handlers.league import (                                # noqa: E402
    ChallengePlayHandler, LeagueHandler,
)

ACCOUNT = "tc-test-account"
RIVAL = "tc-test-rival"


def setUpModule():
    card_loader.load_all()
    Base.metadata.create_all(engine)


def _wallet_coins(account_id):
    with db_session() as session:
        wallet = session.query(Wallet).filter_by(account_id=account_id).first()
        return int(wallet.coins) if wallet else 0


def _collection(account_id):
    with db_session() as session:
        return {row.archetype_id: row.nontradable_count + row.tradable_count
                for row in session.query(Collection).filter_by(account_id=account_id).all()}


class TrainerChallengeContentTest(unittest.TestCase):
    def test_every_opponent_deck_resolves_to_sixty_cards(self):
        for league in content.leagues():
            for opponent in league.opponents:
                deck = content.opponent_deck(opponent)
                self.assertEqual(len(deck["piles"]["deck"]), 60,
                                 f"{opponent.name} ({opponent.deck}) is not a 60-card deck")

    def test_reward_schedule_matches_the_client_shape(self):
        schedule = content.reward_schedule()
        self.assertEqual(sorted(schedule, key=int), [str(i) for i in range(len(content.leagues()))])
        for items in schedule.values():
            self.assertEqual(len(items), 1)
            amount = items[0]["A"]["amount"]
            self.assertEqual(amount["name"], content.TOKENS)
            self.assertGreater(amount["value"], 0)

    def test_opponent_keys_are_unique(self):
        keys = [opponent.key for league in content.leagues() for opponent in league.opponents]
        self.assertEqual(len(keys), len(set(keys)))


class TrainerChallengeProgressTest(unittest.TestCase):
    def setUp(self):
        trainer_challenge_data.reset(ACCOUNT)

    def tearDown(self):
        trainer_challenge_data.reset(ACCOUNT)

    def test_only_the_first_opponent_starts_available(self):
        rows = trainer_challenge_data.status_rows(ACCOUNT)
        self.assertEqual(len(rows), 12)
        self.assertEqual(rows[0]["status"], "Available")
        self.assertTrue(all(row["status"] == "Unavailable" for row in rows[1:]))

    def test_a_win_pays_the_opponent_and_unlocks_the_next(self):
        first = content.leagues()[0].opponents[0]
        before = _wallet_coins(ACCOUNT)
        result = trainer_challenge_data.record_result(ACCOUNT, first.key, won=True)
        self.assertTrue(result["ok"])
        self.assertEqual(result["granted"]["coins"], first.coins)
        self.assertEqual(_wallet_coins(ACCOUNT), before + first.coins)
        self.assertIn(content.leagues()[0].opponents[1].key, result["unlocked"])
        rows = {row["key"]: row["status"] for row in trainer_challenge_data.status_rows(ACCOUNT)}
        self.assertEqual(rows[first.key], "Completed")
        self.assertEqual(rows[content.leagues()[0].opponents[1].key], "Available")

    def test_a_loss_records_but_pays_nothing(self):
        first = content.leagues()[0].opponents[0]
        before = _wallet_coins(ACCOUNT)
        result = trainer_challenge_data.record_result(ACCOUNT, first.key, won=False)
        self.assertEqual(result["granted"]["coins"], 0)
        self.assertEqual(_wallet_coins(ACCOUNT), before)
        self.assertEqual(trainer_challenge_data.losses(ACCOUNT), 1)
        # A loss leaves the Trainer playable: only beating one advances the league.
        rows = {row["key"]: row["status"] for row in trainer_challenge_data.status_rows(ACCOUNT)}
        self.assertEqual(rows[first.key], "Available")

    def test_rewards_are_paid_only_once(self):
        first = content.leagues()[0].opponents[0]
        trainer_challenge_data.record_result(ACCOUNT, first.key, won=True)
        coins = _wallet_coins(ACCOUNT)
        again = trainer_challenge_data.record_result(ACCOUNT, first.key, won=True)
        self.assertEqual(again["granted"]["coins"], 0)
        self.assertEqual(_wallet_coins(ACCOUNT), coins)

    def test_clearing_a_league_pays_its_bonus_and_a_booster_pack(self):
        league = content.leagues()[0]
        for opponent in league.opponents[:-1]:
            trainer_challenge_data.record_result(ACCOUNT, opponent.key, won=True)
        before = _wallet_coins(ACCOUNT)
        collection = _collection(ACCOUNT)
        result = trainer_challenge_data.record_result(
            ACCOUNT, league.opponents[-1].key, won=True)
        self.assertEqual(result["league_completed"], league.key)
        self.assertEqual(_wallet_coins(ACCOUNT), before + league.opponents[-1].coins + league.coins)
        granted_packs = result["granted"]["products"]
        self.assertEqual(len(granted_packs), 1)
        (pack_guid, count), = granted_packs.items()
        self.assertEqual(count, league.packs)
        self.assertEqual(_collection(ACCOUNT).get(pack_guid),
                         collection.get(pack_guid, 0) + league.packs)
        self.assertEqual(
            {row["key"]: row["status"] for row in trainer_challenge_data.status_rows(ACCOUNT)}
            [content.leagues()[1].opponents[0].key], "Available")

    def test_reset_restores_the_league_to_unplayed(self):
        league = content.leagues()[0]
        for opponent in league.opponents:
            trainer_challenge_data.record_result(ACCOUNT, opponent.key, won=True)
        trainer_challenge_data.reset(ACCOUNT, league.key)
        rows = {row["key"]: row["status"] for row in trainer_challenge_data.status_rows(ACCOUNT)}
        self.assertEqual(rows[league.opponents[0].key], "Available")
        self.assertEqual(rows[league.opponents[1].key], "Unavailable")
        self.assertEqual(trainer_challenge_data.load(ACCOUNT), {})

    def test_unknown_opponent_records_nothing(self):
        self.assertFalse(trainer_challenge_data.record_result(ACCOUNT, "nobody", won=True)["ok"])


class _ScoredSession(GameSession):
    """Real session with no choreography pacing and a count of the AI's attacks."""

    def __init__(self, game_id, pairing):
        super().__init__(game_id, pairing)
        self.choreography_pauses = False
        self.attacks = 0

    async def _apply_player_action(self, player_id, entry, target_ids):
        if entry["selectableAction"]["description"] == ACTION_USE_ATTACK:
            self.attacks += 1
        return await super()._apply_player_action(player_id, entry, target_ids)


class TrainerChallengeMatchTest(unittest.TestCase):
    """One real match: the AI attacks, and the finished game is scored and paid."""

    def test_a_played_match_records_its_result(self):
        trainer_challenge_data.reset(ACCOUNT)
        opponent = content.leagues()[0].opponents[0]
        session = _ScoredSession(str(uuid.uuid4()), {
            "is_solo": True,
            "solitaire_id": opponent.key,
            "solo_context": {"account_id": ACCOUNT, "opponent": opponent.key},
            "players": {
                ACCOUNT: {"client": None, "deck": content.opponent_deck(opponent)},
                RIVAL: {"client": None, "deck": content.opponent_deck(
                    content.leagues()[0].opponents[1])},
            },
        })

        async def play():
            await asyncio.wait_for(session.run_gameplay_sequence(), timeout=180)

        asyncio.run(play())

        self.assertEqual(session.game_phase, GamePhase.GAME_OVER)
        self.assertGreater(session.attacks, 0, "the AI never took an attack")
        progress = trainer_challenge_data.load(ACCOUNT)
        self.assertIn(opponent.key, progress,
                      "the finished league match was not scored")
        self.assertEqual(progress[opponent.key]["wins"] + progress[opponent.key]["losses"], 1)


class _StubPlayer:
    def __init__(self, account_id, deck):
        self.account_id = account_id
        self.username = "TestPlayer"
        self.screen_name = "TestPlayer"
        self.decks = [{"deck_data": deck}]


class _StubClient:
    """Just enough client for the league handlers: captures the packets sent."""

    def __init__(self, account_id, deck):
        self.addr = "test"
        self.player = _StubPlayer(account_id, deck)
        self.sent = []

    async def send_packet(self, payload, request_id=0, flags=0):
        self.sent.append(payload)


class LeagueHandlerTest(unittest.TestCase):
    """The wire payloads and the Play path, driven without a socket."""

    def setUp(self):
        trainer_challenge_data.reset(ACCOUNT)
        self.deck = content.opponent_deck(content.leagues()[0].opponents[0])
        self.client = _StubClient(ACCOUNT, self.deck)

    def tearDown(self):
        manager = GameSessionManager()
        for game_id, pairing in list(manager.pending_pairings.items()):
            if pairing.get("solo_context", {}).get("account_id") == ACCOUNT:
                manager.pending_pairings.pop(game_id, None)
        trainer_challenge_data.reset(ACCOUNT)

    def test_status_lists_named_opponents_in_unlock_order(self):
        handler = LeagueHandler(self.client)
        asyncio.run(handler.handle_league_status({}, 1, 0))
        packet = self.client.sent[-1]
        self.assertEqual(packet["messageName"], "LeagueAndGymModeStatus")
        opponents = packet["status"]["opponents"]
        self.assertEqual(len(opponents), 12)
        self.assertEqual(opponents[0]["name"], {"id": "Zach"})
        self.assertEqual(opponents[0]["image"], "zach_landingpage")
        self.assertEqual(opponents[0]["status"], "Available")
        self.assertEqual(opponents[1]["status"], "Unavailable")
        self.assertFalse(packet["status"]["waitingForRewards"])
        self.assertEqual(packet["status"]["losses"], 0)

    def test_rewards_return_a_populated_schedule(self):
        handler = LeagueHandler(self.client)
        asyncio.run(handler.handle_league_rewards({}, 1, 0))
        packet = self.client.sent[-1]
        self.assertEqual(packet["messageName"], "LeagueAndGymModeRewards")
        self.assertEqual(sorted(packet["totalRewardSchedule"], key=int), ["0", "1"])

    def test_play_starts_the_selected_opponent_with_their_own_deck(self):
        handler = ChallengePlayHandler(self.client)
        asyncio.run(handler.handle_league_play({"opponentName": "Zach"}, 7, 0))
        self.assertEqual(self.client.sent[-1]["messageName"], "ConfirmReadyForMatch")
        manager = GameSessionManager()
        pairing = next(pairing for pairing in manager.pending_pairings.values()
                       if pairing.get("solo_context", {}).get("account_id") == ACCOUNT)
        self.assertEqual(pairing["solo_context"]["opponent"], "zach")
        self.assertEqual(pairing["solitaire_id"], "zach")
        self.assertEqual(pairing["players"][ACCOUNT]["deck"], self.deck)
        opponent_deck = next(pairing["players"][key]["deck"] for key
                             in pairing["players"] if key != ACCOUNT)
        self.assertEqual(opponent_deck, content.opponent_deck(
            content.leagues()[0].opponents[0]))

    def test_play_refuses_a_locked_opponent(self):
        handler = ChallengePlayHandler(self.client)
        asyncio.run(handler.handle_league_play({"opponentName": "Tyson"}, 8, 0))
        packet = self.client.sent[-1]
        self.assertEqual(packet["messageName"], "LeagueAndGymModeError")
        self.assertEqual(packet["msg"]["id"], "league.error.unavailable")

    def test_reset_clears_the_named_league(self):
        trainer_challenge_data.record_result(ACCOUNT, "zach", won=True)
        handler = LeagueHandler(self.client)
        asyncio.run(handler.handle_league_reset({"leagueName": "gold"}, 9, 0))
        self.assertEqual(trainer_challenge_data.load(ACCOUNT), {})


if __name__ == "__main__":
    unittest.main(verbosity=2)
