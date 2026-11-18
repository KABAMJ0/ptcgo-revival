from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="88fd5ede-5c1c-5fc3-a4e4-e0e59433567b",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latios.Name",
    display_name="Latios ◇",
    searchable_by=["Latios \u25c7", "Basic", "Prism Star", "Latios"],
    subtypes=["Basic", "Prism Star"],
    collector_number=108,
    set_code="SM7",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    family_id=381,
    abilities=[
        Attack(
            title="Dragon Fleet",
            game_text="This attack does 50 damage for each of your Evolution Dragon Pok\u00e9mon in play.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)