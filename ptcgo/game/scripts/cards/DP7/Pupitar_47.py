from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7fbfbee7-88e5-5bad-81de-4cb2a256e833",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name",
    display_name="Pupitar",
    searchable_by=["Pupitar", "Stage 1", "Pupitar"],
    subtypes=["Stage 1"],
    collector_number=47,
    set_code="DP7",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Larvitar.Name",
    family_id=246,
    abilities=[
        Ability(
            title="Energy Protection",
            game_text="Any damage done to Pupitar by attacks is reduced by 10 for each Energy attached to Pupitar (after applying Weakness and Resistance). You can't reduce more than 30 damage in this way.",
            effect=unimplemented,
        ),
        Attack(
            title="Rock Smash",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 20 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)