from ptcgo.game.data_utils import (PokemonCardDef, Attack, Ability,
                                      Triggers, unimplemented)


async def _dragon_pulse(ctx):
    """Flip 3 coins: 1 damage counter on each of their Benched
    Pokemon per heads."""
    results = await ctx.flip_coins(3)
    for _ in range(sum(1 for heads in results if heads)):
        for pokemon in ctx.opponent_bench():
            if not ctx.effects_blocked(pokemon):
                await ctx.deal_damage(10, target=pokemon,
                                      apply_modifiers=False,
                                      as_counters=True)
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="094f4273-088c-553b-a534-57a423fd4e2d",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GarchompLVX.Name",
    display_name="Garchomp LV.X",
    searchable_by=["Garchomp LV.X", "Level-Up", "GarchompLVX"],
    subtypes=["Level-Up"],
    collector_number=97,
    set_code="DP5",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.COLORLESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Garchomp.Name",
    family_id=445,
    abilities=[
        Ability(
            title="Dragon Pulse",
            game_text="Once during your turn (before your attack), when you put Garchomp LV.X from your hand onto your Active Garchomp, you may flip 3 coins. For each heads, put 1 damage counter on each of your opponent's Benched Pok\u00e9mon.",
            trigger=Triggers.ON_EVOLVE,
            effect=_dragon_pulse,
        ),
        Attack(
            title="Restore",
            game_text="Search your discard pile for a Pok\u00e9mon (excluding Pok\u00e9mon LV.X) and put it onto your Bench as a Basic Pok\u00e9mon. Then, you may search your discard pile for up to 3 basic Energy cards and attach them to that Pok\u00e9mon.",
            cost={},
            effect=unimplemented,
        ),
    ],
)