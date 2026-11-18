from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2cbaba24-6777-56c6-b9c6-6c426fe77292",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaSharpedoex.Name",
    display_name="Mega Sharpedo ex",
    searchable_by=["Mega Sharpedo ex", "Stage 1", "MEGA", "ex", "MegaSharpedoex"],
    subtypes=["Stage 1", "MEGA", "ex"],
    collector_number=61,
    set_code="ME2",
    rarity=Rarities.Rare,
    hp=330,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Carvanha.Name",
    family_id=318,
    abilities=[
        Attack(
            title="Greedy Fang",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=70,
            effect=unimplemented,
        ),
        Attack(
            title="Hungry Jaws",
            game_text="If this Pok\u00e9mon has any damage counters on it, this attack does 150 more damage.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=120,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)