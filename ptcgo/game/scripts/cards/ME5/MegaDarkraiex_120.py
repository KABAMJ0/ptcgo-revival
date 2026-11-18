from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e340ab96-793a-5436-81f1-a25b412149a5",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaDarkraiex.Name",
    display_name="Mega Darkrai ex",
    searchable_by=["Mega Darkrai ex", "Basic", "MEGA", "ex", "MegaDarkraiex"],
    subtypes=["Basic", "MEGA", "ex"],
    collector_number=120,
    set_code="ME5",
    rarity=Rarities.Rare,
    hp=280,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=491,
    abilities=[
        Attack(
            title="Dusk Raid",
            game_text="If your Benched Pok\u00e9mon have any damage counters on them, this attack does 110 more damage.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=110,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Abyss Eye",
            game_text="If your opponent's Active Pok\u00e9mon is affected by a Special Condition, it is Knocked Out.",
            cost={PokemonTypes.DARKNESS: 3},
            effect=unimplemented,
        ),
    ],
)