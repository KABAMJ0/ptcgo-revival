from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.passives_common import shield_from_defender_next_turn


async def negative_ion(ctx):
    """Printed 10, and the Defending Pokemon does 10 less to Chinchou next turn."""
    await ctx.deal_damage()
    await shield_from_defender_next_turn(reduce=10)(ctx)

card = PokemonCardDef(
    guid="d9d88eb3-4217-5007-b71f-9b93ee9ef397",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chinchou.Name",
    display_name="Chinchou",
    searchable_by=["Chinchou", "Basic", "Chinchou"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="NEO3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=170,
    abilities=[
        Attack(
            title="Positive Ion",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 10 more damage. If tails, this attack does 10 damage.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            damage_operator="+",
            effect=flip_damage(base=10, bonus=10),
        ),
        Attack(
            title="Negative Ion",
            game_text="If the Defending Pok\u00e9mon attacks Chinchou during your opponent's next turn, any damage done to Chinchou is reduced by 10 (before applying Weakness and Resistance). (Benching or evolving either Pok\u00e9mon ends this effect.)",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=negative_ion,
        ),
    ],
)