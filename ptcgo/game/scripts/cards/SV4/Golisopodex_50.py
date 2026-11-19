from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import snipe_attack

async def electro_wheel(ctx):
    await ctx.deal_damage()
    picks = await ctx.discard_energy_from(ctx.attacker, 1, prompt="Discard an Energy from this Pokémon.")
    if not picks:
        return
    bench = ctx.my_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.player_id, target)


async def electro_wheel(ctx):
    await ctx.deal_damage()
    picks = await ctx.discard_energy_from(ctx.attacker, 1, prompt="Discard an Energy from this Pokémon.")
    if not picks:
        return
    bench = ctx.my_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.player_id, target)


card = PokemonCardDef(
    guid="92868d4c-e80b-510b-b216-8699f2fc3f53",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golisopodex.Name",
    display_name="Golisopod ex",
    searchable_by=["Golisopod ex", "Stage 1", "ex", "Golisopodex"],
    subtypes=["Stage 1", "ex"],
    collector_number=50,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=270,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wimpod.Name",
    family_id=767,
    abilities=[
        Attack(
            title="Aqua Blade",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
        Attack(
            title="Swing and Skedaddle",
            game_text="Discard an Energy from this Pok\u00e9mon. If you do, switch it with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=170,
            effect=electro_wheel,
        ),
    ],
)