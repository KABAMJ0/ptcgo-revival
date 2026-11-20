"""Safe read-modify-write of asset_map.json when several bundle builders run at once."""
import json
import os
import tempfile

try:
    import fcntl
except ImportError:  # non-POSIX: no inter-process lock available
    fcntl = None


def update_entry(path, key, value) -> bool:
    """Set path[key] = value under an exclusive lock and swap the file in atomically,
    so concurrent builders neither lose each other's entries nor leave a torn file.
    Returns False when the map file does not exist."""
    if not os.path.exists(path):
        return False
    with open(path + ".lock", "a+") as lock:
        if fcntl is not None:
            fcntl.flock(lock, fcntl.LOCK_EX)
        try:
            with open(path, "r") as f:
                data = json.load(f)
            data[key] = value
            fd, tmp = tempfile.mkstemp(dir=os.path.dirname(os.path.abspath(path)), suffix=".tmp")
            try:
                with os.fdopen(fd, "w") as f:
                    json.dump(data, f)
                os.replace(tmp, path)
            except BaseException:
                if os.path.exists(tmp):
                    os.remove(tmp)
                raise
        finally:
            if fcntl is not None:
                fcntl.flock(lock, fcntl.LOCK_UN)
    return True
