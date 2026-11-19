"""The scripted tutorial funnel end to end, headless.

Walks a fresh account from the intro's data load through both scripted matches,
the reward claim and the booster landing in the collection, then plays a real
match through `GameSession.run_gameplay_sequence` so the result hook is
exercised rather than called directly.

    python tests/test_tutorial_funnel.py
"""

import asyncio
import os
import tempfile
import unittest
import uuid

from ptcgo.game.scripts.cards import loader as card_loader

_TMP_DIR = tempfile.mkdtemp(prefix="ptcgo-tutorial-test-")

from ptcgo.database import connection as db_connection   # noqa: E402
db_connection.DB_PATH = os.path.join(_TMP_DIR, "test.db")

from ptcgo.database import Base, engine, db_session, Collection, Wallet   # noqa: E402
from ptcgo.database import tutorial_data                                 # noqa: E402
from ptcgo.game.content import tutorial as content                       # noqa: E402
from ptcgo.game.session.constants import GamePhase                       # noqa: E402
from ptcgo.game.session.game_session import GameSession                   # noqa: E402
from ptcgo.game.session.manager import GameSessionManager                  # noqa: E402
from ptcgo.packets.handlers.league import (                                # noqa: E402
    ChallengePlayHandler, LeagueHandler,
)
from ptcgo.packets.handlers.tutorial import TutorialHandler               # noqa: E402

ACCOUNT = "tutorial-test-account"
RIVAL = "tutorial-test-rival"


def setUpModule():
    card_loader.load_all()
    Base.metadata.create_all(engine)


def _coins(account_id):
    with db_session() as session:
        wallet = session.query(Wallet).filter_by(account_id=account_id).first()
        return int(wallet.coins) if wallet else 0


def _collection(account_id):
    with db_session() as session:
        return {row.archetype_id: row.nontradable_count + row.tradable_count
                for row in session.query(Collection).filter_by(account_id=account_id).all()}


class _StubPlayer:
    def __init__(self, account_id, decks=()):
        self.account_id = account_id
        self.username = "TestPlayer"
        self.screen_name = "TestPlayer"
        self.decks = list(decks)

    def get_wallet_data(self):
        return {"coins": 0, "gems": 0, "tickets": 0}


class _StubClient:
    """Just enough client for the tutorial handlers: captures the packets sent."""

    def __init__(self, account_id, decks=()):
        self.addr = "test"
        self.player = _StubPlayer(account_id, decks)
        self.sent = []
        self.sent_ids = []

    async def send_packet(self, payload, request_id=0, flags=0):
        self.sent.append(payload)
        self.sent_ids.append(request_id)

    def names(self):
        return [packet.get("messageName") for packet in self.sent]


class TutorialContentTest(unittest.TestCase):
    def test_both_scripted_decks_resolve_to_sixty_cards(self):
        for match in content.matches():
            deck = content.opponent_deck(match)
            self.assertEqual(len(deck["piles"]["deck"]), 60,
                             f"{match.name} ({match.deck}) is not a 60-card deck")

    def test_the_schedule_is_contiguous_from_zero(self):
        schedule = content.reward_schedule()
        self.assertEqual(sorted(schedule, key=int), [str(i) for i in range(len(content.matches()))])

    def test_the_roster_matches_the_client_script(self):
        self.assertEqual([match.name for match in content.matches()], ["Ella", "Zach"])


