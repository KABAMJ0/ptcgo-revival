from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import RetaliateCountersPassive, Passive
from ptcgo.game.data_utils import def_for
from ptcgo.game.card_effects.support_common import switch_self_attack


def _tyrogue_under(pokemon) -> bool:
    """Whether a Tyrogue is tucked under `pokemon` ("If Tyrogue is anywhere
    under this Pokemon" -- DP6's Hitmon line)."""
    for child in getattr(pokemon, "children", []) or []:
        name = getattr(def_for(getattr(child, "archetype_id", "") or ""), "display_name", "") or ""
        if name == "Tyrogue":
            return True
    return False

async def _gut_spin(ctx):
    """Gut Spin: printed damage, then optionally spin out with Tyrogue under."""
    await ctx.deal_damage()
    if _tyrogue_under(ctx.attacker):
        await switch_self_attack(damage=0, optional=True)(ctx)

card = PokemonCardDef(
    guid="9c531979-4d20-597d-9069-5ebdd2ca456e",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hitmontop.Name",
    display_name="Hitmontop",
    searchable_by=["Hitmontop", "Basic", "Hitmontop"],
    subtypes=["Basic"],
    collector_number=101,
    set_code="DP6",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=237,
    abilities=[
        Attack(
            title="Triple Kick",
            game_text="Flip 3 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=20),
        ),
        Attack(
            title="Gut Spin",
            game_text="If Tyrogue is anywhere under Hitmontop, you may switch Hitmontop with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=_gut_spin,
        ),
    ],
)