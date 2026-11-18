"""The scripted tutorial funnel: its matches, its rewards, and its claims.

The client walks a fixed funnel after a player first signs in (see
`ptcgo/game/content/tutorial.py` for the states). Three messages carry it:

* `LeagueAndGymModeGetStatus` / `LeagueAndGymModeGetRewards` with `subMode:
  "tutorial"` — the state the funnel scene loads. `NUXFullScreenView.Start` asks
  for both the moment the player is in the funnel to drive the intro, and the
  training scene asks again when it loads.
* `TutorialPlayGame {index}` — the Play button on a tutorial match panel. The
  client sends the panel's 0-based match index.
* `TutorialClaimRewards` — the reward handshake. `TutorialRewardsClaimer` sends
  it automatically as soon as the reward model reports a pending payout.

`StartTutorial`, `StartTutorialPostLogin` and `SetTutorialPack` are *not* client
messages: they are a behaviour method, a scene name and a local model setter in
`pie-src.dll`, and no string literal for any of them exists in this client. They
are answered here only so an older build that does send them is not left
waiting on a request that never completes.
"""

import logging

from ptcgo.database import tutorial_data
from ptcgo.game.content import tutorial as content
from ptcgo.game.session.manager import GameSessionManager
from ptcgo.network.message_names import OutboundMsg

from .base import BaseHandler, handle

TUTORIAL_SUB_MODE = "tutorial"


def sub_mode(request):
    """The `subMode` a league-mode request carries, lowercased, or ""."""
    if not isinstance(request, dict):
        return ""
    value = request.get("subMode") or request.get("submode")
    return str(value).strip().casefold() if value is not None else ""


def tutorial_status(account_id):
    """`LeagueAndGymModeStatus` for the tutorial: its two matches and their state."""
    return {
        "opponents": tutorial_data.status_rows(account_id),
        "playerData": {"playerDeckImages": []},
        "waitingForRewards": tutorial_data.rewards_pending(account_id),
        "losses": tutorial_data.losses(account_id),
    }


def tutorial_rewards():
    """`LeagueAndGymModeRewards` for the tutorial: one entry per match panel."""
    return content.reward_schedule()


async def start_tutorial_match(client, label, index=None, request_id=0):
    """Starts the scripted match the funnel is on.

    `index` is the panel the player pressed (0-based, from `TutorialPlayGame`);
    the intro's Play button sends `LeagueAndGymModePlayGame` with the tutorial
    subMode and no index, so a missing or out-of-range index plays the first
    match still unbeaten.
    """
    account_id = client.player.account_id
    match = None if tutorial_data.completed(account_id) else (
        content.match_at(index) or tutorial_data.next_match(account_id))
    if match is None:
        logging.info(f"[TCP] [{client.addr}] {label} {index!r}: "
                     f"the funnel has no match left to play")
        await client.send_packet({}, request_id)
        await announce_availability(client)
        return
    deck = await _tutorial_player_deck(client, account_id)
    if deck is None:
        logging.info(f"[TCP] [{client.addr}] {label}: no deck available")
        await client.send_packet({
            "messageName": "LeagueAndGymModeError",
            "msg": {"id": "league.error.nodeck"},
        }, request_id)
        return
    logging.info(f"[TCP] [{client.addr}] {label} {index!r}: starting "
                 f"{match.name} ({match.deck})")
    # Complete the RPC first and push the match as events, the way a versus queue
    # entry does. `TutorialPlayGame` never opens a matchmaking request on the
    # client, so its `handleConfirmReadyForMatch` throws on "An existing request
    # does not exist" and the scene would never leave the panel; `auto_ready`
    # confirms on the client's behalf so `MatchFound` follows.
    await client.send_packet({}, request_id)
    await GameSessionManager().start_solo_match(
        client, deck, match.key, {}, request_id=0,
        opponent_deck=content.opponent_deck(match),
        solo_context={"account_id": account_id, "tutorial": match.key},
        auto_ready=True,
    )


async def announce_availability(client):
    """Tells the scene there is no further scripted match.

    The client answers by moving the funnel to OpenBooster, which is right when
    the player asks for a match that does not exist, and wrong straight after the
    last win (it would skip `triggerOpenBoosterFunnel`).
    """
    complete = tutorial_data.completed(client.player.account_id)
    await client.send_packet({
        "messageName": OutboundMsg.HAS_AVAILABLE_TUTORIAL_MATCHES.value,
        "hasAvailableMatches": not complete,
    }, 0)


