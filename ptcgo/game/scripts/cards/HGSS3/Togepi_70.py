from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _plead(ctx):
    answer = await ctx.ask_opponent(
        "May your opponent draw 2 cards?", ["Yes", "No"])
    if answer == 0:
        await ctx.draw_cards(2)
    else:
        await ctx.deal_damage(20)

card = PokemonCardDef(
    guid="c8dd0179-be0f-5da0-a1cc-cf1004bf5f85",
    key="HGSS3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togepi.Name",
    display_name="Togepi",
    searchable_by=["Togepi", "Basic", "Togepi"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="HGSS3",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=175,
    abilities=[
        Attack(
            title="Plead",
            game_text="Ask your opponent if you may draw 2 cards. If yes, draw 2 cards. If no, this attack does 20 damage to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_plead,
        ),
    ],
)