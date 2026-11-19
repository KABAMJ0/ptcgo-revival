from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES, SpecialConditions


async def poison_effect(ctx):
    """Printed 20, or 80 and the Poison cured while Seviper is Poisoned."""
    poisoned = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.POISONED] in \
        (ctx.attacker.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
    await ctx.deal_damage(80 if poisoned else 20)
    if poisoned:
        await ctx.cure_condition(ctx.attacker, SpecialConditions.POISONED)

card = PokemonCardDef(
    guid="f7fa8156-1660-51d5-acd3-8b73b29e81af",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seviper.Name",
    display_name="Seviper",
    searchable_by=["Seviper", "Basic", "Seviper"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="COL",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=336,
    abilities=[
        Attack(
            title="Poison Buildup",
            game_text="Seviper is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Poison Effect",
            game_text="If Seviper is Poisoned, this attack does 20 damage plus 60 more damage and remove the Special Condition Poisoned from Seviper.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=poison_effect,
        ),
    ],
)