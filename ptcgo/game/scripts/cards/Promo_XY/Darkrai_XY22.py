from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.card_effects.attacks_common import bonus_if, defender_has_condition

async def _deep_wind_heal(ctx):
    await ctx.heal(30, target=ctx.attacker)


# Printed 60, +60 and heal 30 from this Pokemon while the defender is Asleep.
deep_wind = bonus_if(defender_has_condition(SpecialConditions.ASLEEP), 60,
                     also=_deep_wind_heal)


card = PokemonCardDef(
    guid="f4deaaec-ac97-5081-b232-7d9701b72616",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Darkrai.Name",
    display_name="Darkrai",
    searchable_by=["Darkrai", "Basic", "Darkrai"],
    subtypes=["Basic"],
    collector_number=22,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=491,
    abilities=[
        Attack(
            title="Hypnoblast",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Deep Wind",
            game_text="If your opponent's Active Pok\u00e9mon is Asleep, this attack does 60 more damage and heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=deep_wind,
        ),
    ],
)