from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import (
    AttrID, PokemonTypes, PokemonStage, Rarities, SpecialConditions,
)


MIRRORED = (SpecialConditions.BURNED, SpecialConditions.POISONED)


def _afflicted(pokemon, condition):
    conditions = pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
    labels = {str(label).lower() for label in conditions}
    return any(str(candidate).lower() in labels
               for candidate in (condition, condition.name, condition.value))


async def mirror_coat(ctx):
    holder = ctx.source
    attacker = ctx.damaged_by
    if holder is None or attacker is None or ctx.effects_blocked(attacker):
        return
    for condition in MIRRORED:
        if _afflicted(holder, condition):
            await ctx.apply_special_condition(attacker, condition)
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="0ba0ae4b-d08c-5aba-8f3b-1c57cb4205e6",
    key="POP2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Suicune.Name",
    display_name="Suicune",
    searchable_by=["Suicune", "Basic", "Suicune"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="POP2",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=245,
    abilities=[
        Ability(
            title="Mirror Coat",
            game_text="If Suicune is Burned or Poisoned by an opponent's attack (even if Suicune is Knocked Out), the Attacking Pok\u00e9mon is now affected by the same Special Conditions (1 if there is only 1).",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=mirror_coat,
        ),
        Attack(
            title="Bubblebeam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)