from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def miraculous_comeback(ctx):
    """Flip one coin per Pokemon in play: 10 per heads to the Defending Pokemon,
    then 10 per tails to Rocket's Meowth itself."""
    in_play = len(ctx.my_pokemon_in_play()) + len(ctx.opponent_pokemon_in_play())
    if in_play <= 0:
        return
    flips = await ctx.flip_coins(in_play, "Miraculous Comeback")
    heads = sum(1 for flip in flips if flip)
    tails = in_play - heads
    if heads:
        await ctx.deal_damage(10 * heads)
    if tails and ctx.attacker is not None:
        await ctx.deal_damage(10 * tails, target=ctx.attacker, apply_modifiers=False)

card = PokemonCardDef(
    guid="fb39866f-97e4-5d09-bfc8-8209a92272ef",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsMeowth.Name",
    display_name="Team Rocket's Meowth",
    searchable_by=["Team Rocket's Meowth", "Basic", "TeamRocketsMeowth"],
    subtypes=["Basic"],
    collector_number=18,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=52,
    abilities=[
        Attack(
            title="Miraculous Comeback",
            game_text="Flip a number of coins equal to the number of Pok\u00e9mon in play. This attack does 10 damage times the number of heads. Then Team Rocket's Meowth does 10 damage times the number of tails to itself.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=miraculous_comeback,
        ),
    ],
)