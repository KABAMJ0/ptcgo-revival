from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bf414aaf-75f9-579d-bb16-081d7ddfad30",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PuruglyG.Name",
    display_name="Purugly G",
    searchable_by=["Purugly G", "Basic", "SP", "PuruglyG"],
    subtypes=["Basic", "SP"],
    collector_number=88,
    set_code="PL1",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=432,
    abilities=[
        Attack(
            title="Chip Off",
            game_text="If your opponent has 6 or more cards in his or her hand, discard a number of cards without looking until your opponent has 5 cards left in his or her hand.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Poor Sleep",
            game_text="Flip a coin. If heads, this attack does 50 damage plus 30 more damage and Purugly G is now Asleep.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)