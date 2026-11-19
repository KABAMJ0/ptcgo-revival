from ptcgo.game.data_utils import Ability, Activations, StadiumCardDef, def_for
from ptcgo.game.attributes import Rarities
from ptcgo.game.session.passives import is_basic_energy

SABRINA = "sabrina"


def _named_sabrina(pokemon) -> bool:
    definition = def_for(pokemon.archetype_id)
    return SABRINA in (getattr(definition, "display_name", "") or "").lower()


def _usable_holders(board, player_id):
    """The player's Pokemon with Sabrina in the name that hold a basic Energy."""
    return [pokemon for pokemon in board.pokemon_in_play(player_id)
            if _named_sabrina(pokemon)
            and any(is_basic_energy(energy)
                    for energy in board.attached_energies(pokemon))]


def _offer_condition(board, player_id, stadium=None) -> bool:
    return bool(_usable_holders(board, player_id))


async def saffron_city_gym_power(ctx):
    """Return 1 basic Energy attached to 1 of your Sabrina Pokemon to hand."""
    holders = _usable_holders(ctx.board, ctx.player_id)
    if not holders:
        return
    holder = holders[0] if len(holders) == 1 else await ctx.choose_pokemon(
        holders, "Choose a Pok\u00e9mon with Sabrina in its name")
    if holder is None:
        return
    basics = [energy for energy in ctx.attached_energies(holder)
              if is_basic_energy(energy)]
    if not basics:
        return
    picks = basics[:1] if len(basics) == 1 else await ctx.choose_cards(
        basics, 1, minimum=1,
        prompt="Choose a basic Energy card to return to your hand")
    if picks:
        await ctx.put_in_hand(picks, reveal=False)


card = StadiumCardDef(
    guid="43d43b08-9d0f-5e3a-b4b0-68ad948ec074",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SaffronCityGym.Name",
    display_name="Saffron City Gym",
    searchable_by=["Saffron City Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=122,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Saffron City Gym",
        game_text="As often as each player likes during his or her turn (before attacking), that player may return 1 basic Energy card attached to 1 of his or her Pok\u00e9mon with Sabrina in its name to his or her hand.",
        activation=Activations.UNLIMITED,
        effect=saffron_city_gym_power,
        condition=_offer_condition,
    ),
)
