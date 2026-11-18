"""League and Gym mode, and the trainer-challenge Play button.

The client asks for league status and rewards when the tab opens, then
`LeagueAndGymModePlayGame` (or `TutorialPlayGame` / `GymModeStart`) when the
player presses Play. Nothing implemented leagues here, so both stages went
unanswered and the screen hung.

Status and rewards are answered with the shapes the client's own metadata
declares: the status object has exactly four members and no league list, so an
empty `opponents` array is the correct "no leagues available" state.

Play is routed into the solo-match machinery this server already has
(`GameSessionManager.start_solo_match`), using the player's own deck. That gives
a real game against the built-in bot instead of a league opponent the panel
names but the server cannot field. If the player owns no complete deck the
client is told so with `LeagueAndGymModeError` rather than left waiting.
"""

import logging

from ptcgo.game.session.manager import GameSessionManager

from .base import BaseHandler, handle

NO_DECK_KEY = "league.error.nodeck"


def _player_deck(client):
    """The first deck of the player's that has a full 60 cards."""
    for deck in getattr(client.player, "decks", []) or []:
        data = deck.get("deck_data") or {}
        pile = (data.get("piles") or {}).get("deck") or []
        if len(pile) == 60:
            return data
    return None


class LeagueHandler(BaseHandler):
    @handle("LeagueAndGymModeGetStatus")
    async def handle_league_status(self, message, request_id, flags):
        logging.info(f"[TCP] [{self.client.addr}] League status requested - answering with an empty status")
        await self.client.send_packet({
            "messageName": "LeagueAndGymModeStatus",
            "status": {
                "opponents": [],
                "playerData": {"playerDeckImages": []},
                "waitingForRewards": False,
                "losses": 0,
            },
        }, request_id)

    @handle("LeagueAndGymModeGetRewards")
    async def handle_league_rewards(self, message, request_id, flags):
        logging.info(f"[TCP] [{self.client.addr}] League rewards requested - answering empty schedule")
        await self.client.send_packet({
            "messageName": "LeagueAndGymModeRewards",
            "totalRewardSchedule": {},
        }, request_id)

    @handle("SetDeckShareMode")
    async def handle_set_deck_share_mode(self, message, request_id, flags):
        # Cosmetic preference; acknowledged so the client does not wait on it.
        await self.client.send_packet({}, request_id)


class ChallengePlayHandler(BaseHandler):
    """Play pressed on a league, gym or tutorial panel: start a real solo game."""

    async def _start(self, message, request_id, label):
        deck = _player_deck(self.client)
        if deck is None:
            logging.info(f"[TCP] [{self.client.addr}] {label}: player has no complete deck")
            await self.client.send_packet({
                "messageName": "LeagueAndGymModeError",
                "msg": {"id": NO_DECK_KEY},
            }, request_id)
            return
        logging.info(f"[TCP] [{self.client.addr}] {label}: starting a solo match")
        await GameSessionManager().start_solo_match(
            self.client, deck, "tutorial_bot", {}, request_id)

    @handle("LeagueAndGymModePlayGame")
    async def handle_league_play(self, message, request_id, flags):
        await self._start(message, request_id, "LeagueAndGymModePlayGame")

    @handle("GymModeStart")
    async def handle_gym_start(self, message, request_id, flags):
        await self._start(message, request_id, "GymModeStart")

    @handle("TutorialPlayGame")
    async def handle_tutorial_play(self, message, request_id, flags):
        await self._start(message, request_id, "TutorialPlayGame")
