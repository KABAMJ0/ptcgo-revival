from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.passives_common import unafflicted
from ptcgo.game.data_utils import Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def energy_burn(ctx):
    """Every Energy on Charizard provides Fire for the rest of the turn."""
    ctx.rewrite_energy_types([PokemonTypes.FIRE.value], pokemon=ctx.source,
                             through_turn=ctx.session.turn_state.turn_number)


card = PokemonCardDef(
    guid="0f124417-b34c-512c-9ab5-fe48edb50c5b",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charizard.Name",
    display_name="Charizard",
    searchable_by=["Charizard", "Stage 2", "Charizard"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="BASE6",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=4,
    abilities=[
        Ability(
            title="Energy Burn",
            game_text="As often as you like during your turn (before your attack), you may turn all Energy attached to Charizard into Fire Energy for the rest of the turn. This power can't be used if Charizard is affected by a Special Condition.",
            activation=Activations.UNLIMITED,
            condition=unafflicted,
            effect=energy_burn,
        ),
        Attack(
            title="Fire Spin",
            game_text="Discard 2 Energy cards attached to Charizard or this attack does nothing.",
            cost={PokemonTypes.FIRE: 4},
            damage=100,
            effect=unimplemented,
        ),
    ],
)