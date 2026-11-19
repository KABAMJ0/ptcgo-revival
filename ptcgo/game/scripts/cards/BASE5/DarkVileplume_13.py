from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.passives_common import play_lock_passive

_hay_fever = play_lock_passive("trainer", opponents_only=False)
from ptcgo.game.attributes import SpecialConditions


async def petal_whirlwind(ctx):
    """One coin per Fire Energy... no: the printed count is the number of coins
    on the card's own text; 30 per heads, and Confused at 2 or more heads."""
    flips = await ctx.flip_coins(2, "Petal Whirlwind")
    heads = sum(1 for flip in flips if flip)
    if heads == 0:
        return
    await ctx.deal_damage(30 * heads)
    if heads >= 2:
        await ctx.apply_special_condition(ctx.attacker, SpecialConditions.CONFUSED)

card = PokemonCardDef(
    guid="b00d2943-c9f6-5984-9346-2103001187e5",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkVileplume.Name",
    display_name="Dark Vileplume",
    searchable_by=["Dark Vileplume", "Stage 2", "DarkVileplume"],
    subtypes=["Stage 2"],
    collector_number=13,
    set_code="BASE5",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DarkGloom.Name",
    family_id=43,
    abilities=[
        Ability(
            title="Hay Fever",
            game_text="No Trainer cards can be played. This power stops working while Dark Vileplume is Asleep, Confused, or Paralyzed.",
            passive=_hay_fever,
        ),
        Attack(
            title="Petal Whirlwind",
            game_text="Flip a coins. This attack does 30 damage times the number of heads. If you get 2 or more heads, Dark Vileplume is now Confused (after doing damage).",
            cost={PokemonTypes.GRASS: 3},
            damage=30,
            damage_operator="x",
            effect=petal_whirlwind,
        ),
    ],
)