class TutorialHandler(BaseHandler):
    @handle("TutorialPlayGame")
    async def handle_tutorial_play(self, request, request_id, flags):
        """Play on a tutorial match panel: field that scripted Trainer."""
        index = request.get("index") if isinstance(request, dict) else None
        await start_tutorial_match(self.client, "TutorialPlayGame", index, request_id)

    @handle("TutorialClaimRewards")
    async def handle_tutorial_claim(self, request, request_id, flags):
        """Pays the pending first-win payout and refreshes what it changed."""
        account_id = self.client.player.account_id
        result = tutorial_data.claim(account_id)
        granted = result["granted"]
        logging.info(f"[TCP] [{self.client.addr}] TutorialClaimRewards: paid {granted}")
        if granted.get("products"):
            await self.push_collection()
        if granted.get("coins"):
            await self.push_wallet()
        await self.client.send_packet({}, request_id)
        # The scene reads pending rewards off the status, so refreshing it is what
        # stops it asking to claim again.
        #
        # `HasAvailableTutorialMatches` is deliberately *not* sent here: the
        # client's handler moves a player who is at the last match straight to
        # OpenBooster and skips `triggerOpenBoosterFunnel`, which is the step that
        # actually opens the pack. Left alone, the scene advances through
        # TrainingIntro and Training on its own, and that second step is what
        # starts the booster. The flag is answered only when Play is pressed with
        # no match left, where nothing else would move the scene along.
        await self.send({"messageName": "LeagueAndGymModeStatus",
                         "status": tutorial_status(account_id)})

    @handle("StartTutorial")
    async def handle_start_tutorial(self, request, request_id, flags):
        logging.info(f"[TCP] [{self.client.addr}] StartTutorial requested (not a client message here)")
        await self.client.send_packet({}, request_id)

    @handle("StartTutorialPostLogin")
    async def handle_start_tutorial_post_login(self, request, request_id, flags):
        logging.info(f"[TCP] [{self.client.addr}] StartTutorialPostLogin requested (not a client message here)")
        await self.client.send_packet({}, request_id)

    @handle("SetTutorialPack")
    async def handle_set_tutorial_pack(self, request, request_id, flags):
        logging.info(f"[TCP] [{self.client.addr}] SetTutorialPack requested (not a client message here)")
        await self.client.send_packet({}, request_id)


async def _tutorial_player_deck(client, account_id):
    """The deck the player fields in a tutorial match, granting one if they own none.

    A player who has never opened the deck builder has no deck of their own, and
    the tutorial is the one place that must not care: the client's own Play
    coroutine resolves the tutorial deck through `K.U::NuxQuickplayDeck`, which
    picks one of the *player's* decks, so the server hands them the first starter
    decklist and saves it as a real deck they keep.
    """
    for deck in getattr(client.player, "decks", []) or []:
        data = deck.get("deck_data") or {}
        if len((data.get("piles") or {}).get("deck") or []) == 60:
            return data
    return await _grant_starter_deck(client, account_id)


async def _grant_starter_deck(client, account_id):
    """Saves and grants the first starter decklist, returning the client-shaped deck."""
    from ptcgo.database import player_data
    from ptcgo.database.async_utils import run_db

    deck = content.starter_deck()
    if len(deck["piles"]["deck"]) != 60:
        logging.warning("[Tutorial] the starter decklist did not resolve to 60 cards")
        return None
    grants = {}
    for guid in deck["piles"]["deck"]:
        grants[guid] = grants.get(guid, 0) + 1
    await run_db(player_data.save_deck, account_id, deck["deckID"], "Tutorial Deck",
                 deck, False)
    await run_db(player_data.add_many_to_collection, account_id, grants, False)
    logging.info(f"[TCP] [{client.addr}] TutorialPlayGame: granted a starter deck to "
                 f"{account_id}, who owned none")
    client.player.decks = list(getattr(client.player, "decks", []) or []) + [
        {"id": deck["deckID"], "name": "Tutorial Deck", "deck_data": deck}]
    return deck
