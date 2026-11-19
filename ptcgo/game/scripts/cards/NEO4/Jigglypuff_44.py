from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import apply_protection


async def _expand(ctx):
    """Expand: printed damage, then -10 taken through their next turn."""
    await ctx.deal_damage()
    await apply_protection(ctx, reduce=10)

card = PokemonCardDef(
    guid="8fd4c6db-d072-54ce-9912-3801ec1efb92",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name",
    display_name="Jigglypuff",
    searchable_by=["Jigglypuff", "Basic", "Jigglypuff"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=39,
    abilities=[
        Attack(
            title="Expand",
            game_text="All damage done to Jigglypuff during your opponent's next turn is reduced by 10 (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            effect=_expand,
        ),
    ],
)