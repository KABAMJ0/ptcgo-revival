from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="92b4f074-ad88-532f-8942-be1e4447eded",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaHawluchaex.Name",
    display_name="Mega Hawlucha ex",
    searchable_by=["Mega Hawlucha ex", "Basic", "MEGA", "ex", "MegaHawluchaex"],
    subtypes=["Basic", "MEGA", "ex"],
    collector_number=116,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=250,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=701,
    abilities=[
        Ability(
            title="Tenacious Body",
            game_text="If this Pok\u00e9mon would be Knocked Out by damage from an attack, flip a coin. If heads, this Pok\u00e9mon is not Knocked Out, and its remaining HP becomes 10.",
            effect=unimplemented,
        ),
        Attack(
            title="Somersault Dive",
            game_text="If a Stadium is in play, this attack does 140 more damage. Then, discard that Stadium.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)