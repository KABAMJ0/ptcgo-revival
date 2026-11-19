from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, subtypes_for
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities


async def healing_breath(ctx):
    """Remove all damage counters from each of your Pokemon SP."""
    for pokemon in ctx.my_pokemon_in_play():
        if "SP" not in (subtypes_for(pokemon.archetype_id) or []):
            continue
        missing = ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0)
        if missing > 0:
            await ctx.heal(missing, pokemon)


async def dragon_rush(ctx):
    """Discard 2 Energy from Garchomp C, then 80 to a chosen opposing Pokemon
    (Weakness and Resistance apply only to the Active one)."""
    await ctx.discard_energy_from(
        ctx.attacker, 2, prompt="Discard 2 Energy attached to Garchomp C")
    pool = ctx.opponent_pokemon_in_play()
    if not pool:
        return
    target = await ctx.choose_pokemon(pool, "Choose 1 of your opponent's Pok\u00e9mon")
    if target is None:
        return
    await ctx.deal_damage(80, target=target)

card = PokemonCardDef(
    guid="c0308a43-6c57-5ac4-954a-d7c294f82e3e",
    key="CEL25C",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GarchompCLVX.Name",
    display_name="Garchomp C LV.X",
    searchable_by=["Garchomp C LV.X", "Level-Up", "SP", "GarchompCLVX"],
    subtypes=["Level-Up", "SP"],
    collector_number=145,
    set_code="CEL25C",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.COLORLESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GarchompC.Name",
    family_id=445,
    abilities=[
        Ability(
            title="Healing Breath",
            game_text="Once during your turn (before your attack), when you put Garchomp C LV.X from your hand onto your Active Garchomp C, you may remove all damage counters from each of your Pok\u00e9mon SP.",
            trigger=Triggers.ON_EVOLVE,
            effect=healing_breath,
        ),
        Attack(
            title="Dragon Rush",
            game_text="Discard 2 Energy attached to Garchomp C. Choose 1 of your opponent's Pok\u00e9mon. This attack does 80 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Garchomp C can't use Dragon Rush during your next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            locks_next_turn=True,
            effect=dragon_rush,
        ),
    ],
)