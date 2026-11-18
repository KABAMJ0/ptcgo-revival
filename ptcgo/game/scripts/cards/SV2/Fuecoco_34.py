from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="94866ec1-0e20-5a16-9f5e-18c4bfd29f0b",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fuecoco.Name",
    display_name="Fuecoco",
    searchable_by=["Fuecoco", "Basic", "Fuecoco"],
    subtypes=["Basic"],
    collector_number=34,
    set_code="SV2",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=909,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
    ],
)