class TutorialProgressTest(unittest.TestCase):
    def setUp(self):
        tutorial_data.reset(ACCOUNT)

    def tearDown(self):
        tutorial_data.reset(ACCOUNT)

    def test_a_fresh_account_starts_on_the_first_match(self):
        rows = tutorial_data.status_rows(ACCOUNT)
        self.assertEqual([row["status"] for row in rows], ["Available", "Available"])
        self.assertEqual(tutorial_data.next_match(ACCOUNT).key, content.matches()[0].key)
        self.assertFalse(tutorial_data.completed(ACCOUNT))

    def test_a_win_leaves_its_payout_pending_until_it_is_claimed(self):
        first = content.matches()[0]
        before = _coins(ACCOUNT)
        result = tutorial_data.record_result(ACCOUNT, first.key, won=True)
        self.assertTrue(result["ok"])
        self.assertFalse(result["completed"])
        self.assertTrue(tutorial_data.rewards_pending(ACCOUNT))
        self.assertEqual(_coins(ACCOUNT), before, "a win paid before the claim")
        claimed = tutorial_data.claim(ACCOUNT)
        self.assertTrue(claimed["claimed"])
        self.assertEqual(_coins(ACCOUNT), before + first.coins)
        self.assertFalse(tutorial_data.rewards_pending(ACCOUNT))
        self.assertFalse(tutorial_data.claim(ACCOUNT)["claimed"], "the payout was paid twice")

    def test_a_loss_records_but_pays_nothing(self):
        first = content.matches()[0]
        before = _coins(ACCOUNT)
        result = tutorial_data.record_result(ACCOUNT, first.key, won=False)
        self.assertTrue(result["ok"])
        self.assertFalse(tutorial_data.rewards_pending(ACCOUNT))
        self.assertEqual(tutorial_data.losses(ACCOUNT), 1)
        self.assertEqual(_coins(ACCOUNT), before)

    def test_the_second_win_closes_the_funnel_and_pays_the_booster(self):
        for match in content.matches():
            tutorial_data.record_result(ACCOUNT, match.key, won=True)
        self.assertTrue(tutorial_data.completed(ACCOUNT))
        self.assertIsNone(tutorial_data.next_match(ACCOUNT))
        claimed = tutorial_data.claim(ACCOUNT)
        self.assertTrue(claimed["granted"]["products"], "the tutorial paid no booster")
        collection = _collection(ACCOUNT)
        for guid in claimed["granted"]["products"]:
            self.assertGreater(collection.get(guid, 0), 0, "the booster never landed")
        self.assertEqual(tutorial_data.status_rows(ACCOUNT), [])

    def test_an_unknown_match_records_nothing(self):
        self.assertFalse(tutorial_data.record_result(ACCOUNT, "nope", won=True)["ok"])

    def test_a_skipped_funnel_is_not_replayed(self):
        tutorial_data.mark_completed(ACCOUNT, reason="test")
        self.assertTrue(tutorial_data.completed(ACCOUNT))
        self.assertEqual(tutorial_data.status_rows(ACCOUNT), [])


