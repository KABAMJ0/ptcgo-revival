from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="18f3c85f-22a4-5834-905b-806c5a373074",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slaking.Name",
    display_name="Slaking",
    searchable_by=["Slaking", "Stage 2", "Slaking"],
    subtypes=["Stage 2"],
    collector_number=162,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vigoroth.Name",
    family_id=287,
    abilities=[
        Ability(
            title="Stir and Snooze",
            game_text="If this Pok\u00e9mon is Asleep, flip 2 coins instead of 1 during Pok\u00e9mon Checkup. If either of them is tails, this Pok\u00e9mon is still Asleep.",
            effect=unimplemented,
        ),
        Attack(
            title="Slacker's Headstrike",
            game_text="This Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=240,
            effect=unimplemented,
        ),
    ],
)