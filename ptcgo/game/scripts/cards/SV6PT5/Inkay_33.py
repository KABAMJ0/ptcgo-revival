from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def mischievous_tail(ctx):
    """Look at the top card of your opponent's deck. You may have your
    opponent shuffle their deck."""
    top = ctx.deck_top(1, player_id=ctx.opponent_id)
    if top:
        await ctx.session.prompt_view_cards(
            ctx.player_id, ctx.source.entity_id, top,
            prompt="Top card of your opponent's deck",
        )
    if await ctx.ask_yes_no("Have your opponent shuffle their deck?"):
        await ctx.shuffle_deck(ctx.opponent_id)


card = PokemonCardDef(
    guid="1d03f9e8-d8a3-567f-9cf0-c7976e50d9e3",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name",
    display_name="Inkay",
    searchable_by=["Inkay", "Basic", "Inkay"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="SV6PT5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=686,
    abilities=[
        Attack(
            title="Mischievous Tentacles",
            game_text="Look at the top card of your opponent's deck. You may have your opponent shuffle their deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=mischievous_tail,
        ),
        Attack(
            title="Peck",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
    ],
)