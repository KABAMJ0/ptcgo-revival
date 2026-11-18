"""Tutorial entry points.

The client has StartTutorial, StartTutorialPostLogin and SetTutorialPack in its
own protocol. Nothing here implements a tutorial, so these were unanswered: an
opening tab that waits on a request never draws, which looks like "loads and does
nothing".

Answering them with an empty packet completes the request so the client moves on
instead of waiting. That is deliberately an absence of tutorial, not a fake one:
a wrong payload would drop the client into a scripted flow the server cannot
follow, and the failure would look like a crash rather than a missing feature.
"""

import logging

from .base import BaseHandler, handle


class TutorialHandler(BaseHandler):
    @handle("StartTutorial")
    async def handle_start_tutorial(self, message, request_id, flags):
        logging.info(f"[TCP] [{self.client.addr}] StartTutorial requested - no tutorial scripted, answering empty")
        await self.client.send_packet({}, request_id)

    @handle("StartTutorialPostLogin")
    async def handle_start_tutorial_post_login(self, message, request_id, flags):
        logging.info(f"[TCP] [{self.client.addr}] StartTutorialPostLogin requested - answering empty")
        await self.client.send_packet({}, request_id)

    @handle("SetTutorialPack")
    async def handle_set_tutorial_pack(self, message, request_id, flags):
        logging.info(f"[TCP] [{self.client.addr}] SetTutorialPack requested - answering empty")
        await self.client.send_packet({}, request_id)
