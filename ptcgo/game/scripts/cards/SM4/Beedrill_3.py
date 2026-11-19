from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import conditions_if


def _evolved_this_turn(ctx) -> bool:
    """Beedrill reaches play only by evolving Kakuna, so "evolved from Kakuna
    during this turn" is the turn it entered play."""
    state = ctx.session.turn_state
    return state.entered_play_turn.get(ctx.attacker.entity_id) == state.turn_number


card = PokemonCardDef(
    guid="404ba0e5-ac58-5a0a-a051-beb3c61970c7",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beedrill.Name",
    display_name="Beedrill",
    searchable_by=["Beedrill", "Stage 2", "Beedrill"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="SM4",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kakuna.Name",
    family_id=13,
    abilities=[
        Attack(
            title="Sudden Sting",
            game_text="If this Pok\u00e9mon evolved from Kakuna during this turn, your opponent's Active Pok\u00e9mon is now Paralyzed and Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=conditions_if(_evolved_this_turn, SpecialConditions.PARALYZED,
                                 SpecialConditions.POISONED),
        ),
        Attack(
            title="Sharp Sting",
            cost={PokemonTypes.GRASS: 1},
            damage=60,
        ),
    ],
)