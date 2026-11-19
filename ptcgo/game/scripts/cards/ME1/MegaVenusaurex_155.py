from ptcgo.game.card_effects.support_common import (
    can_move_energy, heal_attack, move_energy_between,
)
from ptcgo.game.card_effects.trainers import basic_energy_of
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

_BASIC_GRASS = basic_energy_of("grass")


card = PokemonCardDef(
    guid="d3b4de48-47c6-585f-90e9-b8cdef5f8b62",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaVenusaurex.Name",
    display_name="Mega Venusaur ex",
    searchable_by=["Mega Venusaur ex", "Stage 2", "MEGA", "ex", "MegaVenusaurex"],
    subtypes=["Stage 2", "MEGA", "ex"],
    collector_number=155,
    set_code="ME1",
    rarity=Rarities.Rare,
    hp=380,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ivysaur.Name",
    family_id=1,
    abilities=[
        Ability(
            title="Solar Transfer",
            game_text="As often as you like during your turn, you may use this Ability. Move a Basic Grass Energy from 1 of your Pok\u00e9mon to another of your Pok\u00e9mon.",
            activation=Activations.UNLIMITED,
            effect=move_energy_between(_BASIC_GRASS, count=1,
                                       prompt="Choose a Grass Energy to move"),
            condition=can_move_energy(_BASIC_GRASS),
        ),
        Attack(
            title="Jungle Dump",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 4},
            damage=240,
            effect=heal_attack(30),
        ),
    ],
)