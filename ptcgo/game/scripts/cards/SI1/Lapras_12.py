from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack


async def gentle_song(ctx):
    for target in (ctx.attacker, ctx.defender):
        if target is None:
            continue
        if target.get_attribute(AttrID.HP, 0) < ctx.max_hp(target):
            await ctx.heal(20, target)
    await ctx.apply_special_condition(ctx.defender, SpecialConditions.ASLEEP)

card = PokemonCardDef(
    guid="e4cf8192-a562-546b-971f-79dfff355ee0",
    key="SI1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lapras.Name",
    display_name="Lapras",
    searchable_by=["Lapras", "Basic", "Lapras"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="SI1",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=131,
    abilities=[
        Attack(
            title="Gentle Song",
            game_text="If Lapras has any damage counters on it, remove 2 of them from it (1 if it only has 1). If the Defending Pok\u00e9mon has any damage counters on it, remove 2 of them from it (1 if it only has 1). The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=gentle_song,
        ),
        Attack(
            title="Ice Beam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 2},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)