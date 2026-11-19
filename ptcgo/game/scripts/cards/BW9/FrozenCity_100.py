from ptcgo.game.data_utils import StadiumCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import pokemon_of_subtype


_TEAM_PLASMA = pokemon_of_subtype("Team Plasma")


async def _frozen_city(ctx):
    """A hand attach to the player's own non-Team Plasma Pokemon costs it 2
    damage counters."""
    receiver = ctx.energy_receiver
    if receiver is None or ctx.attaching_player_id != receiver.owning_player_id:
        return
    if _TEAM_PLASMA(receiver):
        return
    await ctx.deal_damage(20, target=receiver, apply_modifiers=False,
                          as_counters=True)


card = StadiumCardDef(
    guid="b676ca51-b6cf-5d9f-8b1e-45a89cb027d4",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FrozenCity.Name",
    display_name="Frozen City",
    searchable_by=["Frozen City", "Stadium", "Team Plasma"],
    subtypes=["Stadium", "Team Plasma"],
    collector_number=100,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    abilities=[
        Ability(
            title='Frozen City',
            game_text='Whenever any player attaches an Energy from his or her hand to 1 of his or\nher Pokemon (excluding Team Plasma Pokemon), put 2 damage counters on that\nPokemon.',
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=_frozen_city,
        ),
    ],
)
