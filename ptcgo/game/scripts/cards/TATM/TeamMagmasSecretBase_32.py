from ptcgo.game.data_utils import StadiumCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import card_named_any, is_basic_pokemon


_TEAM_MAGMA = card_named_any(["Team Magma"])


async def _magma_bench_toll(ctx):
    """A Basic benched from hand that is not a Team Magma Pokemon takes 2
    damage counters."""
    pokemon = ctx.benched_pokemon
    if pokemon is None or not is_basic_pokemon(pokemon, ctx.board):
        return
    if _TEAM_MAGMA(pokemon):
        return
    await ctx.deal_damage(20, target=pokemon, apply_modifiers=False,
                          as_counters=True)

card = StadiumCardDef(
    guid="00a64349-e0e4-532e-a4fb-89d300f40dbd",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamMagmasSecretBase.Name",
    display_name="Team Magma's Secret Base",
    searchable_by=["Team Magma's Secret Base", "Stadium"],
    subtypes=["Stadium"],
    collector_number=32,
    set_code="TATM",
    rarity=Rarities.Uncommon,
    abilities=[
        Ability(
            title="Team Magma's Secret Base",
            game_text="Whenever any player puts a Basic Pok\u00e9mon (except for Team Magma Pok\u00e9mon) from his or her hand onto his or her Bench, put 2 damage counters on that Pok\u00e9mon.",
            trigger=Triggers.ON_POKEMON_BENCHED,
            effect=_magma_bench_toll,
        ),
    ],
)
