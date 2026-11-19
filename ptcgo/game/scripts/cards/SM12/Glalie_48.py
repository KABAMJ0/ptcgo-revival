from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import flip_discard_opponent_energy

async def _ice_fang(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Ice Fang")
    if results and results[0]:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)
        await ctx.discard_energy_from(ctx.defender, 1)


card = PokemonCardDef(
    guid="47beaee1-765e-5f0f-bc44-8422dc2c5371",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glalie.Name",
    display_name="Glalie",
    searchable_by=["Glalie", "Stage 1", "Glalie"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="SM12",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name",
    family_id=361,
    abilities=[
        Attack(
            title="Ice Fang",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed, and discard an Energy from that Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=_ice_fang,
        ),
        Attack(
            title="Frosty Typhoon",
            game_text="This Pok\u00e9mon can't use Frosty Typhoon during your next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=unimplemented,
        ),
    ],
)