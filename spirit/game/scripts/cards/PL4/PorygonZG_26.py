from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f7a3a44a-31a7-5400-8431-354baba7edb3",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PorygonZG.Name",
    display_name="Porygon-Z G",
    searchable_by=["Porygon-Z G", "Basic", "SP", "PorygonZG"],
    subtypes=["Basic", "SP"],
    collector_number=26,
    set_code="PL4",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=474,
    abilities=[
        Ability(
            title="Dowsing Code",
            game_text="Once during your turn, when you put Porygon-Z G from your hand onto your Bench, you may search your discard pile for up to 2 Pok\u00e9mon Tool cards, show them to your opponent, and shuffle them into your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Ambush",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 40 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)