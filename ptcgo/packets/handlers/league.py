"""League and Gym mode, and the Trainer Challenge Play button.

The client asks for league status and rewards when the tab opens, then
`LeagueAndGymModePlayGame` (or `TutorialPlayGame` / `GymModeStart`) when the
player presses Play. Status and rewards are the two shapes the client's own
metadata declares (`notes/league-dto.md`): four status members with an opponent
list, and a reward schedule keyed by league id.

Opponents come from `ptcgo/game/content/trainer_challenge.py` and their
availability from the account's progress, so the panel lists named Trainers in
unlock order. Play fields that opponent's own deck through the solo-match
machinery, and the finished match records the result, pays the reward and
unlocks the next Trainer (see `GameSession.end_game`).
"""

import logging

from ptcgo.database import trainer_challenge_data
from ptcgo.network.message_names import OutboundMsg
from ptcgo.game.content import trainer_challenge as content
from ptcgo.game.decks.theme_decks import theme_decks
from ptcgo.game.session.manager import GameSessionManager

from .base import BaseHandler, handle

# Plain text, not keys: the client ships no `league.error.*` string, so its
# LocalizableText lookup would miss and draw the key itself on the panel.
NO_DECK_TEXT = "You need a deck of exactly 60 cards to play here."
UNAVAILABLE_TEXT = "That opponent is not available yet."

# Keys the client may use to name the opponent it selected. The request payload
# is not in the decoded protocol notes, so every plausible spelling of the same
# field is read, plus an index into the status list; an unnamed request falls
# back to the first opponent the player can actually play.
_OPPONENT_KEYS = ("opponentName", "opponent", "opponentKey", "opponentID", "name")


def _player_deck(client):
    """The first deck of the player's that has a full 60 cards."""
    for deck in getattr(client.player, "decks", []) or []:
        data = deck.get("deck_data") or {}
        pile = (data.get("piles") or {}).get("deck") or []
        if len(pile) == 60:
            return data
    return None


# The client names its chosen Trainer in the *matchmaking* request, not in a
# league message: `InitiateTCGameOnSelect.playGame` sends `RequestQueueMatch`
# with queueName "TrainerChallenge" and one clientOptions entry carrying the
# selected scenario id. Both spellings of that key are read.
_CHALLENGE_QUEUE_MARKERS = ("trainerchallenge", "trainer challenge")
_CHALLENGE_OPTION_KEYS = ("scenarios", "scenario", "scenarioID", "scenarioId")


def is_challenge_queue(queue_name, client_options):
    """Whether a matchmaking request is the Trainer Challenge's Play button."""
    name = str(queue_name or "").strip().casefold()
    if any(marker in name for marker in _CHALLENGE_QUEUE_MARKERS):
        return True
    return any(key in (client_options or {}) for key in _CHALLENGE_OPTION_KEYS)


def option_values(client_options):
    """Every string a clientOptions map carries, in order."""
    values = []
    for key, value in (client_options or {}).items():
        if str(key) in _CHALLENGE_OPTION_KEYS or "scenario" in str(key).casefold():
            values.append(value)
    return [str(value) for value in values if value is not None]


def request_values(request):
    """Every string a league Play request carries under a known opponent key."""
    if not isinstance(request, dict):
        return []
    payload = request.get("request") if isinstance(request.get("request"), dict) else request
    values = []
    for key in _OPPONENT_KEYS + _CHALLENGE_OPTION_KEYS:
        value = payload.get(key)
        if isinstance(value, dict):
            value = value.get("id") or value.get("key")
        if isinstance(value, (str, int)) and str(value).strip():
            values.append(str(value))
    index = payload.get("opponentIndex", payload.get("index"))
    if isinstance(index, int):
        values.append(str(index))
    return values


def player_deck_images(client):
    """Theme-deck keys for the player's decks — the names the TC deck panel renders."""
    images = []
    for deck in getattr(client.player, "decks", []) or []:
        pile = ((deck.get("deck_data") or {}).get("piles") or {}).get("deck") or []
        product = theme_decks.match_deck(pile) if pile else None
        if product is not None and product.key not in images:
            images.append(product.key)
    return images


