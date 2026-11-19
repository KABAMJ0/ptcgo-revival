from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def whirlpool_suction(ctx):
    """From the Bench: the opponent switches their Active; then discard
    everything attached to this Pokemon and put it on the bottom of the deck."""
    bench = [p for p in ctx.opponent_bench()]
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose the opponent's new Active Pokemon")
    if target is None:
        return
    await ctx.switch_active(ctx.opponent_id, target)
    source = ctx.source
    attached = list(getattr(source, "children", None) or [])
    if attached:
        await ctx.discard_cards(attached)
    await ctx.put_on_bottom_of_deck(source)


card = PokemonCardDef(
    guid="200f0d75-c183-5c24-9c4c-d0964827ab5f",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Phione.Name",
    display_name="Phione",
    searchable_by=["Phione", "Basic", "Phione"],
    subtypes=["Basic"],
    collector_number=220,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=489,
    abilities=[
        Ability(
            title="Whirlpool Suction",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is on your Bench, you may have your opponent switch their Active Pok\u00e9mon with 1 of their Benched Pok\u00e9mon. If you do, discard all cards attached to this Pok\u00e9mon and put it on the bottom of your deck.",
            activation=Activations.ONCE_PER_TURN,
            effect=whirlpool_suction,
        ),
        Attack(
            title="Rain Splash",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)