from ptcgo.game.data_utils import ItemCardDef, def_for
from ptcgo.game.attributes import Rarities

def _named(card, name):
    definition = def_for(card.archetype_id)
    return bool(definition) and definition.display_name == name


def _second_copy(ctx):
    return next((c for c in ctx.hand()
                 if c.entity_id != ctx.source.entity_id
                 and _named(c, "Pok\u00e9 Blower +")), None)


async def _pok_blower(ctx):
    """2 copies at once: switch an opposing Benched Pokemon into the Active
    Spot. 1 copy: flip a coin and put 1 damage counter on an opposing Pokemon
    on heads."""
    pair = _second_copy(ctx)
    if pair is not None and await ctx.ask_yes_no(
            "Play a second Pok\u00e9 Blower + to switch the opponent's Active "
            "Pokemon instead?"):
        await ctx.discard_cards([pair])
        target = await ctx.choose_pokemon(
            ctx.opponent_bench(), "Choose the opponent's new Active Pokemon")
        if target is not None:
            await ctx.switch_active(ctx.opponent_id, target)
        return
    coins = await ctx.flip_coins(1, "Pok\u00e9 Blower +")
    if not coins or not coins[0]:
        return
    target = await ctx.choose_pokemon(
        ctx.opponent_pokemon_in_play(), "Choose a Pokemon to put 1 damage counter on")
    if target is not None:
        await ctx.place_damage_counters(1, [target])


card = ItemCardDef(
    guid="0c49c6ac-6d99-5347-a613-b05dc7eb95e3",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokBlower.Name",
    display_name="Poké Blower +",
    searchable_by=["Pok\u00e9 Blower +", "Item"],
    subtypes=["Item"],
    collector_number=88,
    set_code="DP7",
    rarity=Rarities.Uncommon,
    effect=_pok_blower,
)
