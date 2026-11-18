from ptcgo.game.data_utils import StadiumCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_pokemon, pokemon_of


_EXEMPT = (pokemon_of("grass"), pokemon_of("psychic"))


async def _miasma_valley(ctx):
    """A Basic Pokemon benched from hand takes 2 damage counters unless it is
    a Grass or Psychic Pokemon."""
    pokemon = ctx.benched_pokemon
    if pokemon is None or not is_basic_pokemon(pokemon, ctx.board):
        return
    if any(check(pokemon) for check in _EXEMPT):
        return
    await ctx.deal_damage(20, target=pokemon, apply_modifiers=False,
                          as_counters=True)


card = StadiumCardDef(
    guid="fbbc1a46-3c01-5c4e-a543-03af27649480",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MiasmaValley.Name",
    display_name="Miasma Valley",
    searchable_by=["Miasma Valley", "Stadium"],
    subtypes=["Stadium"],
    collector_number=111,
    set_code="PL1",
    rarity=Rarities.Uncommon,
    abilities=[
        Ability(
            title='Miasma Valley',
            game_text='Whenever any player puts a Basic Pokemon (excluding Grass or Psychic Pokemon)\nfrom his or her hand onto his or her Bench, put 2 damage counters on that\nPokemon.',
            trigger=Triggers.ON_POKEMON_BENCHED,
            effect=_miasma_valley,
        ),
    ],
)
