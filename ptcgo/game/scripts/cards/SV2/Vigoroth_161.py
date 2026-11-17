from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ba948cba-41a4-588b-8b98-5080789fb709",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vigoroth.Name",
    display_name="Vigoroth",
    searchable_by=["Vigoroth", "Stage 1", "Vigoroth"],
    subtypes=["Stage 1"],
    collector_number=161,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slakoth.Name",
    family_id=287,
    abilities=[
        Attack(
            title="Confront",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
        Attack(
            title="Sharp Claws",
            game_text="Flip a coin. If heads, this attack does 60 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)