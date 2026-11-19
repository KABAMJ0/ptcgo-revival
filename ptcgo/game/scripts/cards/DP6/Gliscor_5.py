from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.card_effects.attacks_common import bonus_if, defender_has_any_condition
from ptcgo.game.card_effects.support_common import remove_self_from_play


async def _burning_poison(ctx):
    choice = await ctx.choose("Choose Burned or Poisoned", ["Burned", "Poisoned"])
    condition = SpecialConditions.BURNED if choice == "Burned" else SpecialConditions.POISONED
    if ctx.defender is not None:
        await ctx.apply_special_condition(ctx.defender, condition)
    if await ctx.ask_yes_no("Return Gliscor and all cards attached to it to your hand?"):
        await remove_self_from_play(destination="hand", optional=False)(ctx)


card = PokemonCardDef(
    guid="2054cd68-1089-59f9-9d99-8915ff1983ce",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gliscor.Name",
    display_name="Gliscor",
    searchable_by=["Gliscor", "Stage 1", "Gliscor"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="DP6",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gligar.Name",
    family_id=207,
    abilities=[
        Attack(
            title="Burning Poison",
            game_text="Choose either Burned or Poisoned. The Defending Pok\u00e9mon is now affected by that Special Condition. You may return Gliscor and all cards attached to it to your hand.",
            cost={},
            effect=_burning_poison,
        ),
        Attack(
            title="Pester",
            game_text="If the Defending Pok\u00e9mon is affected by a Special Condition, this attack does 40 damage plus 40 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            effect=bonus_if(defender_has_any_condition, 40),
        ),
    ],
)