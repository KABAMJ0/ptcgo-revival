from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.pokemon import energy_provides_type


async def hyper_flame(ctx):
    """Printed 60, then heads discards 1 Fire Energy and tails discards every
    Energy attached to Moltres."""
    await ctx.deal_damage()
    fire = [card for card in ctx.attached_energies(ctx.attacker)
            if energy_provides_type(card, PokemonTypes.FIRE.value)]
    if not fire:
        return
    heads = await ctx.flip_coins(1, "Hyper Flame")
    if heads and heads[0]:
        await ctx.discard_energy_from(
            ctx.attacker, 1,
            predicate=lambda card: energy_provides_type(card, PokemonTypes.FIRE.value),
            prompt="Discard 1 Fire Energy attached to Moltres")
    else:
        await ctx.discard_energy_from(
            ctx.attacker, len(ctx.attached_energies(ctx.attacker)),
            prompt="Discard all Energy attached to Moltres")

card = PokemonCardDef(
    guid="55792970-2f0a-51dd-9759-78188de43b81",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Moltres.Name",
    display_name="Moltres",
    searchable_by=["Moltres", "Basic", "Moltres"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=146,
    abilities=[
        Attack(
            title="Hyper Flame",
            game_text="Flip a coin. If heads, discard 1 Fire Energy card attached to Moltres. If tails, discard all Energy cards attached to Moltres. If you can't discard Energy cards, this attack does nothing.",
            cost={PokemonTypes.FIRE: 3},
            damage=60,
            effect=hyper_flame,
        ),
    ],
)