class TutorialWireTest(unittest.TestCase):
    """The messages the funnel scene actually exchanges, driven without a socket."""

    def setUp(self):
        tutorial_data.reset(ACCOUNT)
        self.client = _StubClient(ACCOUNT)

    def tearDown(self):
        manager = GameSessionManager()
        for game_id, pairing in list(manager.pending_pairings.items()):
            if pairing.get("solo_context", {}).get("account_id") == ACCOUNT:
                manager.pending_pairings.pop(game_id, None)
        tutorial_data.reset(ACCOUNT)

    def test_the_funnel_scene_loads_tutorial_status_and_rewards(self):
        league = LeagueHandler(self.client)
        asyncio.run(league.handle_league_status({"subMode": "tutorial"}, 1, 0))
        asyncio.run(league.handle_league_rewards({"subMode": "tutorial"}, 2, 0))
        self.assertEqual(self.client.names(), ["LeagueAndGymModeStatus", "LeagueAndGymModeRewards"])
        status = self.client.sent[0]["status"]
        self.assertEqual([row["name"] for row in status["opponents"]], ["Ella", "Zach"])
        self.assertFalse(status["waitingForRewards"])
        self.assertEqual(sorted(self.client.sent[1]["totalRewardSchedule"], key=int), ["0", "1"])

    def test_a_normal_league_request_is_untouched(self):
        league = LeagueHandler(self.client)
        asyncio.run(league.handle_league_status({}, 1, 0))
        self.assertEqual(len(self.client.sent[0]["status"]["opponents"]), 12)

    def test_play_starts_the_scripted_trainer_with_their_own_deck(self):
        handler = TutorialHandler(self.client)
        pairing = asyncio.run(self._play_and_capture_pairing(
            lambda rid: handler.handle_tutorial_play({"index": 0}, rid, 0), 5))
        match = content.matches()[0]
        self.assertEqual(pairing["solo_context"]["tutorial"], match.key)
        self.assertEqual(pairing["solitaire_id"], match.key)
        opponent = pairing["players"][next(pid for pid in pairing["players"]
                                           if pid.startswith("0000"))]
        self.assertEqual(len(opponent["deck"]["piles"]["deck"]), 60)

    async def _play_and_capture_pairing(self, play, request_id):
        """Plays, then reports the pairing the manager built for it."""
        created = {}
        manager = GameSessionManager()
        original = manager._transition_to_game

        async def capture(game_id):
            created.update(manager.pending_pairings.get(game_id) or {})
            await original(game_id)

        manager._transition_to_game = capture
        try:
            await play(request_id)
        finally:
            manager._transition_to_game = original
        for game_id in [gid for gid, pairing in list(manager.pending_pairings.items())
                        if pairing.get("solo_context", {}).get("account_id") == ACCOUNT]:
            manager.pending_pairings.pop(game_id, None)
        return created

    def test_a_play_request_acknowledges_before_the_match_events(self):
        """The reply completes the RPC; the game start is its own event behind it."""
        manager = GameSessionManager()
        sent = []
        original = manager._transition_to_game

        async def fake_start(game_id):
            await self.client.send_packet({"messageName": "MatchFound"}, 0)

        manager._transition_to_game = fake_start
        try:
            asyncio.run(TutorialHandler(self.client).handle_tutorial_play({"index": 0}, 5, 0))
        finally:
            manager._transition_to_game = original
        for game_id in list(manager.pending_pairings):
            manager.pending_pairings.pop(game_id, None)
        self.assertEqual(self.client.names(), [None, "MatchFound"])
        self.assertEqual(self.client.sent_ids, [5, 0],
                         "the game start must not ride on the request id")

    def test_the_intros_play_button_also_starts_a_tutorial_match(self):
        """The intro sends the league Play message with the tutorial subMode, no index."""
        handler = ChallengePlayHandler(self.client)
        pairing = asyncio.run(self._play_and_capture_pairing(
            lambda rid: handler.handle_league_play({"subMode": "tutorial"}, rid, 0), 9))
        self.assertEqual(pairing["solo_context"]["tutorial"], content.matches()[0].key)
        self.assertEqual(self.client.names(), [None], "the play request was not acknowledged")

    def test_play_gives_a_fresh_account_a_deck_to_play_with(self):
        self.assertEqual(self.client.player.decks, [])
        handler = TutorialHandler(self.client)
        asyncio.run(handler.handle_tutorial_play({"index": 0}, 5, 0))
        self.assertEqual(len(self.client.player.decks), 1)
        self.assertEqual(len(self.client.player.decks[0]["deck_data"]["piles"]["deck"]), 60)
        pile = self.client.player.decks[0]["deck_data"]["piles"]["deck"]
        self.assertGreaterEqual(_collection(ACCOUNT).get(pile[0], 0), pile.count(pile[0]),
                                "the starter deck's cards were not added to the collection")

    def test_a_fresh_account_walks_the_whole_funnel(self):
        """Every step of the funnel, in the order the scene asks for it."""
        league = LeagueHandler(self.client)
        tutorial = TutorialHandler(self.client)

        asyncio.run(league.handle_league_status({"subMode": "tutorial"}, 1, 0))
        asyncio.run(league.handle_league_rewards({"subMode": "tutorial"}, 2, 0))
        self.assertEqual(
            [row["status"] for row in self.client.sent[0]["status"]["opponents"]],
            ["Available", "Available"])

        for index, match in enumerate(content.matches()):
            self.client.sent.clear()
            pairing = asyncio.run(self._play_and_capture_pairing(
                lambda rid, i=index: tutorial.handle_tutorial_play({"index": i}, rid, 0),
                10 + index))
            self.assertEqual(self.client.names(), [None], "the play request was not acknowledged")
            self.assertEqual(pairing["solo_context"]["tutorial"], match.key)
            self.assertEqual(len(pairing["players"][ACCOUNT]["deck"]["piles"]["deck"]), 60)

            tutorial_data.record_result(ACCOUNT, match.key, won=True)

            self.client.sent.clear()
            asyncio.run(league.handle_league_status({"subMode": "tutorial"}, 20 + index, 0))
            self.assertTrue(self.client.sent[0]["status"]["waitingForRewards"],
                            "the scene is never told the win is uncollected")

            self.client.sent.clear()
            asyncio.run(tutorial.handle_tutorial_claim({}, 30 + index, 0))
            self.assertIn("LeagueAndGymModeStatus", self.client.names())
            self.assertNotIn("HasAvailableTutorialMatches", self.client.names(),
                             "the claim must not push the scene past the booster step")
            refreshed = next(packet for packet in self.client.sent
                             if packet.get("messageName") == "LeagueAndGymModeStatus")
            self.assertFalse(refreshed["status"]["waitingForRewards"])

        self.assertTrue(tutorial_data.completed(ACCOUNT))
        self.assertTrue(content.matches()[-1].packs)
        self.assertTrue(_collection(ACCOUNT), "nothing landed in the collection")
        self.assertEqual(tutorial_data.status_rows(ACCOUNT), [])

        self.client.sent.clear()
        asyncio.run(tutorial.handle_tutorial_play({"index": 0}, 40, 0))
        # the request is completed, then the scene is told there is nothing left
        self.assertEqual(self.client.names(), [None, "HasAvailableTutorialMatches"])
        self.assertFalse(self.client.sent[-1]["hasAvailableMatches"])

    def test_claim_pays_the_pending_reward_and_refreshes_the_wallet(self):
        tutorial_data.record_result(ACCOUNT, content.matches()[0].key, won=True)
        handler = TutorialHandler(self.client)
        asyncio.run(handler.handle_tutorial_claim({}, 7, 0))
        self.assertIn("CurrentWallet", self.client.names())
        self.assertFalse(tutorial_data.rewards_pending(ACCOUNT))


