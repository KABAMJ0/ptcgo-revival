"""PTCGO_HTTP_BASE_URL: the client-facing HTTP base when the server sits behind a tunnel."""
import importlib
import unittest
from unittest import mock

import ptcgo.config as config


def reload_with(**env):
    """Re-import ptcgo.config with a clean PTCGO_* environment."""
    base = {"PTCGO_PUBLIC_HOST": "127.0.0.1", "PTCGO_HTTP_PORT": "8000"}
    base.update(env)
    with mock.patch.dict("os.environ", base, clear=False):
        for key in ("PTCGO_HTTP_BASE_URL",):
            if key not in env:
                import os
                os.environ.pop(key, None)
        return importlib.reload(config)


class HttpBaseUrlTests(unittest.TestCase):
    def tearDown(self):
        import os
        os.environ.pop("PTCGO_HTTP_BASE_URL", None)
        importlib.reload(config)

    def test_unset_keeps_host_and_port(self):
        cfg = reload_with()
        self.assertEqual(cfg.HTTP_BASE_URL, "http://127.0.0.1:8000")
        self.assertEqual(cfg.PLACEHOLDER_IMG, "http://127.0.0.1:8000/placeholder.png")
        self.assertEqual(cfg.client_base_url("example.test:9000"),
                         "http://example.test:9000")

    def test_override_is_used_verbatim_without_a_port(self):
        cfg = reload_with(PTCGO_HTTP_BASE_URL="https://cards.example.com")
        self.assertEqual(cfg.HTTP_BASE_URL, "https://cards.example.com")
        self.assertEqual(cfg.PLACEHOLDER_IMG, "https://cards.example.com/placeholder.png")
        # The Host header no longer decides the base once a tunnel owns the hostname.
        self.assertEqual(cfg.client_base_url("127.0.0.1:8000"),
                         "https://cards.example.com")

    def test_trailing_slash_does_not_double(self):
        cfg = reload_with(PTCGO_HTTP_BASE_URL="https://cards.example.com/")
        self.assertEqual(cfg.HTTP_BASE_URL, "https://cards.example.com")
        self.assertEqual(f"{cfg.HTTP_BASE_URL}/manifest/version", "https://cards.example.com/manifest/version")
        self.assertNotIn("//", cfg.HTTP_BASE_URL.split("://", 1)[1])


if __name__ == "__main__":
    unittest.main()
