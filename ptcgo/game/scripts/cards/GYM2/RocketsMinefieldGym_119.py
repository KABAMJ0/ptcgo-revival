from ptcgo.game.data_utils import StadiumCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities


async def _minefield(ctx):
    """The player who just benched a Basic from hand flips a coin; tails puts
    2 damage counters on that Pokemon."""
    pokemon = ctx.benched_pokemon
    if pokemon is None:
        return
    heads = await ctx.flip_coins(1, "Rocket's Minefield Gym", source=ctx.source)
    if not heads[0]:
        await ctx.deal_damage(20, target=pokemon, apply_modifiers=False,
                              as_counters=True)


card = StadiumCardDef(
    guid="001174e4-1a40-5fb7-a678-f8555a7adb78",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RocketsMinefieldGym.Name",
    display_name="Rocket's Minefield Gym",
    searchable_by=["Rocket's Minefield Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=119,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    abilities=[
        Ability(
            title="Rocket's Minefield Gym",
            game_text="Whenever a player puts a Basic Pok\u00e9mon onto his or "
                      "her Bench from his or her hand, he or she flips a coin. "
                      "If tails, put 2 damage counters on that Pok\u00e9mon.",
            trigger=Triggers.ON_POKEMON_BENCHED,
            effect=_minefield,
        ),
    ],
)
