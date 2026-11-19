from ptcgo.game.card_effects.pokemon import is_fire_energy

from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack


async def kindle(ctx):
    """70, then one Energy off Flareon and one off the Defending Pokemon."""
    await ctx.deal_damage(70)
    await ctx.discard_energy_from(ctx.attacker, 1)
    defender = ctx.defender
    if defender is not None and not ctx.effects_blocked(defender):
        await ctx.discard_energy_from(defender, 1)

card = PokemonCardDef(
    guid="cfa87aa5-131f-55ab-ad76-29ce8669a650",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flareon.Name",
    display_name="Flareon",
    searchable_by=["Flareon", "Stage 1", "Flareon"],
    subtypes=["Stage 1"],
    collector_number=19,
    set_code="DP5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Fire Fang",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.BURNED, flip=True),
        ),
        Attack(
            title="Kindle",
            game_text="Discard an Energy card attached to Flareon and then discard an Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=kindle,
        ),
    ],
)