class _ScoredSession(GameSession):
    """Real session, no choreography pacing."""

    def __init__(self, game_id, pairing):
        super().__init__(game_id, pairing)
        self.choreography_pauses = False


class TutorialMatchTest(unittest.TestCase):
    """One real match: the finished tutorial game is scored through the session."""

    def setUp(self):
        tutorial_data.reset(ACCOUNT)

    def tearDown(self):
        tutorial_data.reset(ACCOUNT)

    def test_a_played_match_records_its_result(self):
        match = content.matches()[0]
        session = _ScoredSession(str(uuid.uuid4()), {
            "is_solo": True,
            "solitaire_id": match.key,
            "solo_context": {"account_id": ACCOUNT, "tutorial": match.key},
            "players": {
                ACCOUNT: {"client": None, "deck": content.opponent_deck(match)},
                RIVAL: {"client": None, "deck": content.starter_deck()},
            },
        })

        async def play():
            await asyncio.wait_for(session.run_gameplay_sequence(), timeout=180)

        asyncio.run(play())

        self.assertEqual(session.game_phase, GamePhase.GAME_OVER)
        progress = tutorial_data.load(ACCOUNT)
        self.assertIn(match.key, progress, "the finished tutorial match was not scored")
        self.assertEqual(progress[match.key]["wins"] + progress[match.key]["losses"], 1)


if __name__ == "__main__":
    unittest.main()
