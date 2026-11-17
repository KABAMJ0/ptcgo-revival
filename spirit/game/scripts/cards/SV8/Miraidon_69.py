from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0c812459-4207-5f93-98b9-ba665a032305",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Miraidon.Name",
    display_name="Miraidon",
    searchable_by=["Miraidon", "Basic", "Future", "Miraidon"],
    subtypes=["Basic", "Future"],
    collector_number=69,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=1008,
    abilities=[
        Attack(
            title="C.O.D.E.: Protect",
            game_text="During your opponent's next turn, prevent all damage done to each of your Future Pok\u00e9mon by attacks from Pok\u00e9mon ex. If this Pok\u00e9mon is no longer your Active Pok\u00e9mon, this effect ends.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=unimplemented,
        ),
        Attack(
            title="Thunder Claws",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)