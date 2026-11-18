from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a5ff22e7-03d5-5f82-b284-fd9c94df26b2",
    key="DP4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wigglytuff.Name",
    display_name="Wigglytuff",
    searchable_by=["Wigglytuff", "Stage 1", "Wigglytuff"],
    subtypes=["Stage 1"],
    collector_number=32,
    set_code="DP4",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name",
    family_id=39,
    abilities=[
        Ability(
            title="Good Night Melody",
            game_text="Once during your turn (before your attack), you may use this power. Each Active Pok\u00e9mon (both yours and your opponent's) is now Asleep. This power can't be used if Wigglytuff is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Ballon Attack",
            game_text="If Igglybuff is anywhere under Wigglytuff, this attack does 40 damage plus 20 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)