from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="219d7070-ddbf-504a-b914-4f4a15a65719",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysStarmie.Name",
    display_name="Misty's Starmie",
    searchable_by=["Misty's Starmie", "Stage 1", "MistysStarmie"],
    subtypes=["Stage 1"],
    collector_number=56,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MistysStaryu.Name",
    family_id=120,
    abilities=[
        Attack(
            title="Water Gun",
            game_text="Does 10 damage plus 10 more damage for each Water Energy attached to Misty's Starmie but not used to pay for this attack's Energy cost. You can't add more than 20 damage in this way.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Bubblebeam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 3},
            damage=30,
            effect=unimplemented,
        ),
    ],
)