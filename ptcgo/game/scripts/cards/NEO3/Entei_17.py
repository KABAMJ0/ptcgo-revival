from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.pokemon import energy_provides_type


async def mega_flame(ctx):
    """Printed 50, then one Fire Energy discarded per tails of two."""
    await ctx.deal_damage()
    flips = await ctx.flip_coins(2, "Mega Flame")
    tails = sum(1 for flip in flips if not flip)
    for _ in range(tails):
        gone = await ctx.discard_energy_from(
            ctx.attacker, 1,
            predicate=lambda card: energy_provides_type(card, PokemonTypes.FIRE.value),
            prompt="Discard a Fire Energy from Entei")
        if not gone:
            break

card = PokemonCardDef(
    guid="a8aa24a3-0ea8-5bd6-81ad-9ee17eb52979",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Entei.Name",
    display_name="Entei",
    searchable_by=["Entei", "Basic", "Entei"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="NEO3",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    family_id=244,
    abilities=[
        Ability(
            title="Legendary Body",
            game_text="As long as Entei is your Active Pok\u00e9mon, Entei and Energy cards attached to it aren't affected by effects from Trainer cards other than Stadium cards. As long as this Power is active, discard any Trainer cards attached to Entei. (This power works even if Entei is Asleep, Confused, or Paralyzed.)",
            effect=unimplemented,
        ),
        Attack(
            title="Mega Flame",
            game_text="Flip 2 coins. For each tails, discard 1 Fire Energy card from Entei, if it has any.",
            cost={PokemonTypes.FIRE: 3},
            damage=50,
            effect=mega_flame,
        ),
    ],
)