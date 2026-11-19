from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.attributes import SpecialConditions


async def toxic_saliva(ctx):
    """On heads the Defending Pokemon is Poisoned for 20 a turn."""
    heads = await ctx.flip_coins(1, "Toxic Saliva")
    if heads and heads[0]:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED,
                                          poison_counters=2)

card = PokemonCardDef(
    guid="474a45d9-8c09-5324-a023-77bb0a9ca25d",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shuckle.Name",
    display_name="Shuckle",
    searchable_by=["Shuckle", "Basic", "Shuckle"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="NEO3",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=213,
    abilities=[
        Ability(
            title="Hard Shell",
            game_text="Whenever an attack (including your own) does 40 or less damage to Shuckle (after applying Weakness and Resistance), reduce that damage to 10. (Any other effects of attacks still happen.) This power stops working while Shuckle is Asleep, Confused, or Paralyzed.",
            effect=unimplemented,
        ),
        Attack(
            title="Toxic Saliva",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned. It now takes 20 Poison damage instead of 10 after each player's turn (even if it was already Poisoned).",
            cost={PokemonTypes.GRASS: 2},
            effect=toxic_saliva,
        ),
    ],
)