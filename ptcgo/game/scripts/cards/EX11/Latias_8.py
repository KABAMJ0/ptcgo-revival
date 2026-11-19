from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _spiral_drain(ctx):
    """Remove 2 damage counters from this Pokemon, all if fewer."""
    holder = ctx.attacker
    if holder is None:
        return
    from ptcgo.game.attributes import AttrID
    damaged = ctx.max_hp(holder) - holder.get_attribute(AttrID.HP, 0)
    if damaged > 0:
        await ctx.heal(min(20, damaged), holder)

card = PokemonCardDef(
    guid="69c3b9c9-1986-54b1-9f71-592d3cb45932",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latias.Name",
    display_name="Latias δ",
    searchable_by=["Latias \u03b4", "Basic", "Latias"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="EX11",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING, PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=380,
    abilities=[
        Ability(
            title="Delta Aura",
            game_text="If you have Latios or Latios ex in play, the attack cost of Latias's Extra Crush is now Lightning MetalColorless.",
            effect=unimplemented,
        ),
        Attack(
            title="Spiral Drain",
            game_text="Remove 2 damage counters fro Latias.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=_spiral_drain,
        ),
        Attack(
            title="Extra Crush",
            game_text="If your opponent has no Pok\u00e9mon-ex in play, this attack does nothing.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=unimplemented,
        ),
    ],
)