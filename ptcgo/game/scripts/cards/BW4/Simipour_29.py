from ptcgo.game.card_effects.attacks_common import stadium_in_play_cond
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def _simipour_29(ctx):
    """Printed 30, +30 and the defender asleep while a Stadium is in play."""
    has_stadium = stadium_in_play_cond(ctx)
    await ctx.deal_damage(30 + (30 if has_stadium else 0))
    defender = ctx.defender
    if has_stadium and defender is not None and not ctx.effects_blocked(defender):
        await ctx.apply_special_condition(defender, SpecialConditions.ASLEEP)
from ptcgo.game.card_effects.support_common import draw_attack

card = PokemonCardDef(
    guid="d062871a-5423-5c07-8071-e4cf5adf2784",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Simipour.Name",
    display_name="Simipour",
    searchable_by=["Simipour", "Stage 1", "Simipour"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="BW4",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Panpour.Name",
    family_id=515,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw 3 cards.",
            cost={PokemonTypes.WATER: 1},
            effect=draw_attack(3),
        ),
        Attack(
            title="Stadium Wave",
            game_text="If there is any Stadium card in play, this attack does 30 more damage and the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=_simipour_29,
        ),
    ],
)