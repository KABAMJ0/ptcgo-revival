from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.pokemon import energy_provides_type


async def twister(ctx):
    """Printed 30; on two tails it does nothing at all, and each heads discards
    an Energy from the Defending Pokemon."""
    flips = await ctx.flip_coins(2, "Twister")
    heads = sum(1 for flip in flips if flip)
    if heads == 0:
        return
    await ctx.deal_damage()
    if ctx.defender is not None:
        await ctx.discard_energy_from(
            ctx.defender, heads,
            prompt="Discard an Energy attached to the Defending Pokemon")

card = PokemonCardDef(
    guid="1325f29d-a8e3-5922-8400-d23a74f6f9f1",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeotto.Name",
    display_name="Pidgeotto",
    searchable_by=["Pidgeotto", "Stage 1", "Pidgeotto"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="COL",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgey.Name",
    family_id=16,
    abilities=[
        Attack(
            title="Gust",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Twister",
            game_text="Flip 2 coins. If both of them are tails, this attack does nothing. For each heads, discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            effect=twister,
        ),
    ],
)