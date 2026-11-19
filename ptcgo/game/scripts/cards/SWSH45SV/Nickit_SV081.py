from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def instigate(ctx):
    moved = await ctx.hand_to_bottom_of_deck(ctx.opponent_id)
    if moved > 0:
        await ctx.draw_cards(3, player_id=ctx.opponent_id)


card = PokemonCardDef(
    guid="21f5f566-8786-5ac0-adea-c515f9779d1e",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nickit.Name",
    display_name="Nickit",
    searchable_by=["Nickit", "Basic", "Nickit"],
    subtypes=["Basic"],
    collector_number=81,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=827,
    abilities=[
        Attack(
            title="Instigate",
            game_text="Your opponent shuffles their hand and puts it on the bottom of their deck. If they put any cards on the bottom of their deck in this way, they draw 3 cards.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=instigate,
        ),
    ],
)