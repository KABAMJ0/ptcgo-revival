"""League and Gym mode, and the deck-share toggle.

The client's Trainer Challenge / tutorial tab asks for league status and league
rewards on entry. Nothing in this server implements leagues, so both requests
went unanswered and the screen span forever with no error: the log showed
"No handler registered for message: LeagueAndGymModeGetStatus".

These handlers answer the request so the RPC completes and the tab stops
loading. The payloads are deliberately empty: there is no league state to
report, and inventing one would put the client into a flow the server cannot
follow. `SetDeckShareMode` is likewise acknowledged and ignored.
"""

import logging

from .base import BaseHandler, handle


class LeagueHandler(BaseHandler):
    @handle("LeagueAndGymModeGetStatus")
    async def handle_league_status(self, message, request_id, flags):
        logging.info(f"[TCP] [{self.client.addr}] League status requested - answering empty")
        # An empty packet completes the RPC; a shaped payload would imply leagues exist.
        await self.client.send_packet({}, request_id)

    @handle("LeagueAndGymModeGetRewards")
    async def handle_league_rewards(self, message, request_id, flags):
        logging.info(f"[TCP] [{self.client.addr}] League rewards requested - answering empty")
        await self.client.send_packet({}, request_id)

    @handle("SetDeckShareMode")
    async def handle_set_deck_share_mode(self, message, request_id, flags):
        # Cosmetic preference; acknowledged so the client does not wait on it.
        await self.client.send_packet({}, request_id)
