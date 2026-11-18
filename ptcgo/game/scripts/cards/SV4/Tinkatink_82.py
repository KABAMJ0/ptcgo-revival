from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _mountain_scrounging(ctx):
    """Look at the top card: keep it, or discard it and draw a card."""
    top = ctx.deck_top(1)
    if not top:
        return
    if await ctx.ask_yes_no("Put the top card of your deck into your hand?"):
        await ctx.put_in_hand(top, reveal=False)
        return
    await ctx.discard_cards(top)
    await ctx.draw_cards(1)

card = PokemonCardDef(
    guid="0d797cf2-5bd0-5393-a11c-0204cf2b236f",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatink.Name",
    display_name="Tinkatink",
    searchable_by=["Tinkatink", "Basic", "Tinkatink"],
    subtypes=["Basic"],
    collector_number=82,
    set_code="SV4",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=957,
    abilities=[
        Attack(
            title="Mountain Scrounging",
            game_text="Look at the top card of your deck. You may put that card into your hand. If you don't, discard that card and draw a card.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=_mountain_scrounging,
        ),
        Attack(
            title="Mumble",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)