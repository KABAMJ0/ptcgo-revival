from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def amazing_plea(ctx):
    """Choose 2 cards from your discard pile; the opponent may allow them into
    your hand, and if they refuse the attack does 80 to their Active."""
    pile = list(ctx.discard_pile())
    picks = []
    if pile:
        picks = await ctx.choose_cards(
            pile, min(2, len(pile)),
            prompt="Choose 2 cards from your discard pile")
    allowed = picks and await ctx.ask_opponent(
        "May your opponent put those cards into their hand?", ["Yes", "No"]) == 0
    if allowed:
        await ctx.put_in_hand(picks)
    else:
        await ctx.deal_damage(80)


card = PokemonCardDef(
    guid="4c0be209-e950-5f34-bbbd-59ee46dda1eb",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cinccino.Name",
    display_name="Cinccino",
    searchable_by=["Cinccino", "Stage 1", "Cinccino"],
    subtypes=["Stage 1"],
    collector_number=86,
    set_code="SM4",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Minccino.Name",
    family_id=572,
    abilities=[
        Attack(
            title="Amazing Plea",
            game_text="Choose 2 cards from your discard pile. Then, ask your opponent if you may put them into your hand. If yes, put those cards into your hand. If no, this attack does 80 damage to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=amazing_plea,
        ),
    ],
)