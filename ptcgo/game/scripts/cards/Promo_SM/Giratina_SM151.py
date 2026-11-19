from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def distortion_door(ctx):
    """From the discard pile onto your Bench, then 1 damage counter on 2 of the
    opponent's Benched Pokemon."""
    source = ctx.source
    if source is None:
        return
    if not await ctx.bench_pokemon(source):
        return
    bench = list(ctx.opponent_bench())[:2]
    if bench:
        await ctx.place_damage_counters(len(bench), bench)


card = PokemonCardDef(
    guid="e4604c2d-41af-554b-b871-036902cd0fd2",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Giratina.Name",
    display_name="Giratina",
    searchable_by=["Giratina", "Basic", "Giratina"],
    subtypes=["Basic"],
    collector_number=151,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=487,
    abilities=[
        Ability(
            title="Distortion Door",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is in your discard pile, you may put it onto your Bench. If you do, put 1 damage counter on 2 of your opponent's Benched Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            effect=distortion_door,
        ),
        Attack(
            title="Shadow Impact",
            game_text="Put 4 damage counters on 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=unimplemented,
        ),
    ],
)