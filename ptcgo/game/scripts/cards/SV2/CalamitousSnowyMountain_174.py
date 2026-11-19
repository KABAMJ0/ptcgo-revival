from ptcgo.game.data_utils import StadiumCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_pokemon, pokemon_of


_BASIC = is_basic_pokemon
_WATER = pokemon_of("water")


async def _calamitous_snowy_mountain(ctx):
    """A hand attach to the player's own Basic non-Water Pokemon costs it 2
    damage counters."""
    receiver = ctx.energy_receiver
    if receiver is None or ctx.attaching_player_id != receiver.owning_player_id:
        return
    if not _BASIC(receiver, ctx.board) or _WATER(receiver):
        return
    await ctx.deal_damage(20, target=receiver, apply_modifiers=False,
                          as_counters=True)


card = StadiumCardDef(
    guid="a662e600-bd33-50bd-9832-dac9d73d0729",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CalamitousSnowyMountain.Name",
    display_name="Calamitous Snowy Mountain",
    searchable_by=["Calamitous Snowy Mountain", "Stadium"],
    subtypes=["Stadium"],
    collector_number=174,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    abilities=[
        Ability(
            title='Calamitous Snowy Mountain',
            game_text='Whenever any player attaches an Energy card from their hand to 1 of their\nBasic non-Water Pokemon, put 2 damage counters on that Pokemon.',
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=_calamitous_snowy_mountain,
        ),
    ],
)
