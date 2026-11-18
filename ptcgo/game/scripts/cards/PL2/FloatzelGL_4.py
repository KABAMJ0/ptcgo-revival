from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3d6bf181-ec87-5684-a821-344665ccb75e",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FloatzelGL.Name",
    display_name="Floatzel GL",
    searchable_by=["Floatzel GL", "Basic", "SP", "FloatzelGL"],
    subtypes=["Basic", "SP"],
    collector_number=4,
    set_code="PL2",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=419,
    abilities=[
        Attack(
            title="Incite",
            game_text="Search your discard pile for up to 2 Supporter cards, show them to your opponent, and put them into your hand.",
            cost={},
            effect=unimplemented,
        ),
        Attack(
            title="Giant Wave",
            game_text="Floatzel GL can't use Giant Wave during your next turn.",
            cost={PokemonTypes.WATER: 2},
            damage=50,
            effect=unimplemented,
        ),
    ],
)