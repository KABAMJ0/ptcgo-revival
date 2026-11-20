"""Parallel bundle building: the asset map survives concurrent writers and the pool helper
keeps results ordered and isolates failures."""
import json
import multiprocessing
import os
import tempfile
import time
import unittest

from ptcgo.server import asset_map


def _writer(path, start, count):
    for i in range(start, start + count):
        asset_map.update_entry(path, f"bundle_{i}", [str(i)])


class AssetMapLockTest(unittest.TestCase):
    def test_concurrent_writers_lose_nothing(self):
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "asset_map.json")
            with open(path, "w") as f:
                json.dump({"existing": ["001"]}, f)
            procs = [multiprocessing.Process(target=_writer, args=(path, n * 50, 50)) for n in range(4)]
            for p in procs:
                p.start()
            for p in procs:
                p.join(60)
                self.assertEqual(p.exitcode, 0)
            with open(path) as f:
                data = json.load(f)
            self.assertEqual(len(data), 201)
            self.assertEqual(data["existing"], ["001"])
            self.assertEqual(data["bundle_199"], ["199"])
            self.assertFalse([n for n in os.listdir(d) if n.endswith(".tmp")])

    def test_missing_map_is_a_noop(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertFalse(asset_map.update_entry(os.path.join(d, "nope.json"), "k", []))


class RunParallelTest(unittest.TestCase):
    def setUp(self):
        from ptcgo.server import parallel
        self.ab = parallel

    def test_results_keep_order(self):
        jobs = [lambda i=i: (time.sleep(0.02 * (5 - i)), i)[1] for i in range(5)]
        self.assertEqual(self.ab.run_parallel(jobs, workers=3), [0, 1, 2, 3, 4])

    def test_failure_is_isolated(self):
        def boom():
            raise RuntimeError("x")
        with self.assertLogs(level="ERROR"):
            self.assertEqual(self.ab.run_parallel([lambda: 1, boom, lambda: 3], workers=2), [1, None, 3])

    def test_jobs_overlap(self):
        jobs = [lambda: time.sleep(0.3) or 1 for _ in range(4)]
        start = time.time()
        self.ab.run_parallel(jobs, workers=4)
        self.assertLess(time.time() - start, 0.9)

    def test_single_worker_is_sequential(self):
        order = []
        jobs = [lambda i=i: order.append(i) for i in range(3)]
        self.ab.run_parallel(jobs, workers=1)
        self.assertEqual(order, [0, 1, 2])

    def test_worker_env_parsing(self):
        for value, expected in (("4", 4), ("0", 1), ("junk", 2)):
            os.environ["PTCGO_BUNDLE_WORKERS"] = value
            self.assertEqual(self.ab.worker_count(), expected)
        del os.environ["PTCGO_BUNDLE_WORKERS"]
        self.assertEqual(self.ab.worker_count(), 2)


if __name__ == "__main__":
    unittest.main()
