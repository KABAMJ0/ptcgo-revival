from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c73e8546-e51d-5f25-b83a-fda5ffe48cb4",
    key="DC1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasAron.Name",
    display_name="Team Magma's Aron",
    searchable_by=["Team Magma's Aron", "Basic", "TeamMagmasAron"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="DC1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=304,
    abilities=[
        Attack(
            title="Gnaw",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
    ],
)