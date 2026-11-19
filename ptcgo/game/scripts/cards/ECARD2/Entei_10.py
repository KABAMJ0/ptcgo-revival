from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import (PokemonTypes, PokemonStage, Rarities,
                                    SpecialConditions)
from ptcgo.game.card_effects.attacks_common import energy_provides_type


async def _burning_fang(ctx):
    """Printed damage, then on heads discard one attached Fire Energy and Burn
    the Defending Pokemon."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Burning Fang")
    if not (results and results[0]):
        return
    await ctx.discard_energy_from(
        ctx.attacker, 1,
        predicate=lambda e: energy_provides_type(e, PokemonTypes.FIRE.value),
        prompt="Choose a Fire Energy to discard from Entei")
    if ctx.defender is not None:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)


card = PokemonCardDef(
    guid="e778d8c6-411a-546b-93a6-8ea845849ff6",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Entei.Name",
    display_name="Entei",
    searchable_by=["Entei", "Basic", "Entei"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="ECARD2",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=244,
    abilities=[
        Ability(
            title="Pure Body",
            game_text="To attach a Fire Energy card from your hand to Entei, you must discard an Energy card attached to Entei. (Attach the Fire Energy, and then discard an Energy from Entei.)",
            effect=unimplemented,
        ),
        Attack(
            title="Burning Fang",
            game_text="You may flip a coin. If heads, discard a Fire Energy card attached to Entei and the Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=_burning_fang,
        ),
    ],
)