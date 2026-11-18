from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="175cff49-08a4-559c-82ed-c86d3a3f4dd4",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skitty.Name",
    display_name="Skitty",
    searchable_by=["Skitty", "Basic", "Skitty"],
    subtypes=["Basic"],
    collector_number=104,
    set_code="XY1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=300,
    abilities=[
        Attack(
            title="Heal Bell",
            game_text="Heal 10 damage from each of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Tail Whap",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)