class LeagueHandler(BaseHandler):
    @handle("LeagueAndGymModeGetStatus")
    async def handle_league_status(self, request, request_id, flags):
        """League status: the opponent list, this player's decks, losses, payouts."""
        account_id = self.client.player.account_id
        opponents = [
            {"name": {"id": row["name"]}, "image": row["image"], "status": row["status"]}
            for row in trainer_challenge_data.status_rows(account_id)
        ]
        losses = trainer_challenge_data.losses(account_id)
        logging.info(f"[TCP] [{self.client.addr}] League status: {len(opponents)} opponents, "
                     f"{losses} losses")
        await self.client.send_packet({
            "messageName": "LeagueAndGymModeStatus",
            "status": {
                "opponents": opponents,
                "playerData": {"playerDeckImages": player_deck_images(self.client)},
                # Payouts are paid the moment the result is recorded, so nothing
                # is ever left waiting for the client to collect.
                "waitingForRewards": False,
                "losses": losses,
            },
        }, request_id)

    @handle("LeagueAndGymModeGetRewards")
    async def handle_league_rewards(self, request, request_id, flags):
        """The reward schedule: one entry per league, paid by clearing it."""
        schedule = content.reward_schedule()
        logging.info(f"[TCP] [{self.client.addr}] League rewards: {len(schedule)} leagues")
        await self.client.send_packet({
            "messageName": "LeagueAndGymModeRewards",
            "totalRewardSchedule": schedule,
        }, request_id)

    @handle("LeagueAndGymModeReset")
    async def handle_league_reset(self, request, request_id, flags):
        """Clears one league's progress (or every league when none is named)."""
        payload = request if isinstance(request, dict) else {}
        league_key = payload.get("leagueName") or payload.get("league") or payload.get("leagueKey")
        if not isinstance(league_key, str) or content.league(league_key.strip().lower()) is None:
            league_key = None
        trainer_challenge_data.reset(self.client.player.account_id, league_key)
        await self.client.send_packet({}, request_id)

    @handle("SetDeckShareMode")
    async def handle_set_deck_share_mode(self, request, request_id, flags):
        # Cosmetic preference; acknowledged so the client does not wait on it.
        await self.client.send_packet({}, request_id)


class ChallengePlayHandler(BaseHandler):
    """Play pressed on a league, gym or tutorial panel: start a real solo game."""

    @staticmethod
    def is_challenge_request(queue_name, client_options):
        """Whether a matchmaking request came from the Trainer Challenge."""
        return is_challenge_queue(queue_name, client_options)

    async def _start(self, values, request_id, label, deck=None):
        account_id = self.client.player.account_id
        opponent = trainer_challenge_data.pick_opponent(account_id, values)
        if opponent is None:
            logging.info(f"[TCP] [{self.client.addr}] {label}: no league opponent is available")
            await self.client.send_packet({
                "messageName": "LeagueAndGymModeError",
                "msg": {"id": UNAVAILABLE_TEXT},
            }, request_id)
            return
        if not trainer_challenge_data.available(
                opponent.key, trainer_challenge_data.load(account_id)):
            logging.info(f"[TCP] [{self.client.addr}] {label}: {opponent.name} is not available")
            await self.client.send_packet({
                "messageName": "LeagueAndGymModeError",
                "msg": {"id": UNAVAILABLE_TEXT},
            }, request_id)
            return
        deck = deck or _player_deck(self.client)
        if deck is None:
            logging.info(f"[TCP] [{self.client.addr}] {label}: player has no complete deck")
            await self.client.send_packet({
                "messageName": "LeagueAndGymModeError",
                "msg": {"id": NO_DECK_TEXT},
            }, request_id)
            return
        logging.info(f"[TCP] [{self.client.addr}] {label}: starting a match vs "
                     f"{opponent.name} ({opponent.difficulty}, {opponent.deck})")
        await GameSessionManager().start_solo_match(
            self.client, deck, opponent.key, {},
            request_id=request_id,
            opponent_deck=content.opponent_deck(opponent),
            solo_context={"account_id": account_id, "opponent": opponent.key},
        )

    async def start_from_queue(self, queue_name, client_options, deck=None):
        """The Trainer Challenge Play button.

        `InitiateTCGameOnSelect.playGame` sends `RequestQueueMatch` with the
        Trainer Challenge queue name and the chosen Trainer in clientOptions;
        there is no league-specific play message on the wire. The client is put
        into the matchmaking state first (MatchQueueEntered), exactly as a
        versus queue entry does, before the match is confirmed.
        """
        await self.client.send_packet({
            "messageName": OutboundMsg.MATCH_QUEUE_ENTERED.value,
            "estimatedWaitTime": 0,
        }, 0)
        await self._start(option_values(client_options), 0,
                          f"queue '{queue_name}'", deck)

    @handle("LeagueAndGymModePlayGame")
    async def handle_league_play(self, request, request_id, flags):
        await self._start(request_values(request), request_id, "LeagueAndGymModePlayGame")

    @handle("GymModeStart")
    async def handle_gym_start(self, request, request_id, flags):
        await self._start(request_values(request), request_id, "GymModeStart")

    @handle("TutorialPlayGame")
    async def handle_tutorial_play(self, request, request_id, flags):
        """The tutorial's own Play button: a practice match, not a league opponent.

        The tutorial flow itself is not scripted (see handlers/tutorial.py), so the
        player's deck gets the generic practice opponent rather than a Trainer.
        """
        deck = _player_deck(self.client)
        if deck is None:
            await self.client.send_packet({
                "messageName": "LeagueAndGymModeError",
                "msg": {"id": NO_DECK_TEXT},
            }, request_id)
            return
        logging.info(f"[TCP] [{self.client.addr}] TutorialPlayGame: starting a practice match")
        await GameSessionManager().start_solo_match(
            self.client, deck, "tutorial_bot", {}, request_id=request_id)
