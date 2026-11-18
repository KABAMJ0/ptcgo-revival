from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import (
    PokemonTypes, PokemonStage, Rarities, SpecialConditions,
)
from ptcgo.game.card_effects.attacks_common import mill_attack, recoil_attack


async def _burn_defender(ctx):
    if ctx.defender is not None:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)

card = PokemonCardDef(
    guid="64398753-b146-5681-80b0-b04cbaa04ec6",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SlitherWing.Name",
    display_name="Slither Wing",
    searchable_by=["Slither Wing", "Basic", "Ancient", "SlitherWing"],
    subtypes=["Basic", "Ancient"],
    collector_number=107,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=988,
    abilities=[
        Attack(
            title="Stomp Off",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=mill_attack(1),
        ),
        Attack(
            title="Burning Turbulence",
            game_text="This Pok\u00e9mon also does 90 damage to itself. Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=120,
            effect=recoil_attack(90, also=_burn_defender),
        ),
    ],
)