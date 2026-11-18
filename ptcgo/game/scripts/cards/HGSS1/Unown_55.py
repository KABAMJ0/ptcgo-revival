from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def effect(ctx):
    await ctx.reorder_deck_top(5)


card = PokemonCardDef(
    guid="dfe7d3bc-8854-5b95-b844-38dbd7d52f6e",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Unown.Name",
    display_name="Unown",
    searchable_by=["Unown", "Basic", "Unown"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="HGSS1",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="FLASH",
            game_text="Once during your turn, when you put Unown from your hand onto your Bench, you may look at the top 5 cards of your deck and put them back on top of your deck in any order.",
            trigger=Triggers.ON_PLAY,
            effect=effect,
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)