from ptcgo.game.data_utils import StadiumCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import card_named_any, is_basic_pokemon


_TEAM_MAGMA = card_named_any(["Team Magma"])


async def _team_magma_hideout(ctx):
    """A Basic benched from hand that is not a Team Magma Pokemon takes 1
    damage counter."""
    pokemon = ctx.benched_pokemon
    if pokemon is None or not is_basic_pokemon(pokemon, ctx.board):
        return
    if _TEAM_MAGMA(pokemon):
        return
    await ctx.deal_damage(10, target=pokemon, apply_modifiers=False,
                          as_counters=True)


card = StadiumCardDef(
    guid="9c01768b-b7a2-5259-a978-6545d4298e00",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamMagmaHideout.Name",
    display_name="Team Magma Hideout",
    searchable_by=["Team Magma Hideout", "Stadium"],
    subtypes=["Stadium"],
    collector_number=83,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    abilities=[
        Ability(
            title='Team Magma Hideout',
            game_text="Whenever any player plays a Basic Pokemon that doesn't have Team Magma in its\nname from his or her hand, that player puts 1 damage counter on that Pokemon.",
            trigger=Triggers.ON_POKEMON_BENCHED,
            effect=_team_magma_hideout,
        ),
    ],
)
