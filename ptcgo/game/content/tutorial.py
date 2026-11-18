"""The scripted tutorial funnel: two matches, their rewards, and what they pay.

The client walks a fixed funnel after a player first signs in
(`pie.code.pie.gameModules.trainerChallenge.FunnelState`):

    UNSET -> TutorialGame1Intro -> TutorialGame1 -> TutorialGame2Intro
          -> TutorialGame2 -> TrainingIntro -> Training -> OpenBooster -> OutOfFunnel

Every step above `Training` is client-side theatre driven by three things the
server owns: the state the scene loads (`LeagueAndGymMode*` with the `tutorial`
subMode), the match the Play button starts (`TutorialPlayGame {index}`), and the
rewards the scene pays out (`TutorialClaimRewards`). The two matches are the
client's own scripted Trainers — `Ella` first, then `Zach` (read out of the
Play coroutine in `pie-src.dll`) — so the roster here names them, and their
decks come from the same starter catalogue the Trainer Challenge fields.

A fresh account has to be able to *start* a tutorial game, which means the match
needs a deck the player owns even if they have never opened the deck builder.
`tutorial_deck()` picks one for them the way the client's own
`K.U::NuxQuickplayDeck` does, and the handler builds it from the starter
catalogue when the account owns no deck at all.
"""

from dataclasses import dataclass

from ptcgo.game.attributes import AttrID

# The client's currency id for Trainer Tokens, the same id `trainer_challenge`
# pays end-of-match rewards in.
TOKENS = AttrID.TRAINER_TOKENS.value

# Color id the client's quickplay deck picker looks for first ("Basic Green"):
# `K.U::NuxQuickplayDeck` returns the first owned deck whose first deck colour is
# 11 and falls back to a random owned deck, so fielding the player's own deck of
# that colour keeps the two ends describing the same deck.
GREEN_DECK_COLOR = 11


@dataclass(frozen=True)
class TutorialMatch:
    """One scripted tutorial game: who the player faces and what beating it pays."""

    key: str
    name: str
    deck: str      # STARTER_DECKS entry name (ptcgo/game/content/starter.py)
    coins: int
    packs: int

    @property
    def image(self):
        """Landing-page asset name: PvEOpponentRenderer loads `<name>_landingpage`."""
        return f"{self.name.casefold()}_landingpage"


MATCHES = (
    TutorialMatch("tutorial_game_1", "Ella", "Mew VMAX", 50, 0),
    TutorialMatch("tutorial_game_2", "Zach", "Lugia VSTAR", 50, 1),
)

# The account-level row in `tutorial_progress`; per-match rows use a match key.
COMPLETE_ROW = "complete"


def matches():
    """The tutorial's games, in play order."""
    return MATCHES


def match_at(index):
    """The game at a 0-based index, or None for an index the funnel does not have."""
    if isinstance(index, bool) or not isinstance(index, int):
        return None
    if 0 <= index < len(MATCHES):
        return MATCHES[index]
    return None


def find(key):
    """The game with this key, or None."""
    return next((entry for entry in MATCHES if entry.key == key), None)


def reward_schedule():
    """`LeagueAndGymModeRewards.totalRewardSchedule` for the tutorial subMode.

    One entry per match panel, keyed 0..n-1 and contiguous from zero —
    `PvEModeRewardsData.UpdateRewards` copies `map[i]` for its own loop index and
    throws `KeyNotFoundException` on the first missing key.
    """
    return {
        str(index): [{"A": {"amount": {"name": TOKENS, "value": entry.coins}}}]
        for index, entry in enumerate(MATCHES)
    }


def status_rows(progress):
    """The panel's opponent list for the tutorial: Ella, then Zach.

    `progress` is `tutorial_data.load()`: a match is `Completed` once beaten and
    `Available` until then, which is what draws the checkmark on its panel.
    """
    rows = []
    for entry in MATCHES:
        beaten = int((progress.get(entry.key) or {}).get("wins") or 0) > 0
        rows.append({"key": entry.key, "name": entry.name, "image": entry.image,
                     "status": "Completed" if beaten else "Available"})
    return rows


def opponent_deck(entry):
    """A client-shaped 60-card deck for this scripted Trainer, built once each."""
    cached = _DECKS.get(entry.key)
    if cached is None:
        from ptcgo.game.content.starter import STARTER_DECKS, build_deck_data
        decklists = dict(STARTER_DECKS)
        cached = build_deck_data(f"{entry.name}'s {entry.deck}", decklists[entry.deck])
        _DECKS[entry.key] = cached
    return cached


def starter_deck():
    """A client-shaped deck for a player who owns none: the first starter decklist."""
    from ptcgo.game.content.starter import STARTER_DECKS, build_deck_data
    name, decklist = STARTER_DECKS[0]
    return build_deck_data(f"Tutorial {name}", decklist)


_DECKS = {}
