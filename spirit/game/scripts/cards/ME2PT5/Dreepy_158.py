from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0fc37927-af1a-52e5-864e-84099709c98c",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dreepy.Name",
    display_name="Dreepy",
    searchable_by=["Dreepy", "Basic", "Dreepy"],
    subtypes=["Basic"],
    collector_number=158,
    set_code="ME2PT5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=885,
    abilities=[
        Attack(
            title="Petty Grudge",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.PSYCHIC: 1},
            damage=40,
        ),
    ],
)