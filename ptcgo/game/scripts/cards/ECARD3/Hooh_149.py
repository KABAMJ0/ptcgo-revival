from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.attributes import SpecialConditions


async def _scalding_steam(ctx):
    discarded = await ctx.discard_energy_from(
        ctx.attacker, 1, prompt="Discard an Energy card attached to Ho-oh")
    results = await ctx.flip_coins(1, "Scalding Steam")
    if results and results[0] and ctx.defender is not None:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="eba887a5-8e84-5a2d-90a3-3326c67595bf",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hooh.Name",
    display_name="Ho-oh",
    searchable_by=["Ho-oh", "Basic", "Hooh"],
    subtypes=["Basic"],
    collector_number=149,
    set_code="ECARD3",
    rarity=Rarities.RareSecret,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=250,
    abilities=[
        Ability(
            title="Crystal Type",
            game_text="Whenever you attach a Fire, Water, or Lightning basic Energy card from your hand to Ho-oh, Ho-oh's type (color) becomes the same as that type of Energy until the end of the turn.",
            effect=unimplemented,
        ),
        Attack(
            title="Holy Flame",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 1},
            damage=20,
        ),
        Attack(
            title="Scalding Steam",
            game_text="Discard an Energy card attached to Ho-oh and flip a coin. If heads, the Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=_scalding_steam,
        ),
    ],
)