from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.card_effects.attacks_common import named_in_play

async def paired_attack(ctx):
    """Printed damage plus the partner's extra 20 and Special Condition."""
    partner = named_in_play('Chimchar')(ctx)
    printed = getattr(ctx.ability, "damage", 0) or 0
    await ctx.deal_damage(printed + (20 if partner else 0))
    if partner:
        defender = ctx.defender
        if defender is not None:
            await ctx.apply_special_condition(defender, SpecialConditions.BURNED)


card = PokemonCardDef(
    guid="74e3b07c-b275-5d6c-b911-ad816cbca154",
    key="POP9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Turtwig.Name",
    display_name="Turtwig",
    searchable_by=["Turtwig", "Basic", "Turtwig"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="POP9",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=387,
    abilities=[
        Attack(
            title="Absorb",
            game_text="Remove 1 damage counter from Turtwig.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Parboil",
            game_text="If you have Chimchar in play, this attack does 40 damage plus 20 more damage and the Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=paired_attack,
        ),
    ],
)