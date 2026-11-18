# PTCGO Revival

PTCGO Revival is a Python server emulator for the discontinued Pokémon Trading
Card Game Online (PTCGO) client. It runs the game server and serves the assets
that an existing copy of the client needs to connect.

The current checkout loads **19,643 cards across 172 sets**. About **57% of
Trainer scripts** are implemented in this checkout; the Trainer worker reported
about **67%** on its separate branch. About **58% of Pokémon attacks and
abilities with text** are scripted here. The dashboard counts attacks without
effect text too, so it shows about **68% of all entries** resolving without a
stub. A stubbed attack deals its printed base damage only; a stubbed Ability or
Trainer doesn't perform its printed effect.

## Quick start

On the Linux machine that will host the server:

```sh
git clone https://github.com/KABAMJ0/ptcgo-revival.git
cd ptcgo-revival
sudo ./install.sh --host play.example.com
```

Replace `play.example.com` with the public hostname or IP players will use.
[`install.sh`](install.sh) creates a Python 3.12 virtual environment with the
server dependencies, generates a self-signed TLS certificate for that host,
and initializes the local SQLite database if it doesn't already exist. It
downloads about 14 GB of card art, installs and starts the systemd service, and
opens the required ports in firewalld or UFW if available.

Allow **45–60 minutes on first start** for the server to pack the card bundles,
after the art download. Both server ports stay closed until that finishes, so
the dashboard won't answer during packing. Use the service journal to see
whether packing is moving.

## Requirements

| Requirement | What to provide |
| --- | --- |
| Server | Linux with systemd, 2 vCPUs, 4 GB RAM, and 80 GB of disk. |
| HTTP | TCP **8000** for the patch manifest, assets, and admin dashboard. |
| Game socket | TCP **39389** for the client's game connection. |
| Client | An existing copy of Pokémon TCG Online. The project was developed against client version 2.95.0.5815; other versions may not work. |

Open both TCP ports in the host firewall and any cloud security group. The
client dials **39389** itself: `cake.cfg` gives it a hostname, not an alternate
game port. An HTTP reverse proxy or a tunnel that assigns a random public port
can't carry that game connection. A proxy can still serve HTTP assets on
port 8000; see the [nginx deployment notes](deploy/README.md). Port 39389 must
remain reachable as TCP on the advertised host.

## Point players at the server

In the client installation, open
`Pokemon Trading Card Game Online_Data/cake.cfg`. Change these three lines
and leave the rest of the file alone:

```ini
hostname=play.example.com
versionURL=http://play.example.com:8000/
assetURL=http://play.example.com:8000/
```

Use the same hostname you passed to `--host`. The service sets
`PTCGO_PUBLIC_HOST` from that value so the server advertises it during login.
The client also checks the game socket's certificate against the hostname it
dialed. The installer generates that name into the certificate; don't add the
self-signed certificate to the client's OS trust store.

## Admin dashboard

Once packing finishes, open `http://play.example.com:8000/admin`. A fresh
SQLite database has a seeded administrator account; the installer prints its
default login. Keep the admin route private and replace or disable the default
login before exposing it. The default dashboard endpoint is plain HTTP.

| Tab | What it gives you |
| --- | --- |
| **Monitor** | Connected sessions, matchmaking queues and active matches; an activity feed, HTTP traffic, process health, and recent warnings and errors. Use it to see whether a problem is in the connection, the queue, or an active match. |
| **Coverage** | Per-set counts for loaded cards and implemented or stubbed attack and Ability entries. Counts are taken after wording-based effects are bound and distinguish them from hand-scripted effects and attacks that need no script. This is effect coverage, not a compatibility test. |

## Card art

The bulk card scans aren't stored in Git; a fresh clone has definitions but
doesn't have the scans needed to pack them. The installer runs
[`tools/fetch_art.py`](tools/fetch_art.py). To resume an interrupted download
or rebuild the art, run it from the repository root:

```sh
./venv/bin/python tools/fetch_art.py
```

The fetcher keeps existing images in `ptcgo/assets/cards/`. It tries the
Pokémon TCG API and the upstream repository before falling back to a card face
rendered from the card data. Pass set codes if you only want to fetch scans
for those sets.

Run [`tools/fetch_client_bundles.py`](tools/fetch_client_bundles.py) separately
to fetch the original Pokémon logo and landing-page carousel bundles from
upstream into `ptcgo/assets/bundleCache/`. Restart afterward so the server
picks them up in its manifest.

```sh
./venv/bin/python tools/fetch_client_bundles.py
```

## Everyday operation

The installer creates the system unit `spirit-ptcgo.service`. Run these on
the server:

| Task | Command |
| --- | --- |
| Check service status | `systemctl status spirit-ptcgo` |
| Follow startup and runtime logs | `sudo journalctl -u spirit-ptcgo -f` |
| Restart after an update or asset change | `sudo systemctl restart spirit-ptcgo` |
| Stop for maintenance | `sudo systemctl stop spirit-ptcgo` |
| Start after maintenance | `sudo systemctl start spirit-ptcgo` |

During packing, the journal works even while the admin dashboard is offline.
For a browser view, save the current boot's service log and follow it:

