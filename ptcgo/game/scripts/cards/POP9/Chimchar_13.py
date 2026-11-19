from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.card_effects.attacks_common import named_in_play

async def paired_attack(ctx):
    """Printed damage plus the partner's extra 20 and Special Condition."""
    partner = named_in_play('Piplup')(ctx)
    printed = getattr(ctx.ability, "damage", 0) or 0
    await ctx.deal_damage(printed + (20 if partner else 0))
    if partner:
        defender = ctx.defender
        if defender is not None:
            await ctx.apply_special_condition(defender, SpecialConditions.ASLEEP)


card = PokemonCardDef(
    guid="1da86946-0538-5050-ba54-baee23afc99d",
    key="POP9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chimchar.Name",
    display_name="Chimchar",
    searchable_by=["Chimchar", "Basic", "Chimchar"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="POP9",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=390,
    abilities=[
        Attack(
            title="Serial Swipes",
            game_text="Flip 4 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            damage_operator="x",
            effect=flip_damage(coins=4, per_heads=10),
        ),
        Attack(
            title="Sleepy",
            game_text="If you have Piplup in play, this attack does 40 damage plus 20 more damage and the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=paired_attack,
        ),
    ],
)