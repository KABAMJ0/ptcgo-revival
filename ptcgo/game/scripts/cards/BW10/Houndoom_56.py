from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, \
    SpecialConditions
from ptcgo.game.card_effects.attacks_common import bonus_if, no_retreat_attack
from ptcgo.game.card_effects.passives_common import has_team_plasma


def _defender_is_team_plasma(ctx) -> bool:
    defender = ctx.defender
    return defender is not None and has_team_plasma(ctx.board, defender)


async def _burn_team_plasma_defender(ctx) -> None:
    if _defender_is_team_plasma(ctx):
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)


card = PokemonCardDef(
    guid="1769730c-9294-5d22-9066-6be18244f1f5",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndoom.Name",
    display_name="Houndoom",
    searchable_by=["Houndoom", "Stage 1", "Houndoom"],
    subtypes=["Stage 1"],
    collector_number=56,
    set_code="BW10",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name",
    family_id=228,
    abilities=[
        Attack(
            title="Dark Clamp",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=no_retreat_attack(),
        ),
        Attack(
            title="Blazing Claws",
            game_text="If the Defending Pok\u00e9mon is a Team Plasma Pok\u00e9mon, this attack does 60 more damage, and the Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=bonus_if(_defender_is_team_plasma, 60,
                            also=_burn_team_plasma_defender),
        ),
    ],
)