from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import def_for
from ptcgo.game.card_effects.pokemon import is_pokemon_ex
from ptcgo.game.session.passives import Passive, carrier_pokemon


def _named(pokemon) -> str:
    definition = def_for(getattr(pokemon, "archetype_id", "") or "")
    return (getattr(definition, "display_name", "") or "").lower()


def _latios_in_play(pokemon, board) -> bool:
    """'If you have Latios or Latios ex in play' -- any Latios, not a -EX/-GX
    print, on the holder's own side."""
    for other in board.pokemon_in_play(pokemon.owning_player_id):
        name = _named(other)
        if name.startswith("latios") and "-" not in name:
            return True
    return False


class _DeltaAuraExtraCrush(Passive):
    """With Latios in play, Latias's Extra Crush costs Lightning Metal
    Colorless (printed: Lightning Metal Colorless Colorless Colorless)."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        if (cost.get("Colorless") != 3 or cost.get("Lightning") != 1
                or cost.get("Metal") != 1):
            return cost
        if not _latios_in_play(pokemon, board):
            return cost
        cost["Colorless"] = 1
        return cost


async def _extra_crush(ctx):
    """Nothing at all unless the opponent has a Pokemon-ex in play."""
    if any(is_pokemon_ex(pokemon) for pokemon in ctx.opponent_pokemon_in_play()):
        await ctx.deal_damage()


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
            passive=_DeltaAuraExtraCrush(),
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
            effect=_extra_crush,
        ),
    ],
)