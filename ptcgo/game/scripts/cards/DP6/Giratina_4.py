from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import damage_counters_on, damage_per
from ptcgo.game.card_effects.attacks_common import flip_gate, snipe_attack
from ptcgo.game.card_effects.passives_common import apply_protection


async def _shadow_force_shield(ctx):
    await apply_protection(ctx, prevent=True, effects_too=True)


async def _shadow_force_shield(ctx):
    await apply_protection(ctx, prevent=True, effects_too=True)


card = PokemonCardDef(
    guid="9716b7c8-ce3a-50d8-8cab-fa43b320a3c5",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Giratina.Name",
    display_name="Giratina",
    searchable_by=["Giratina", "Basic", "Giratina"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="DP6",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    family_id=487,
    abilities=[
        Attack(
            title="Shadow Force",
            game_text="Choose 1 of your opponent's Benched Pok\u00e9mon. This attack does 20 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Flip a coin. If heads, prevent all effects of an attack, including damage, done to Giratina during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=snipe_attack(20, pool="bench", count=1, also=flip_gate(then=_shadow_force_shield)),
        ),
        Attack(
            title="Brutal Edge",
            game_text="Does 50 damage plus 10 more damage for each damage counter on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=damage_per(damage_counters_on("defender"), 10, base=50),
        ),
    ],
)