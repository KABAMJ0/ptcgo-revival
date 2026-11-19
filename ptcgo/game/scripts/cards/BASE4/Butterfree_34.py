from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import gust_attack


import math
from ptcgo.game.attributes import AttrID
async def mega_drain(ctx):
    """Printed 40, then heal Butterfree a number of damage counters equal to
    half the damage dealt, rounded up to the nearest 10."""
    dealt = await ctx.deal_damage()
    if dealt <= 0 or ctx.attacker is None:
        return
    counters = math.ceil(math.ceil(dealt / 2) / 10)
    await ctx.heal(10 * counters, target=ctx.attacker)


card = PokemonCardDef(
    guid="2326ecfa-c2f2-53cd-b6bb-74f31321d870",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Butterfree.Name",
    display_name="Butterfree",
    searchable_by=["Butterfree", "Stage 2", "Butterfree"],
    subtypes=["Stage 2"],
    collector_number=34,
    set_code="BASE4",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Metapod.Name",
    family_id=10,
    abilities=[
        Attack(
            title="Whirlwind",
            game_text="If your opponent has any Benched Pok\u00e9mon, he or she chooses 1 of them and switches it with the Defending Pok\u00e9mon. (Do the damage before switching the Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=gust_attack(opponent_chooses=True),
        ),
        Attack(
            title="Mega Drain",
            game_text="Remove a number of damage counters from Butterfree equal to half the damage done to the Defending Pok\u00e9mon (after applying Weakness and Resistance) (rounded up to the nearest 10). If Butterfree has fewer damage counters than that, remove all of them.",
            cost={PokemonTypes.GRASS: 4},
            damage=40,
            effect=mega_drain,
        ),
    ],
)