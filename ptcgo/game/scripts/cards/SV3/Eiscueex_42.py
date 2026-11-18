from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="dc39203f-fa3f-542c-a0fd-5f5cbd058a02",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eiscueex.Name",
    display_name="Eiscue ex",
    searchable_by=["Eiscue ex", "Basic", "ex", "Tera", "Eiscueex"],
    subtypes=["Basic", "ex", "Tera"],
    collector_number=42,
    set_code="SV3",
    rarity=Rarities.Rare,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=875,
    abilities=[
        Attack(
            title="Scalding Block",
            game_text="Discard an Energy from this Pok\u00e9mon. During your opponent's next turn, the Defending Pok\u00e9mon can't attack.",
            cost={PokemonTypes.WATER: 3},
            damage=160,
            effect=unimplemented,
        ),
    ],
)