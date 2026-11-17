from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="52c723f7-9624-5a1f-b527-6f93fcaaf9b2",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magby.Name",
    display_name="Magby",
    searchable_by=["Magby", "Basic", "Magby"],
    subtypes=["Basic"],
    collector_number=88,
    set_code="DP2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=240,
    abilities=[
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Magmar from your hand onto Magby (this counts as evolving Magby) and remove all damage counters from Magby.",
            effect=unimplemented,
        ),
        Attack(
            title="Scorch",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Burned.",
            cost={},
            effect=unimplemented,
        ),
    ],
)