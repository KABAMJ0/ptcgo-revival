from ptcgo.game.data_utils import StadiumCardDef, Attack, def_for
from ptcgo.game.attributes import PokemonTypes, Rarities
from ptcgo.game.session.passives import Passive


def _is_delta(card):
    name = getattr(def_for(card.archetype_id), "display_name", "") or ""
    return "\u03b4" in name


async def _delta_call(ctx):
    picks = await ctx.search_deck(
        _is_delta, count=1, minimum=0,
        prompt="Choose a Pok\u00e9mon that has \u03b4 on its card")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


_DELTA_CALL = Attack(
    title="Delta Call",
    game_text="Search your deck for a Pok\u00e9mon that has \u03b4 on its card, "
              "show it to your opponent, and put it into your hand. Shuffle "
              "your deck afterward.",
    cost={PokemonTypes.COLORLESS: 1},
    effect=_delta_call,
)


class HolonLakePassive(Passive):
    """Each player's Pokemon that has delta on its card may use Delta Call."""

    def granted_attacks(self, board, pokemon, carrier):
        return [_DELTA_CALL] if _is_delta(pokemon) else []


card = StadiumCardDef(
    guid="58b6e0bc-f74a-5f97-b04d-11c1b1473f99",
    key="EX13",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonLake.Name",
    display_name="Holon Lake",
    searchable_by=["Holon Lake", "Stadium"],
    subtypes=["Stadium"],
    collector_number=87,
    set_code="EX13",
    rarity=Rarities.Uncommon,
    passive=HolonLakePassive(),
)
