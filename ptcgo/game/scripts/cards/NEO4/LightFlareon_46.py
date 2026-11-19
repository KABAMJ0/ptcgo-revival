from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import energy_provides_type


async def _warm_up(ctx):
    """Warm Up: a Fire Energy out of the deck onto a Benched Pokemon."""
    bench = ctx.my_bench()
    if not bench:
        return
    found = await ctx.search_deck(
        predicate=lambda c: energy_provides_type(c, PokemonTypes.FIRE.value),
        count=1, minimum=1, prompt="Choose a Fire Energy card")
    if not found:
        await ctx.shuffle_deck()
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokemon")
    if target is not None:
        await ctx.attach_energy(found[0], target)
    await ctx.shuffle_deck()

from ptcgo.game.card_effects.pokemon import energy_provides_type


def _fire_energy(card):
    return energy_provides_type(card, PokemonTypes.FIRE.value)


async def burning_flame(ctx):
    """Two coins: on either tails the attack does nothing at all; otherwise 30
    plus 20 per heads, with a Fire Energy discarded per heads."""
    flips = await ctx.flip_coins(2, "Burning Flame")
    heads = sum(1 for flip in flips if flip)
    if heads < 2:
        return
    fire = [e for e in ctx.attached_energies(ctx.attacker) if _fire_energy(e)]
    if len(fire) < heads:
        return
    for _ in range(heads):
        await ctx.discard_energy_from(ctx.attacker, 1, predicate=_fire_energy,
                                      prompt="Discard a Fire Energy")
    await ctx.deal_damage(30 + 20 * heads)

card = PokemonCardDef(
    guid="2d0dc74f-1f8b-5eb5-a135-e135471e6fa0",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LightFlareon.Name",
    display_name="Light Flareon",
    searchable_by=["Light Flareon", "Stage 1", "LightFlareon"],
    subtypes=["Stage 1"],
    collector_number=46,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=136,
    abilities=[
        Attack(
            title="Warm Up",
            game_text="If you have any benched Pok\u00e9mon, search your deck for a Fire Energy card and attach it to 1 of them. Then shuffle your deck.",
            cost={PokemonTypes.FIRE: 1},
            effect=_warm_up,
        ),
        Attack(
            title="Burning Flame",
            game_text="Flip 2 coins. For each heads, discard a Fire Energy card attached to Light Flareon or this attack does nothing. This attack does 30 damage plus 20 damage for each heads.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=burning_flame,
        ),
    ],
)