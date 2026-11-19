from ptcgo.game.session.passives import carrier_pokemon
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import Passive, is_in_active_spot
from ptcgo.game.data_utils import def_for


def _other_player(board, player_id):
    """The other seat on this board."""
    return next(pid for pid in (getattr(board, "player_ids", None) or [])
                if pid != player_id)


def _pokemon_in_play(board, player_id):
    """Every top-level Pokemon a player has in the Active spot or on the Bench."""
    out = []
    for area_name in ("activePokemonArea", "bench"):
        area = board.find_player_area(player_id, area_name)
        out.extend(getattr(area, "children", []) or [])
    return [p for p in out if p is not None]


def _is_level_up(pokemon) -> bool:
    """A Pokemon LV.X: its definition carries the Level-Up subtype."""
    subtypes = getattr(def_for(getattr(pokemon, "archetype_id", "") or ""),
                       "subtypes", None) or []
    return any(str(s).lower().startswith("level") for s in subtypes)


class _Rivalry(Passive):
    """+50 to the Active while the opponent has a Pokemon LV.X in play."""

    def modify_damage_dealt(self, calc, carrier):
        attacker = calc.attacker
        if not (calc.is_attack and calc.is_opposing and attacker is not None):
            return
        if attacker is not carrier_pokemon(carrier) or not calc.to_active:
            return
        opponent = _other_player(calc.board, carrier.owning_player_id)
        if any(_is_level_up(p) for p in _pokemon_in_play(calc.board, opponent)):
            calc.amount += 50

card = PokemonCardDef(
    guid="a63384ed-5e61-5191-a276-f2683beaf653",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Luxray.Name",
    display_name="Luxray",
    searchable_by=["Luxray", "Stage 2", "Luxray"],
    subtypes=["Stage 2"],
    collector_number=8,
    set_code="DP6",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Luxio.Name",
    family_id=403,
    abilities=[
        Ability(
            title="Rivalry",
            game_text="If your opponent has any Pok\u00e9mon LV.X in play, each of Luxray's attacks does 50 more damage to the Active Pok\u00e9mon (before applying Weakness and Resistance).",
            passive=_Rivalry(),
        ),
        Attack(
            title="Plasma",
            game_text="Search your discard pile for a Lightning Energy card and attach it to Luxray.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=unimplemented,
        ),
        Attack(
            title="Shock Bolt",
            game_text="Discard all Lightning Energy attached to Luxray.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=unimplemented,
        ),
    ],
)