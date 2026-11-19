"""PTCGO_ADMIN_PORT: the admin panel on its own listener, and 404 on the asset port.

The admin *handler* needs a booted server (it reads the DB for the shop panel and does
not answer on a bare `AssetHTTPServer` in-process), so the "admin answers on its own
port" direction is asserted on the routing decision, and the isolation directions are
asserted over real HTTP.
"""
import unittest
import urllib.error
import urllib.request
from unittest import mock

import ptcgo.config as config
from ptcgo.server import http_server


def _get(port, path):
    url = f"http://127.0.0.1:{port}{path}"
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            return response.status
    except urllib.error.HTTPError as exc:
        return exc.code


class Handler:
    """Minimal stand-in for the request handler's routing predicate."""

    _is_admin_path = staticmethod(http_server.MockHTTPRequestHandler._is_admin_path)
    _serves_admin = http_server.MockHTTPRequestHandler._serves_admin
    _off_mode = http_server.MockHTTPRequestHandler._off_mode

    def __init__(self, admin_only):
        self.server = type("S", (), {"admin_only": admin_only})()


class RoutingDecisionTests(unittest.TestCase):
    def test_separate_ports(self):
        with mock.patch.object(config, "ADMIN_ON_SEPARATE_PORT", True):
            asset, admin = Handler(False), Handler(True)
            # The asset listener refuses admin outright: it reaches the admin branch
            # and _serves_admin() turns it into a 404.
            self.assertFalse(asset._serves_admin())
            self.assertFalse(asset._off_mode("/admin"))
            self.assertFalse(asset._off_mode("/admin/api/session"))
            # ...and answers everything else.
            self.assertFalse(asset._off_mode("/motd.json"))
            self.assertFalse(asset._off_mode("/health"))
            # The admin listener is the mirror image.
            self.assertTrue(admin._serves_admin())
            self.assertFalse(admin._off_mode("/admin"))
            self.assertFalse(admin._off_mode("/admin/api/session"))
            self.assertTrue(admin._off_mode("/motd.json"))
            self.assertTrue(admin._off_mode("/health"))

    def test_unset_keeps_admin_on_the_asset_listener(self):
        with mock.patch.object(config, "ADMIN_ON_SEPARATE_PORT", False):
            asset = Handler(False)
            self.assertTrue(asset._serves_admin())
            self.assertFalse(asset._off_mode("/admin"))
            self.assertFalse(asset._off_mode("/motd.json"))


class LiveListenerTests(unittest.TestCase):
    def _start(self, admin_only):
        server = http_server.AssetHTTPServer(host="127.0.0.1", port=0,
                                            admin_only=admin_only)
        server.start()
        self.addCleanup(server.stop)
        return server.server.server_address[1]

    def test_asset_port_is_404_for_admin_and_serves_assets(self):
        with mock.patch.object(config, "ADMIN_ON_SEPARATE_PORT", True):
            port = self._start(admin_only=False)
            self.assertEqual(_get(port, "/admin"), 404)
            self.assertEqual(_get(port, "/admin/api/session"), 404)
            self.assertEqual(_get(port, "/motd.json"), 200)

    def test_admin_port_serves_no_assets(self):
        with mock.patch.object(config, "ADMIN_ON_SEPARATE_PORT", True):
            port = self._start(admin_only=True)
            self.assertEqual(_get(port, "/motd.json"), 404)
            self.assertEqual(_get(port, "/health"), 404)
            self.assertEqual(_get(port, "/placeholder.png"), 404)


class AdminPortConfigTests(unittest.TestCase):
    def test_admin_port_defaults_to_http_port(self):
        import importlib
        import os
        os.environ.pop("PTCGO_ADMIN_PORT", None)
        cfg = importlib.reload(config)
        self.assertEqual(cfg.ADMIN_PORT, cfg.HTTP_PORT)
        self.assertFalse(cfg.ADMIN_ON_SEPARATE_PORT)

    def test_admin_port_can_differ(self):
        import importlib
        import os
        os.environ["PTCGO_ADMIN_PORT"] = "8080"
        try:
            cfg = importlib.reload(config)
            self.assertEqual(cfg.ADMIN_PORT, 8080)
            self.assertTrue(cfg.ADMIN_ON_SEPARATE_PORT)
        finally:
            os.environ.pop("PTCGO_ADMIN_PORT", None)
            importlib.reload(config)


if __name__ == "__main__":
    unittest.main()