```sh
sudo journalctl -u spirit-ptcgo -b -n all -f > "$HOME/ptcgo-pack.log"
```

From the repository root in a second terminal, run:

```sh
./venv/bin/python tools/pack_feed.py "$HOME/ptcgo-pack.log"
```

Open `http://127.0.0.1:8999/` on the server for progress, a log tail, and an
indication of whether the ports are listening. [`tools/pack_feed.py`](tools/pack_feed.py)
binds to all interfaces and doesn't authenticate viewers. Keep port 8999
blocked from untrusted hosts, and stop the feed and log capture when done.

Back up these files from the repository root:

| Files | Why they matter |
| --- | --- |
| `ptcgo_server.db` | The default SQLite database holds player accounts, collections, decks, and trade data. Stop the service before copying the live database file, or use a SQLite-aware backup. If you configured an [external database](sql/README.md), back up that database instead. |
| `server.crt` and `server.key` | The certificate and private key are the game socket's TLS identity. Save them together so a restore can reuse that identity, and restrict access to the private key and its backups. |

Downloaded stock art and generated bundles can be rebuilt. Keep separate
copies of any artwork you made yourself.

## What works and what's missing

The engine runs matches and enforces the core rules: it resolves damage and
Knock Outs, awards Prizes, and handles evolution and retreat. That doesn't
mean every card plays as printed. Loaded card definitions make up the
catalogue; the per-card scripts and shared patterns determine which effects
actually run.

| Area | Known gaps |
| --- | --- |
| Engine and card effects | The card workers found effects that still need general rules for once-per-game GX attacks, revealing and manipulating face-up Prize cards, and replacing a Prism Star card's discard with a move to the Lost Zone. Having a Lost Zone does not implement that discard rule. |
| Client protocol | [`notes/client-gaps.md`](notes/client-gaps.md) lists unhandled requests such as observing a match, requesting a replay, and viewing trade history. A client screen can exist even when the server doesn't handle its request. |
| Headless verification | The Pokémon effects worker reported that the smoke harness couldn't place an assembled V-UNION on the board. A smoke pass should not be treated as proof of that client flow. |

## Upstream and licence

PTCGO Revival is a fork of
[Bratah123/Spirit-PTCGO](https://github.com/Bratah123/Spirit-PTCGO).
Credit for the original server goes to Bratah123 and the Spirit-PTCGO
contributors. The server code is licensed under GPL-3.0; see [`LICENSE`](LICENSE).

| What this fork adds | Where to look |
| --- | --- |
| A full card catalogue, separate from effect coverage | Card definitions in [`ptcgo/game/scripts/cards/`](ptcgo/game/scripts/cards/) and the set catalogue in [`sets.json`](ptcgo/database/json_data/sets.json). |
| Rebuildable art and catalogue tooling | Art fetchers, set importers, and client filter-label tools in [`tools/`](tools/). |
| An operator console | [`dashboard.html`](ptcgo/server/admin/dashboard.html) implements the Monitor and Coverage views. |
| A client protocol reference | [`notes/client-protocol.md`](notes/client-protocol.md) documents message shapes; [`notes/`](notes/) also holds the registry, enums, and compatibility notes. |

## Contributing

**Add a set.** Run [`tools/fetch_set.py`](tools/fetch_set.py) with the API set ID
and the repository set code. It writes the set's JSON under
`ptcgo/game/scripts/cards/`. Pass that file and `--set-code` to
[`ptcgo/tools/import_set.py`](ptcgo/tools/import_set.py) to generate card
definitions and download the art. Don't re-import a set casually: the
importer writes the card scripts, which can overwrite hand-written effects.
Review card IDs, collector numbers, and the generated diff.

Use [`tools/build_set_catalog.py`](tools/build_set_catalog.py) to refresh the
set metadata and generate missing booster definitions.
[`tools/tidy_series.py`](tools/tidy_series.py) normalizes the series names and
[`tools/build_labels.py`](tools/build_labels.py) generates missing client
filter labels. Review the catalogue changes alongside the card definitions.

**Wire card effects.** At load time, the Pokémon
[pattern table](ptcgo/game/card_effects/patterns.py) matches complete,
normalized wording and replaces an `unimplemented` marker with a shared
effect. Use the table for repeated text and the individual card script for
card-specific behavior; the table doesn't replace an explicit effect. For
Trainers, [`tools/trainer_patterns.py`](tools/trainer_patterns.py) describes
reusable shapes and [`tools/trainer_wire.py`](tools/trainer_wire.py) previews
matching changes with `--dry-run` before you apply them.

**Gate every change.** From the repository root with the dependencies
installed, require zero loader failures and run the headless smoke test for
every set touched by the change. Replace `SWSH8` with each affected set code:

```sh
./venv/bin/python -c '
from ptcgo.game.scripts.cards import loader
cards = loader.load_all()
print(f"{len(cards)} cards, {len(loader.last_errors)} failures")
raise SystemExit(bool(loader.last_errors))
'
./venv/bin/python -m ptcgo.tools.effect_smoke --set SWSH8
```

Require zero `FAIL` results. Inspect `UNIMPL` and `SKIP` separately; they
don't show that an affected effect ran.
