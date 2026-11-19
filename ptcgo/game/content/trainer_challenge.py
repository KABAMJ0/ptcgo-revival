"""Trainer Challenge content: the leagues, their opponents, and what beating them pays.

Opponent names are the client's own roster, read from its localization DB
(`com.direwolfdigital.cake.data.scenarios.trainers.<key>.name`), so the panel
shows the Trainers the shipped client was built around. Each opponent brings a
deck from the server's existing starter decklists: the theme-deck catalogue
holds a single approved product, and those decklists are the only complete
60-card decks the engine can field as a real opponent today.

Progression: the first opponent of a league is available once every earlier
league is complete, and every later opponent unlocks when all the opponents
before it in the same league have been beaten.
"""

from dataclasses import dataclass

from ptcgo.game.attributes import AttrID

# The client's currency id for Trainer Tokens, the same id the shop writes in
# its price maps (`ptcgo/shop`), i.e. the currency an end-of-game "Tokens"
# reward pays.
TOKENS = AttrID.TRAINER_TOKENS.value

EASY, MEDIUM, HARD = "Easy", "Medium", "Hard"


@dataclass(frozen=True)
class Opponent:
    """One Trainer: who they are, what they play, and the first-win payout."""

    key: str
    name: str
    deck: str      # STARTER_DECKS entry name (ptcgo/game/content/starter.py)
    difficulty: str
    coins: int

    @property
    def image(self):
        """Landing-page asset name: PvEOpponentRenderer loads `<key>_landingpage`."""
        return f"{self.key}_landingpage"


@dataclass(frozen=True)
class League:
    """A league: an ordered opponent list and the payout for clearing it."""

    key: str
    name: str
    opponents: tuple
    coins: int
    packs: int


LEAGUES = (
    League("gold", "Gold League", (
        Opponent("zach", "Zach", "Lugia VSTAR", EASY, 100),
        Opponent("ella", "Ella", "Mew VMAX", EASY, 100),
        Opponent("daniel", "Daniel", "Lost Zone Box", MEDIUM, 150),
        Opponent("brittney", "Brittney", "Regigigas", MEDIUM, 150),
        Opponent("cammie", "Cammie", "Lugia VSTAR", HARD, 250),
        Opponent("otis", "Otis", "Mew VMAX", HARD, 250),
    ), coins=500, packs=1),
    League("platinum", "Platinum League", (
        Opponent("nathan", "Nathan", "Lost Zone Box", EASY, 200),
        Opponent("kendall", "Kendall", "Regigigas", EASY, 200),
        Opponent("mick", "Mick", "Mew VMAX", MEDIUM, 250),
        Opponent("logan", "Logan", "Lugia VSTAR", MEDIUM, 250),
        Opponent("penelope", "Penelope", "Lost Zone Box", HARD, 350),
        Opponent("tyson", "Tyson", "Regigigas", HARD, 350),
    ), coins=1000, packs=2),
)


def leagues():
    """Every league, in unlock order."""
    return LEAGUES


def opponents():
    """Every opponent in match order: league order, then position within the league.

    The client's panels are indexed by this order (`IndexedMatchPanel.matchIndex`),
    and so is the reward schedule, so the two must line up exactly.
    """
    return [opponent for entry in LEAGUES for opponent in entry.opponents]


def find(opponent_key):
    """The (league, opponent, position) for an opponent key, or None."""
    for league in LEAGUES:
        for position, opponent in enumerate(league.opponents):
            if opponent.key == opponent_key:
                return league, opponent, position
    return None


def select_opponent(raw):
    """The opponent a client-supplied value names, or None.

    Values arrive unlabelled (the client sends a scenario id from its own
    progression data), so a key, a display name, a league key and a match index
    are all accepted.
    """
    if raw is None:
        return None
    text = str(raw).strip()
    if not text:
        return None
    found = find(text.casefold())
    if found:
        return found[1]
    for opponent in opponents():
        if opponent.name.casefold() == text.casefold():
            return opponent
    entry = league(text.casefold())
    if entry:
        return entry.opponents[0]
    if text.isdigit():
        index = int(text)
        if 0 <= index < len(opponents()):
            return opponents()[index]
    return None


def league(league_key):
    """One league by key, or None."""
    return next((entry for entry in LEAGUES if entry.key == league_key), None)


def reward_schedule():
    """`LeagueAndGymModeRewards.totalRewardSchedule`: match index -> reward items.

    The client stores this as `PvEModeRewardsData.allMatchRewards` — one reward
    list per *match panel*, indexed by `IndexedMatchPanel.matchIndex` — so the map
    is keyed by opponent position, not by league.

    `UpdateRewards` copies the map into its own array with
    `for (i = 0; i < map.Count; i++) array[i] = map[i]`, so it indexes the map
    0..Count-1 and throws `KeyNotFoundException` on any key that is not exactly
    its loop index: keys are 0-based and contiguous.

    Each item is the client's shared reward object, whose only member `A` carries
    a currency amount that is `{name: <currency id>, value: <amount>}`.
    """
    return {
        str(index): [{"A": {"amount": {"name": TOKENS, "value": opponent.coins}}}]
        for index, opponent in enumerate(opponents())
    }


def opponent_deck(opponent):
    """A client-shaped 60-card deck for this opponent, built once per opponent."""
    cached = _DECKS.get(opponent.key)
    if cached is None:
        from ptcgo.game.content.starter import STARTER_DECKS, build_deck_data
        decklists = dict(STARTER_DECKS)
        cached = build_deck_data(f"{opponent.name}'s {opponent.deck}",
                                 decklists[opponent.deck])
        _DECKS[opponent.key] = cached
    return cached


_DECKS = {}
