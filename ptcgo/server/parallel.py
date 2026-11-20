"""Thread-pool helpers for the bundle builder."""
import logging
import os
from concurrent.futures import ThreadPoolExecutor

def worker_count() -> int:
    """Parallel build workers: PTCGO_BUNDLE_WORKERS, default 2 (each build holds a few
    hundred MB, so raise it only on machines with spare RAM)."""
    try:
        return max(1, int(os.environ.get("PTCGO_BUNDLE_WORKERS", "2")))
    except ValueError:
        return 2


def run_parallel(jobs, workers=None):
    """Run zero-argument callables on a thread pool and return their results in order.
    The heavy work is subprocesses and PIL calls, which release the GIL. A failing job
    is logged and yields None instead of aborting the batch."""
    workers = workers or worker_count()

    def guarded(job):
        try:
            return job()
        except Exception as e:
            logging.error(f"[AutoBundle] Job failed: {e}")
            return None

    if workers <= 1 or len(jobs) <= 1:
        return [guarded(j) for j in jobs]
    with ThreadPoolExecutor(max_workers=workers) as pool:
        return list(pool.map(guarded, jobs))
