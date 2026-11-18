from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c142d3a5-5e0f-54c4-b060-c6fc042e75d1",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golduck.Name",
    display_name="Golduck",
    searchable_by=["Golduck", "Stage 1", "Golduck"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="PL1",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name",
    family_id=54,
    abilities=[
        Attack(
            title="Swim",
            game_text="If your opponent has any Water Energy attached to any of his or her Pok\u00e9mon, you may do 30 damage to any 1 Benched Pok\u00e9mon instead. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Water Slide",
            game_text="You may move all Energy cards attached to Golduck to 1 of your Benched Pok\u00e9mon. If you do, this attack does 40 damage plus 20 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)