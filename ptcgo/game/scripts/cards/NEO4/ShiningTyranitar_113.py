from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import energy_provides_type


def _is_fire(energy):
    return energy_provides_type(energy, PokemonTypes.FIRE.value)


async def _mountain_crush(ctx):
    await ctx.deal_damage()
    heads = await ctx.flip_until_tails("Mountain Crush")
    milled = ctx.deck_top(heads, player_id=ctx.opponent_id) if heads > 0 else []
    if milled:
        await ctx.discard_cards(milled)


async def _destructive_fire(ctx):
    attacker = ctx.attacker
    if attacker is None:
        return
    fire = [energy for energy in ctx.attached_energies(attacker) if _is_fire(energy)]
    if not fire:
        return
    results = await ctx.flip_coins(len(fire), "Destructive Fire")
    heads = sum(1 for result in results if result)
    if heads:
        await ctx.discard_energy_from(
            attacker, heads, predicate=_is_fire,
            prompt="Discard Fire Energy from Shining Tyranitar")
    await ctx.deal_damage()
    defender = ctx.defender
    if heads and defender is not None and not ctx.effects_blocked(defender):
        await ctx.discard_energy_from(
            defender, heads,
            prompt="Discard Energy from the Defending Pok\u00e9mon")


card = PokemonCardDef(
    guid="21f61cd0-03dc-5aad-804b-9c2491572500",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShiningTyranitar.Name",
    display_name="Shining Tyranitar",
    searchable_by=["Shining Tyranitar", "Basic", "ShiningTyranitar"],
    subtypes=["Basic"],
    collector_number=113,
    set_code="NEO4",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=248,
    abilities=[
        Attack(
            title="Mountain Crush",
            game_text="Flip a coin until you get tails. For each heads, your opponent discards the top card from his or her deck.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.FIGHTING: 2},
            damage=30,
            effect=_mountain_crush,
        ),
        Attack(
            title="Destructive Fire",
            game_text="Flip a coin for each Fire Energy card attached to Shining Tyranitar. For each heads, discard a Fire Energy card attached to Shining Tyranitar or this attack does nothing. Then, for each heads, choose an Energy card attached to the Defending Pok\u00e9mon and discard it. If it has fewer Energy cards than that, remove all of them.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.FIRE: 3},
            damage=50,
            effect=_destructive_fire,
        ),
    ],
)