from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.attacks_common import discard_for_bonus
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

_provides = lambda type_value: (
    lambda card: energy_provides_type(card, type_value.value)
)


card = PokemonCardDef(
    guid="0984787f-7f77-5999-9be5-2b87a1d4ab21",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RillaboomVMAX.Name",
    display_name="Rillaboom VMAX",
    searchable_by=["Rillaboom VMAX", "VMAX", "RillaboomVMAX"],
    subtypes=["VMAX"],
    collector_number=106,
    set_code="SWSH45SV",
    rarity=Rarities.RareHoloVMAX,
    hp=330,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.RillaboomV.Name",
    family_id=812,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Max Beating",
            game_text="You may discard up to 3 Grass Energy from this Pok\u00e9mon. If you do, this attack does 50 more damage for each card you discarded in this way.",
            cost={PokemonTypes.GRASS: 3, PokemonTypes.COLORLESS: 1},
            damage=130,
            damage_operator="+",
            effect=discard_for_bonus(
                source="self-energy",
                predicate=_provides(PokemonTypes.GRASS),
                max_count=3,
                per=50,
            ),
        ),
    ],
)