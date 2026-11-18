"""Turn-boundary scheduling for delayed card effects.

Cards print delayed resolutions in two shapes and this module serves both:

* "at the end of your opponent's next turn" -- Dugtrio's Dig Trap bonus
  ("If Dugtrio is your Active Pokémon at the end of your opponent's next
  turn, put 6 damage counters on 1 of your opponent's Benched Pokémon"),
  Word of Ruin, Dark Gengar's prey marker;
* "at the end of this turn" / "at the start of your next turn" -- the same
  queue one boundary closer in.

The queue is keyed to a boundary, never to a bare turn number: an entry is
(event, owner player, not-before turn) and fires at the first matching turn
boundary at or after that turn. That is the same taxonomy
VisualizationLifetime uses ("start"/"end" of *your* or *your opponent's*
turn), so a reader meets one vocabulary in both places, and it survives the
extra-turn cards (Star Chronos, Yoga Loop) that make plain turn arithmetic
wrong -- a delayed effect fires on the opponent's actual next turn, not on
turn number N+1 if the opponent took it at N+2.

Delayed effects that are really *lifetimes* rather than resolutions ("during
your opponent's next turn, the Defending Pokémon takes 30 more damage",
"prevent all effects ... during your opponent's next turn") do not belong
here; they are stored with the thing they modify, e.g.
passives.TurnDamageModifier / passives.TargetDamageModifier /
TempPassive.expires_after_turn. This queue is only for "and then, later,
something happens".

GameSession drains it: `drain_turn_boundary("start", player_id)` from
_begin_turn and `drain_turn_boundary("end", player_id)` at the end of the
turn loop iteration. Entries are removed when drained, guard or not, so a
guarded-away effect never fires later.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable, List, Optional


class TurnBoundary(Enum):
    """The boundary a delayed effect waits for, worded from the registerer's
    side (the acting player's ctx.player_id)."""

    # "at the end of this turn" -- the acting player's current turn.
    END_OF_THIS_TURN = "end_of_this_turn"
    # "at the end of your opponent's next turn" (Dugtrio's Dig Trap rider).
    END_OF_OPPONENT_NEXT_TURN = "end_of_opponent_next_turn"
    # "at the start of your next turn".
    START_OF_YOUR_NEXT_TURN = "start_of_your_next_turn"
    # "at the start of your opponent's next turn".
    START_OF_OPPONENT_NEXT_TURN = "start_of_opponent_next_turn"

    def resolve(self, player_id: str, opponent_id: str,
                turn_number: int) -> "BoundaryPoint":
        """The (event, owner, not-before turn) this boundary names from
        `turn_number`.""" 
        return {
            TurnBoundary.END_OF_THIS_TURN: BoundaryPoint(
                "end", player_id, turn_number),
            TurnBoundary.END_OF_OPPONENT_NEXT_TURN: BoundaryPoint(
                "end", opponent_id, turn_number + 1),
            TurnBoundary.START_OF_YOUR_NEXT_TURN: BoundaryPoint(
                "start", player_id, turn_number + 2),
            TurnBoundary.START_OF_OPPONENT_NEXT_TURN: BoundaryPoint(
                "start", opponent_id, turn_number + 1),
        }[self]


@dataclass(frozen=True)
class BoundaryPoint:
    """A concrete turn edge: event ("start" / "end"), the player whose turn
    it is, and the first turn number it may fire on."""

    event: str
    owner_id: str
    not_before_turn: int


@dataclass
class ScheduledEffect:
    """One delayed effect waiting on a turn boundary.

    `effect` receives a fresh EffectContext whose player_id / source are the
    ones that registered it, so it can use the ordinary primitives (draw,
    damage, place counters, prompts) and its messages flush as their own
    sequence brackets.

    `guard(board)` returning False at fire time drops the entry silently (the
    usual "if it is still your Active Pokémon" clause). With
    `require_source_in_play` the entry is dropped when the registering
    Pokémon has left play, which is the shared half of "if this Pokémon is no
    longer in play, this effect doesn't happen".
    """

    event: str
    owner_id: str
    not_before_turn: int
    effect: Callable[[Any], Any]
    label: str = ""
    guard: Optional[Callable[[Any], bool]] = None
    source_entity_id: Optional[str] = None
    require_source_in_play: bool = False


class TurnScheduler:
    """The session's queue of boundary-keyed effects."""

    def __init__(self):
        self._queue: List[ScheduledEffect] = []

    def schedule(self, boundary, *, player_id: str, opponent_id: str,
                 turn_number: int, effect: Callable[[Any], Any],
                 label: str = "", guard: Optional[Callable[[Any], bool]] = None,
                 source_entity_id: Optional[str] = None,
                 require_source_in_play: bool = False) -> ScheduledEffect:
        """Registers `effect` at `boundary`, read from `player_id`'s side of
        turn `turn_number`. `boundary` is a TurnBoundary or its string value."""
        point = TurnBoundary(boundary).resolve(player_id, opponent_id, turn_number)
        entry = ScheduledEffect(
            event=point.event,
            owner_id=point.owner_id,
            not_before_turn=point.not_before_turn,
            effect=effect,
            label=label,
            guard=guard,
            source_entity_id=source_entity_id,
            require_source_in_play=require_source_in_play,
        )
        self._queue.append(entry)
        return entry

    def schedule_at(self, event: str, owner_id: str, not_before_turn: int,
                    effect: Callable[[Any], Any], label: str = "",
                    guard: Optional[Callable[[Any], bool]] = None,
                    source_entity_id: Optional[str] = None,
                    require_source_in_play: bool = False) -> ScheduledEffect:
        """The raw form, for an effect that already knows its turn edge."""
        entry = ScheduledEffect(
            event=event,
            owner_id=owner_id,
            not_before_turn=not_before_turn,
            effect=effect,
            label=label,
            guard=guard,
            source_entity_id=source_entity_id,
            require_source_in_play=require_source_in_play,
        )
        self._queue.append(entry)
        return entry

    def take_due(self, event: str, player_id: Optional[str],
                 turn_number: int) -> List[ScheduledEffect]:
        """Removes and returns every entry due at this turn edge."""
        if player_id is None:
            return []
        due = [
            e for e in self._queue
            if e.event == event and e.owner_id == player_id
            and turn_number >= e.not_before_turn
        ]
        if due:
            due_ids = {id(e) for e in due}
            self._queue = [e for e in self._queue if id(e) not in due_ids]
        return due

    def pending(self) -> List[ScheduledEffect]:
        """A copy of the queued entries, oldest first."""
        return list(self._queue)

    def clear(self) -> None:
        self._queue.clear()

    def __len__(self) -> int:
        return len(self._queue)


@dataclass
class BoundaryDrain:
    """Bookkeeping result of one drain, for logging and self-tests."""

    event: str
    player_id: str
    fired: List[str] = field(default_factory=list)
    skipped: List[str] = field(default_factory=list)
