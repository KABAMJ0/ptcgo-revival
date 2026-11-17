from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="71856159-40e5-5ae4-81e3-c3c5c99c4330",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EthansSlugma.Name",
    display_name="Ethan's Slugma",
    searchable_by=["Ethan's Slugma", "Basic", "EthansSlugma"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="SV10",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=218,
    abilities=[
        Attack(
            title="Steady Firebreathing",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
    ],
)