from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4513cdbb-3905-5083-b86c-62d5da2e411e",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronMoth.Name",
    display_name="Iron Moth",
    searchable_by=["Iron Moth", "Basic", "Future", "IronMoth"],
    subtypes=["Basic", "Future"],
    collector_number=9,
    set_code="SV6PT5",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    abilities=[
        Attack(
            title="Suction",
            game_text="Heal from this Pok\u00e9mon the same amount of damage you did to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Anachronism Repulsor",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Ancient Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=unimplemented,
        ),
    ],
)