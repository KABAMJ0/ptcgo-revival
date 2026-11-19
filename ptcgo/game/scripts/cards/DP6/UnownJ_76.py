from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import Triggers
from ptcgo.game.session.effects import is_trainer_card
from ptcgo.game.attributes import SpecialConditions


async def _junk(ctx):
    """JUNK: heads pulls a Trainer out of the discard pile."""
    heads = await ctx.flip_coins(1, "JUNK")
    if not (heads and all(heads)):
        return
    pile = [c for c in ctx.discard_pile() if is_trainer_card(c)]
    if not pile:
        return
    picked = await ctx.choose_cards(pile, 1, prompt="Choose a Trainer card")
    if picked:
        await ctx.put_in_hand(picked)


async def _hidden_power_wake(ctx):
    """Hidden Power (Unown J): printed damage, then wake the Defending Pokemon."""
    await ctx.deal_damage()
    if ctx.defender is not None:
        await ctx.cure_condition(ctx.defender, SpecialConditions.ASLEEP)

card = PokemonCardDef(
    guid="a22141ac-1b4e-53d8-971a-3107ac0e050a",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownJ.Name",
    display_name="Unown [J]",
    searchable_by=["Unown [J]", "Basic", "UnownJ"],
    subtypes=["Basic"],
    collector_number=76,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="JUNK",
            game_text="Once during your turn, when you put Unown J from your hand onto your Bench, you may flip a coin. If heads, search your discard pile for a Trainer card, show it to your opponent, and put it into your hand.",
                        trigger=Triggers.ON_PLAY,
            effect=_junk,
        ),
        Attack(
            title="Hidden Power",
            game_text="Remove the Special Condition Asleep from the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=_hidden_power_wake,
        ),
    ],
)