from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.passives import Passive


class _PerplexingEyesPassive(Passive):
    """The carrier's Weakness reads Psychic for as long as this rides it; the
    multiplier is untouched, so "the amount of Weakness doesn't change"."""

    def modify_weakness(self, calc, carrier):
        if calc.target is carrier:
            calc.weak_types = [PokemonTypes.PSYCHIC.value]


async def perplexing_eyes(ctx):
    """Printed damage; the Defending Pokemon's Weakness is Psychic until the
    end of your next turn."""
    await ctx.deal_damage()
    if ctx.defender is not None:
        ctx.add_passive_through_own_next_turn(ctx.defender,
                                              _PerplexingEyesPassive())


card = PokemonCardDef(
    guid="24bef80e-7d94-5e60-9f26-64d46e56a5c3",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Espurr.Name",
    display_name="Espurr",
    searchable_by=["Espurr", "Basic", "Espurr"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="SM3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=677,
    abilities=[
        Attack(
            title="Perplexing Eyes",
            game_text="The Defending Pok\u00e9mon's Weakness is now Psychic until the end of your next turn. (The amount of Weakness doesn't change.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=perplexing_eyes,
        ),
    ],
)