from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a3edc573-9c0f-5a5e-b0bc-11777ffc802a",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Torterra.Name",
    display_name="Torterra",
    searchable_by=["Torterra", "Stage 2", "Torterra"],
    subtypes=["Stage 2"],
    collector_number=39,
    set_code="PL1",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grotle.Name",
    family_id=387,
    abilities=[
        Attack(
            title="Green Blast",
            game_text="Does 40 damage plus 10 more damage for each Grass Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Soothing Scent",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=unimplemented,
        ),
    ],
)