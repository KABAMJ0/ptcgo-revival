from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e6147f47-b51d-5d5c-ad9e-b21b5b445a3f",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShiningArceus.Name",
    display_name="Shining Arceus",
    searchable_by=["Shining Arceus", "Basic", "ShiningArceus"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="SL",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=493,
    abilities=[
        Ability(
            title="Fabled Defense",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, prevent all damage done to your Benched Pok\u00e9mon by your opponent's attacks.",
            effect=unimplemented,
        ),
        Attack(
            title="Ultimate Arrow",
            game_text="This attack does 30 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 4},
            effect=unimplemented,
        ),
    ],
)