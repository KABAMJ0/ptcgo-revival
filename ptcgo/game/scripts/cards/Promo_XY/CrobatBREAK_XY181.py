from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def silent_bite(ctx):
    """Printed 60; you may Paralyze the Defending Pokemon, and if you do this
    Pokemon and everything attached to it go back into the deck."""
    from ptcgo.game.attributes import SpecialConditions
    await ctx.deal_damage()
    if not await ctx.ask_yes_no("Leave the Defending Pokemon Paralyzed?"):
        return
    defender = ctx.defender
    if defender is not None:
        await ctx.apply_special_condition(defender, SpecialConditions.PARALYZED)
    attacker = ctx.attacker
    if attacker is not None:
        await ctx.shuffle_into_deck([attacker] + list(getattr(attacker, "children", None) or []))


card = PokemonCardDef(
    guid="6f80fe6e-99a8-5010-8d40-4df848a9b7c6",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CrobatBREAK.Name",
    display_name="Crobat BREAK",
    searchable_by=["Crobat BREAK", "BREAK", "CrobatBREAK"],
    subtypes=["BREAK"],
    collector_number=181,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Crobat.Name",
    family_id=169,
    abilities=[
        Attack(
            title="Silent Bite",
            game_text="You may leave your opponent's Active Pok\u00e9mon Paralyzed. If you do, shuffle this Pok\u00e9mon and all cards attached to into your deck.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=silent_bite,
        ),
    ],
)