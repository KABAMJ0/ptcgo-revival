from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="22a8959f-6760-5007-a20b-d8668642ab7e",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Milotic.Name",
    display_name="Milotic",
    searchable_by=["Milotic", "Stage 1", "Milotic"],
    subtypes=["Stage 1"],
    collector_number=7,
    set_code="PL3",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name",
    family_id=349,
    abilities=[
        Ability(
            title="Aqua Mirage",
            game_text="If you have no cards in your hand, prevent all damage done to Milotic by attacks from your opponent's Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Dwindling Wave",
            game_text="Does 80 damage minus 10 damage for each damage counter on Milotic.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="-",
            effect=unimplemented,
        ),
    ],
)