from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="79f32884-75b4-58cd-8e2b-dddeb056647f",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EthansSlugma.Name",
    display_name="Ethan's Slugma",
    searchable_by=["Ethan's Slugma", "Basic", "EthansSlugma"],
    subtypes=["Basic"],
    collector_number=23,
    set_code="ME2PT5",
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