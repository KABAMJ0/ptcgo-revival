from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import (
    AttrID, CLIENT_SPECIAL_CONDITION_NAMES, PokemonTypes, PokemonStage,
    Rarities, SpecialConditions,
)
from ptcgo.game.card_effects.attacks_common import condition_attack


async def poison_boost(ctx):
    """Printed 80, +80 while this Pokemon is Poisoned; then that condition is
    removed from it."""
    attacker = ctx.attacker
    poison = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.POISONED]
    poisoned = attacker is not None \
        and poison in (attacker.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
    await ctx.deal_damage(80 + (80 if poisoned else 0))
    if poisoned:
        await ctx.cure_condition(attacker, SpecialConditions.POISONED)


card = PokemonCardDef(
    guid="bbef14a1-fd41-5bf4-81a4-2cab9a42438c",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxicroak.Name",
    display_name="Toxicroak",
    searchable_by=["Toxicroak", "Stage 1", "Toxicroak"],
    subtypes=["Stage 1"],
    collector_number=55,
    set_code="SM3",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Croagunk.Name",
    family_id=453,
    abilities=[
        Attack(
            title="Poison Jab",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
        Attack(
            title="Poison Boost",
            game_text="If this Pok\u00e9mon is Poisoned, this attack does 80 more damage. Then, remove that Special Condition from this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=poison_boost,
        ),
    ],
)