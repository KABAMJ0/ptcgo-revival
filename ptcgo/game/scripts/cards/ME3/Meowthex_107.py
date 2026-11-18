from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6121a952-a451-5926-a6b6-98585a048d0d",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowthex.Name",
    display_name="Meowth ex",
    searchable_by=["Meowth ex", "Basic", "ex", "Meowthex"],
    subtypes=["Basic", "ex"],
    collector_number=107,
    set_code="ME3",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=52,
    abilities=[
        Ability(
            title="Last-Ditch Catch",
            game_text="Once during your turn, when you play this Pok\u00e9mon from your hand onto your Bench, you may use this Ability. Search your deck for a Supporter card, reveal it, and put it into your hand. Then, shuffle your deck. You can't use more than 1 Ability that has \"Last-Ditch\" in its name each turn.",
            effect=unimplemented,
        ),
        Attack(
            title="Tuck Tail",
            game_text="Put this Pok\u00e9mon and all attached cards into your hand.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=unimplemented,
        ),
    ],
)