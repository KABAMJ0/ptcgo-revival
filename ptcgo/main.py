import time
import logging
import logging.handlers
import queue
import os
import json
import asyncio

from ptcgo import config


def _configure_logging():
    """Off-thread, non-blocking logging: a QueueHandler feeds a QueueListener so hot
    paths never block on a slow stderr (Windows console especially). Level is
    PTCGO_LOG_LEVEL-overridable."""
    log_queue = queue.Queue(-1)
    fmt = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    stream = logging.StreamHandler()
    stream.setFormatter(fmt)
    listener = logging.handlers.QueueListener(log_queue, stream, respect_handler_level=True)
    listener.start()
    root = logging.getLogger()
    root.handlers.clear()
    root.addHandler(logging.handlers.QueueHandler(log_queue))
    root.setLevel(getattr(logging, config.LOG_LEVEL, logging.INFO))
    return listener


_LOG_LISTENER = _configure_logging()

# Imports below are intentionally after logging setup so import-time logs use the
# queue handler (E402 is expected here).
from ptcgo.server.server import PTCGOServer  # noqa: E402
from ptcgo.server.http_server import (  # noqa: E402
    BUNDLE_CACHE_DIR, AssetHTTPServer, manifest_manager, prepare_virtual_bundles)
from ptcgo.server.bundle_variants import strip_stale_bundles  # noqa: E402
from ptcgo.server.auto_bundle import check_and_generate_bundles  # noqa: E402
from ptcgo.server import metrics  # noqa: E402
from ptcgo.server import telemetry  # noqa: E402
from ptcgo.database import Base, engine  # noqa: E402
from ptcgo.database.migrations import run_light_migrations  # noqa: E402
from ptcgo.database.admin_data import bootstrap_admins_from_env  # noqa: E402
from ptcgo.game.tournaments.manager import TournamentManager
from ptcgo.game.progression.quests import load_catalog

async def run_server():
    tcp_server = PTCGOServer()

    # Sample event-loop lag continuously (tracked task, cancelled on shutdown).
    lag_task = asyncio.ensure_future(metrics.sample_loop_lag(1.0))

    # We want to catch asyncio.CancelledError to stop server gracefully
    try:
        await tcp_server.start()
    except asyncio.CancelledError:
        pass
    finally:
        lag_task.cancel()
        await tcp_server.stop()

def _mark_oldtimer_accounts_out_of_the_tutorial():
    """Accounts that predate the scripted tutorial are done with it already."""
    from ptcgo.database import tutorial_data
    try:
        tutorial_data.backfill_completed()
    except Exception as e:
        logging.error(f"[Main] Tutorial backfill failed: {e}")


def main():
    telemetry.install_log_capture()
    logging.info(f"[Main] Public host: {config.PUBLIC_HOST} (HTTP {config.HTTP_PORT}, TCP {config.TCP_PORT})")
    if config.PUBLIC_HOST == "127.0.0.1":
        logging.warning("[Main] PUBLIC_HOST is 127.0.0.1 — remote clients will fail to log in. "
                        "Set it in spirit/config.py or via PTCGO_PUBLIC_HOST.")

    # 0. Ensure all database tables exist (idempotent)
    Base.metadata.create_all(engine)
    run_light_migrations()
    bootstrap_admins_from_env()
    # Shop rows we ship (a product without a row never reaches the shop)
    from ptcgo.database.shop_defaults import ensure_default_shop_items
    ensure_default_shop_items()
    _mark_oldtimer_accounts_out_of_the_tutorial()
    # Prime the tournament cache off-loop (handlers only read it afterwards)
    TournamentManager()
    load_catalog()

    # 1. Ensure asset_map.json exists for first-time setup
    map_path = "ptcgo/server/asset_map.json"
    if not os.path.exists(map_path):
        logging.info("ERROR: [Main] asset_map.json not found.")
        return

    # 2. Run the auto bundle generation
    # The scan opens every bundle to see whether any card art is newer than the
    # built bundle: two to four minutes on a 2,000-bundle cache. A deploy that
    # only changed code sets PTCGO_SKIP_BUNDLE_SCAN=1 and skips it; a deploy that
    # ships art leaves it unset and pays for the rebuild.
    if os.environ.get("PTCGO_SKIP_BUNDLE_SCAN") == "1":
        logging.info("[AutoBundle] Skipping the bundle scan (PTCGO_SKIP_BUNDLE_SCAN=1)")
    else:
        check_and_generate_bundles()
        strip_stale_bundles(BUNDLE_CACHE_DIR)
    
    logging.info("[Main] Refreshing manifest manager...")
    # Reload asset map and refresh manifest to capture all compiled cards and cosmetics
    map_path = "ptcgo/server/asset_map.json"
    try:
        with open(map_path, "r") as f:
            manifest_manager.asset_map = json.load(f)
    except Exception as e:
        logging.error(f"[Main] Failed to reload asset_map.json: {e}")
    manifest_manager.refresh()
    prepare_virtual_bundles()

    http_server = AssetHTTPServer()
    http_server.start()

    # The admin panel moves to its own listener when PTCGO_ADMIN_PORT differs, so a
    # tunnel pointed at the asset port can never reach it. Unset, this block is a no-op
    # and /admin stays on the asset listener.
    admin_server = None
    if config.ADMIN_ON_SEPARATE_PORT:
        admin_server = AssetHTTPServer(port=config.ADMIN_PORT, admin_only=True)
        admin_server.start()

    try:
        asyncio.run(run_server())
    except KeyboardInterrupt:
        print("\nShutting down gracefully...")
        http_server.stop()
        if admin_server is not None:
            admin_server.stop()

if __name__ == '__main__':
    main()
