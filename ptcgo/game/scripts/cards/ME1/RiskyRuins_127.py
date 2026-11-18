from ptcgo.game.data_utils import StadiumCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_pokemon, pokemon_of


_DARKNESS = pokemon_of("darkness")


async def _risky_ruins(ctx):
    """A Basic non-Darkness Pokemon benched from hand takes 2 damage counters."""
    pokemon = ctx.benched_pokemon
    if pokemon is None or not is_basic_pokemon(pokemon, ctx.board):
        return
    if _DARKNESS(pokemon):
        return
    await ctx.deal_damage(20, target=pokemon, apply_modifiers=False,
                          as_counters=True)


card = StadiumCardDef(
    guid="34f2d480-4d64-528e-a379-c5728742136c",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RiskyRuins.Name",
    display_name="Risky Ruins",
    searchable_by=["Risky Ruins", "Stadium"],
    subtypes=["Stadium"],
    collector_number=127,
    set_code="ME1",
    rarity=Rarities.Uncommon,
    abilities=[
        Ability(
            title='Risky Ruins',
            game_text='Whenever any player puts a Basic non-Darkness Pokemon onto their Bench\nduring their turn, place 2 damage counters on that Pokemon.',
            trigger=Triggers.ON_POKEMON_BENCHED,
            effect=_risky_ruins,
        ),
    ],
)
