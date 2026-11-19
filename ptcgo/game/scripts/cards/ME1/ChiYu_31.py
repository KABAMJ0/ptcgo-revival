from ptcgo.game.data_utils import PokemonCardDef, Attack
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import lock_opponent_plays


async def scorching_earth(ctx):
    """40; discard the opponent's Stadium, and only if it was discarded,
    they can't play Stadium cards from hand next turn."""
    if ctx.stadium_in_play() is None:
        await ctx.deal_damage()
        return
    await ctx.discard_stadium()
    await lock_opponent_plays("stadium", damage=40)(ctx)


card = PokemonCardDef(
    guid="e831ca8e-3e36-5711-85d9-ccd3c2a60baa",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ChiYu.Name",
    display_name="Chi-Yu",
    searchable_by=["Chi-Yu", "Basic", "ChiYu"],
    subtypes=["Basic"],
    collector_number=31,
    set_code="ME1",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=1004,
    abilities=[
        Attack(
            title="Scorching Earth",
            game_text="If your opponent has a Stadium in play, discard it. If you do, your opponent can't play any Stadium cards from their hand during their next turn.",
            cost={PokemonTypes.FIRE: 1},
            damage=40,
            effect=scorching_earth,
        ),
    ],
)