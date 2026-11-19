from ptcgo.game.card_effects.attacks_common import conditions_if
from ptcgo.game.card_effects.passives_common import discard_from_hand_then, unafflicted
from ptcgo.game.card_effects.support_common import opponent_switches
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, Triggers, unimplemented, def_for, subtypes_for
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

_EVOLVED_STAGES = ("Stage 1", "Stage 2", "VMAX", "BREAK")


def _regi_move_condition(board, player_id, pokemon) -> bool:
    """Regi Move needs a clean Regice, a non-Evolved opposing Active with a Bench to swap in."""
    if not unafflicted(board, player_id, pokemon):
        return False
    for child in board.playmat.children:
        other = getattr(child, "owning_player_id", None)
        if other is None or other == player_id:
            continue
        active = board.active_pokemon(other)
        bench = board.find_player_area(other, "bench")
        if active is None or not bench or not bench.children:
            continue
        if any(stage in _EVOLVED_STAGES
               for stage in subtypes_for(active.archetype_id)):
            return False
        return True
    return False


async def _regi_move(ctx):
    await opponent_switches(ctx)


def _regi_reflect_condition(ctx) -> bool:
    return ctx.attacker is not None and \
        ctx.damaged_by_attack_last_turn(ctx.attacker) > 0

card = PokemonCardDef(
    guid="ea1646f9-88d9-5cdf-b63c-df3d4bb93c86",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regice.Name",
    display_name="Regice",
    searchable_by=["Regice", "Basic", "Regice"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="DP6",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    family_id=378,
    abilities=[
        Ability(
            title="Regi Move",
            game_text="Once during your turn (before your attack), you may use this power. Discard 2 cards from your hand and choose 1 of your opponent's Active Pok\u00e9mon that isn't an Evolved Pok\u00e9mon. Then, your opponent switches that Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon. This power can't be used if Regice is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=_regi_move_condition,
            effect=discard_from_hand_then(None, 2, then=_regi_move),
        ),
        Attack(
            title="Ice Reflect",
            game_text="If Regice was damaged by an attack during your opponent's last turn, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=conditions_if(_regi_reflect_condition,
                                 SpecialConditions.PARALYZED),
        ),
    ],
)