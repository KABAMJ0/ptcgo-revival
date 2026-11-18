from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fcbf80ed-ae42-51a9-92a8-237b02f179ab",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skorupi.Name",
    display_name="Skorupi",
    searchable_by=["Skorupi", "Basic", "Skorupi"],
    subtypes=["Basic"],
    collector_number=82,
    set_code="SM11",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=451,
    abilities=[
        Attack(
            title="Knock Off",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Bug Bite",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
        ),
    ],
)