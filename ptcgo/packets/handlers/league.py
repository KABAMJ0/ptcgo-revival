"""League and Gym mode, and the deck-share toggle.

The client's Trainer Challenge / tutorial tab asks for league status and league
rewards on entry. Nothing implemented leagues, so both requests went unanswered
and the screen span forever with no error.

These handlers answer with the real shapes, read out of the client's own
metadata (JsonFx maps the [JsonName] attributes, so the keys are lower case even
though the CLR members are PascalCase). The status object has exactly four
members and no league list at all: an empty `opponents` array *is* the "no
leagues available" state, so the screen renders instead of hanging.
"""

import logging

from .base import BaseHandler, handle


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
