"""Offline deterministic tests for the read-only HIVE desk."""
import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from desk_health import snapshot, handler

NOW = datetime(2026, 11, 22, 14, 0, tzinfo=timezone.utc)


class DeskHealthTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "desk").mkdir()
        (self.root / "messages").mkdir()

    def state(self, as_of):
        (self.root / "desk" / "STATE.json").write_text(json.dumps(
            {"as_of": as_of, "sensitive_field": "do_not_expose"}))

    def message(self, fname, **kw):
        d = dict(id=fname, timestamp_utc="2026-11-22T13:55:00Z",
                 **{"from": "argus"}, to=["muse"], subject="Research",
                 requires_response=True, status="open")
        d.update(kw)
        (self.root / "messages" / fname).write_text(json.dumps(d))

    def scan(self):
        return snapshot(self.root, now=NOW)

    def test_stale_state_and_no_muse_are_explicit(self):
        self.state("2026-09-11T04:50:00Z")
        self.message("argus.json")
        s = self.scan()
        self.assertEqual(s["state"]["status"], "STALE")
        self.assertIn("STATE_STALE", s["warnings"])
        self.assertIn("MUSE_NOT_VERIFIED", s["warnings"])
        self.assertFalse(s["agent_runtime_verified"])

    def test_open_queue_and_actor_evidence(self):
        self.state("2026-11-22T13:50:00Z")
        self.message("argus.json")
        self.message("muse.json", **{"from": "muse", "to": ["chatgpt"],
                                     "subject": "Please review"})
        self.message("done.json", status="closed")
        s = self.scan()
        self.assertEqual(s["messages"]["pending_count"], 2)
        muse = next(a for a in s["agents"] if a["role"] == "muse")
        self.assertEqual(muse["status"], "RECENT_POST_ONLY")
        self.assertNotIn("MUSE_NOT_VERIFIED", s["warnings"])
        self.assertEqual(s["state"]["status"], "RECENT_SNAPSHOT")

    def test_invalid_and_future_messages_are_not_trusted(self):
        (self.root / "messages" / "bad.json").write_text("not json")
        self.message("future.json", timestamp_utc="2026-11-23T01:00:00Z")
        s = self.scan()
        self.assertEqual(s["messages"]["valid_count"], 0)
        self.assertEqual(s["messages"]["invalid_count"], 1)
        self.assertIn("FUTURE_MESSAGE", s["warnings"])

    def test_body_and_sensitive_state_are_never_exposed(self):
        self.state("2026-11-22T13:50:00Z")
        self.message("private.json", body_md="SECRET_API_KEY_DO_NOT_LEAK")
        encoded = json.dumps(self.scan())
        self.assertNotIn("SECRET_API_KEY_DO_NOT_LEAK", encoded)
        self.assertNotIn("do_not_expose", encoded)

    def test_no_messages_directory(self):
        (self.root / "messages").rmdir()
        self.assertIn("MESSAGES_MISSING", self.scan()["warnings"])

    def test_re_reads_after_changes(self):
        self.assertEqual(self.scan()["messages"]["valid_count"], 0)
        self.message("one.json")
        self.assertEqual(self.scan()["messages"]["valid_count"], 1)

    def test_bad_clock_rejected(self):
        with self.assertRaises(ValueError):
            snapshot(self.root, now=datetime(2026, 11, 22))

    def test_local_http_handler_is_class(self):
        from http.server import BaseHTTPRequestHandler
        self.assertTrue(issubclass(handler(self.root, 24), BaseHTTPRequestHandler))


if __name__ == "__main__":
    unittest.main()
